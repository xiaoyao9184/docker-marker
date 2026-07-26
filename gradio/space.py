import sys

from pip_override import install_pip_override

install_pip_override()

# run gradio in subprocess in reloaded mode
# huggingface space issue: https://github.com/gradio-app/gradio/issues/10048
# need disable reload for huggingface space
import re
import sys
from gradio.cli import cli
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv.append(re.sub(r'space\.py$', 'gradio_app.py', sys.argv[0]))
    sys.exit(cli())
