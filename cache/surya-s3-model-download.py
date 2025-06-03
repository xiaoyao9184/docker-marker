#!/usr/bin/env python3

import os
from surya.common.s3 import download_directory
from surya.settings import settings

for remote_path in [
    settings.DETECTOR_MODEL_CHECKPOINT,
    settings.INLINE_MATH_MODEL_CHECKPOINT,
    settings.RECOGNITION_MODEL_CHECKPOINT,
    settings.LAYOUT_MODEL_CHECKPOINT,
    settings.TABLE_REC_MODEL_CHECKPOINT,
    settings.TEXIFY_MODEL_CHECKPOINT,
    settings.OCR_ERROR_MODEL_CHECKPOINT
]:
    pretrained_model_name_or_path = remote_path.replace("s3://", "")
    local_path = os.path.join(os.getcwd(), "datalab", "models", pretrained_model_name_or_path)
    os.makedirs(local_path, exist_ok=True)
    download_directory(pretrained_model_name_or_path, local_path)
    print(f"Downloaded {pretrained_model_name_or_path}")
