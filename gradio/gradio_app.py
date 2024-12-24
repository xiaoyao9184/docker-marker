import os
import sys

if "APP_PATH" in os.environ:
    app_path = os.path.abspath(os.environ["APP_PATH"])
    if os.getcwd() != app_path:
        # fix sys.path for import
        os.chdir(app_path)
    if app_path not in sys.path:
        sys.path.append(app_path)

import gradio as gr

from marker.settings import settings

import base64
import io
import re
from typing import Any, Dict

import pypdfium2
from PIL import Image

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser
from marker.output import text_from_rendered


def load_models():
    return create_model_dict()

def convert_pdf(fname: str, config_parser: ConfigParser) -> (str, Dict[str, Any], dict):
    config_dict = config_parser.generate_config_dict()
    config_dict["pdftext_workers"] = 1
    converter = PdfConverter(
        config=config_dict,
        artifact_dict=model_dict,
        processor_list=config_parser.get_processors(),
        renderer=config_parser.get_renderer()
    )
    return converter(fname)

def open_pdf(pdf_file):
    return pypdfium2.PdfDocument(pdf_file)

def count_pdf(pdf_file):
    doc = open_pdf(pdf_file)
    return len(doc)

def get_page_image(pdf_file, page_num, dpi=96):
    doc = open_pdf(pdf_file)
    renderer = doc.render(
        pypdfium2.PdfBitmap.to_pil,
        page_indices=[page_num - 1],
        scale=dpi / 72,
    )
    png = list(renderer)[0]
    png_image = png.convert("RGB")
    return png_image


def img_to_html(img, img_alt):
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()
    encoded = base64.b64encode(img_bytes).decode()
    img_html = f'<img src="data:image/png;base64,{encoded}" alt="{img_alt}" style="max-width: 100%;">'
    return img_html

def markdown_insert_images(markdown, images):
    image_tags = re.findall(r'(!\[(?P<image_title>[^\]]*)\]\((?P<image_path>[^\)"\s]+)\s*([^\)]*)\))', markdown)

    for image in image_tags:
        image_markdown = image[0]
        image_alt = image[1]
        image_path = image[2]
        if image_path in images:
            markdown = markdown.replace(image_markdown, img_to_html(images[image_path], image_alt))
    return markdown

# Load models if not already loaded in reload mode
if 'model_dict' not in globals():
    model_dict = load_models()

with gr.Blocks(title="Marker") as demo:
    gr.Markdown("""
    # Marker Demo

    This app will let you try marker, a PDF -> Markdown converter. It works with any languages, and extracts images, tables, equations, etc.

    Find the project [here](https://github.com/VikParuchuri/marker).
    """)

    with gr.Row():
        with gr.Column():
            in_file = gr.File(label="PDF file:", file_types=[".pdf"])
            in_num = gr.Slider(label="PDF file page number", minimum=1, maximum=1, value=1, step=1, visible=False)
            in_img = gr.Image(label="PDF file (preview)", type="pil", sources=None, visible=False)

            page_range_txt = gr.Textbox(label="Page range to parse, comma separated like 0,5-10,20", value=f"0-0")
            output_format_dd = gr.Dropdown(label="Output format", choices=["markdown", "json", "html"], value="markdown")

            force_ocr_ckb = gr.Checkbox(label="Force OCR", value=True, info="Force OCR on all pages")
            debug_ckb = gr.Checkbox(label="Debug", value=False, info="Show debug information")
            trun_marker_btn = gr.Button("Run Marker", interactive=False)
        with gr.Column():
            result_md = gr.Markdown(label="Result markdown", visible=False)
            result_json = gr.JSON(label="Result json", visible=False)
            result_html = gr.Markdown(label="Result html", visible=False)
            debug_img_pdf = gr.Image(label="PDF debug image", visible=False)
            debug_img_layout = gr.Image(label="Layout debug image", visible=False)

        def show_image(file, num=1):
            if file is None:
                return [
                    gr.update(visible=False, maximum=1, value=num),
                    gr.update(visible=False),
                    "0-0"]
            count = count_pdf(file)
            img = get_page_image(file, num)
            return [
                gr.update(visible=True, maximum=count),
                gr.update(visible=True, value=img),
                f"0-{num-1}"]

        in_file.clear(
            fn=show_image,
            inputs=[in_file],
            outputs=[in_num, in_img, page_range_txt]
        )
        in_file.upload(
            fn=show_image,
            inputs=[in_file],
            outputs=[in_num, in_img, page_range_txt]
        )
        in_num.change(
            fn=show_image,
            inputs=[in_file, in_num],
            outputs=[in_num, in_img, page_range_txt]
        )

        def check_page_range(page_range, file):
            count = count_pdf(file) if file is not None else 1
            if not re.match(r"^(\d+(-\d+)?)?$", page_range):
                gr.Warning(f"Invalid format. Please use 0-{count-1}", duration=0)
                return [
                    gr.update(info=f"format 0-{count-1}"),
                    gr.update(interactive=False)]
            else:
                return [
                    gr.update(info=f"format 0-{count-1}"),
                    gr.update(interactive=True)]
        page_range_txt.change(
            fn=check_page_range,
            inputs=[page_range_txt, in_file],
            outputs=[page_range_txt, trun_marker_btn]
        )

        # Run Marker
        def run_marker_img(filename, page_range, force_ocr, output_format, debug):
            cli_options = {
                "output_format": output_format,
                "page_range": page_range,
                "force_ocr": force_ocr,
                "debug": debug,
                "output_dir": settings.DEBUG_DATA_FOLDER if debug else None,
            }
            config_parser = ConfigParser(cli_options)
            rendered = convert_pdf(
                filename,
                config_parser
            )
            gr_debug_pdf = gr.update(visible=False)
            gr_debug_lay = gr.update(visible=False)
            if debug:
                debug_data_path = rendered.metadata.get("debug_data_path")
                if debug_data_path:
                    page_range = config_parser.generate_config_dict()["page_range"]
                    first_page = page_range[0] if page_range else 0

                    pdf_image_path = os.path.join(debug_data_path, f"pdf_page_{first_page}.png")
                    img = Image.open(pdf_image_path)
                    gr_debug_pdf = gr.update(visible=True, value=img)
                    layout_image_path = os.path.join(debug_data_path, f"layout_page_{first_page}.png")
                    img = Image.open(layout_image_path)
                    gr_debug_lay = gr.update(visible=True, value=img)

            text, ext, images = text_from_rendered(rendered)
            if output_format == "markdown":
                text = markdown_insert_images(text, images)
                return [
                    gr.update(visible=True, value=text),
                    gr.update(visible=False),
                    gr.update(visible=False),
                    gr_debug_pdf,
                    gr_debug_lay
                ]
            elif output_format == "json":
                return [
                    gr.update(visible=False),
                    gr.update(visible=True, value=text),
                    gr.update(visible=False),
                    gr_debug_pdf,
                    gr_debug_lay
                ]
            elif output_format == "html":
                return [
                    gr.update(visible=False),
                    gr.update(visible=False),
                    gr.update(visible=True, value=text),
                    gr_debug_pdf,
                    gr_debug_lay
                ]

        trun_marker_btn.click(
            fn=run_marker_img,
            inputs=[in_file, page_range_txt, force_ocr_ckb, output_format_dd, debug_ckb],
            outputs=[result_md, result_json, result_html, debug_img_pdf, debug_img_layout]
        )

if __name__ == "__main__":
    demo.launch()
