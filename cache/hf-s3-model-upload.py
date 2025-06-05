#!/usr/bin/env python3

import os

from surya.settings import settings
from huggingface_hub import HfApi
api = HfApi()

map_remote_path_env_name = {
    settings.DETECTOR_MODEL_CHECKPOINT: "DETECTOR_MODEL_REPO_ID",
    settings.RECOGNITION_MODEL_CHECKPOINT: "RECOGNITION_MODEL_REPO_ID",
    settings.LAYOUT_MODEL_CHECKPOINT: "LAYOUT_MODEL_REPO_ID",
    settings.TABLE_REC_MODEL_CHECKPOINT: "TABLE_REC_MODEL_REPO_ID",
    settings.OCR_ERROR_MODEL_CHECKPOINT: "OCR_ERROR_MODEL_REPO_ID",
}

for remote_path, env_name in map_remote_path_env_name.items():
    pretrained_model_name_or_path = remote_path.replace("s3://", "")
    local_path = os.path.join(os.getcwd(), "datalab", "models", pretrained_model_name_or_path)

    if not os.path.exists(local_path):
        continue

    if os.getenv(env_name) is None:
        continue

    repo_id = os.getenv(env_name)
    tag_name = pretrained_model_name_or_path.split("/")[1]
    repo_type = "model"
    branch = "main"

    print(f"Uploading {pretrained_model_name_or_path}")
    api.upload_large_folder(
        repo_id=repo_id,
        folder_path=local_path,
        repo_type=repo_type,
        revision=branch,
        ignore_patterns="**/manifest.json"
    )

    refs = api.list_repo_refs(repo_id=repo_id, repo_type=repo_type)
    tag_names = [tag.name for tag in refs.tags]
    if tag_name not in tag_names:
        commits = api.list_repo_commits(repo_id=repo_id, repo_type=repo_type, revision=branch)
        latest_commit = commits[0].commit_id
        api.create_tag(
            repo_id=repo_id,
            tag=tag_name,
            revision=latest_commit,
            repo_type=repo_type
        )
