# Docker Marker

A Docker image built through Github Actions with Git commit version tag

[![Docker Image Build/Publish tag with commit](https://github.com/xiaoyao9184/docker-marker/actions/workflows/docker-image-tag-commit.yml/badge.svg)](https://github.com/xiaoyao9184/docker-marker/actions/workflows/docker-image-tag-commit.yml) [![](https://img.shields.io/docker/v/xiaoyao9184/marker)](https://hub.docker.com/r/xiaoyao9184/marker)

[![Docker Image Build/Publish tag with version](https://github.com/xiaoyao9184/docker-marker/actions/workflows/docker-image-tag-version.yml/badge.svg)](https://github.com/xiaoyao9184/docker-marker/actions/workflows/docker-image-tag-version.yml) [![](https://img.shields.io/docker/v/xiaoyao9184/marker/2.0.0)](https://hub.docker.com/r/xiaoyao9184/marker)

[![HuggingFace Model Sync](https://github.com/xiaoyao9184/docker-marker/actions/workflows/hf-model-sync.yml/badge.svg)](https://github.com/xiaoyao9184/docker-marker/actions/workflows/hf-model-sync.yml) [![](https://img.shields.io/badge/HuggingFace-model-8b2cff?logo=huggingface)](https://huggingface.co/collections/xiaoyao9184/surya-and-marker-68635abc74f33ef5d5be792d)

[![HuggingFace Space Sync](https://github.com/xiaoyao9184/docker-marker/actions/workflows/hf-space-sync.yml/badge.svg)](https://github.com/xiaoyao9184/docker-marker/actions/workflows/hf-space-sync.yml) [![](https://img.shields.io/badge/HuggingFace-space-ff9f44?logo=huggingface)](https://huggingface.co/spaces/xiaoyao9184/marker) ![](https://badge.mcpx.dev?type=server 'MCP Server')

# Why

I found that Marker's Docker image is difficult to find.
The code on [GitHub](https://github.com/VikParuchuri/marker) does not provide a pre-built Docker image.

After reviewing the following items

- [linux.do](https://linux.do/t/topic/239082)

This project will use GitHub Actions and Docker Hub to build and publish images,
aiming to keep the process as clean as possible without custom configuration files.

# Tags

The images of this project will be published to Docker Hub under the repository [xiaoyao9184/marker](https://hub.docker.com/r/xiaoyao9184/marker).

The default image name format is `${DOCKERHUB_USERNAME}/marker`.

Currently, only the `linux/amd64` platform is supported.

Since this project references the Marker project via a submodule, it cannot monitor push events on the Marker project, and therefore cannot automatically create an image for every upstream Marker commit.

When the submodule pointer or Docker build files are updated and pushed to this project, the [docker-image-tag-commit](./.github/workflows/docker-image-tag-commit.yml) job builds an image for the current project commit.
The commit-based image tag is the short commit id of this project repository,
generated from the GitHub Actions checkout with `git rev-parse --short HEAD`.
For example, a project commit `0123456789abcdef` will publish `${DOCKERHUB_USERNAME}/marker:0123456`.

**NOTE**:
> Starting from Marker `2.0.0`, commit-based image tags use the short commit id of this project repository.
> Before Marker `2.0.0`, commit-based image tags used the short commit id of the upstream Marker project repository.

If the job [docker-image-tag-version](./.github/workflows/docker-image-tag-version.yml) is triggered, the Marker package published on PyPI will be installed for the build.
The Docker image tag is read from the Git tag on the current `marker` submodule commit,
with the leading `v` prefix removed.
For example, a Marker Git tag `v0.20.0` will publish `${DOCKERHUB_USERNAME}/marker:0.20.0`.
If no Git tag is found on the current `marker` submodule commit, the build will fail.

# Model

The models of this project will be synced to HuggingFace under the collection [xiaoyao9184/surya-and-marker](https://huggingface.co/collections/xiaoyao9184/surya-and-marker-68635abc74f33ef5d5be792d).

The Docker image does not include model files.
When running, the required models will be automatically downloaded.

If you need to run offline, you must pre-download the model files and enable offline mode.
See [cache/README.md](./cache/README.md) for detailed instructions.

# Service

By default, the Docker container runs the Streamlit App, which comes from the original project.

However, this project also provides a Gradio App, a functional reimplementation of the Streamlit version.
The Gradio App supports both a UI and API interface, and can even serve as an MCP server,
so it is recommended as the preferred option.

The source code for the Gradio App is located in the [gradio](./gradio) directory of this project.
A demo of this project is also available and auto-synced on Hugging Face Spaces: [xiaoyao9184/marker](https://huggingface.co/spaces/xiaoyao9184/marker)

To run the Gradio App, you can do so by modifying the Docker command. see the `up.gradio` sub-directory in the [docker](./docker) directory for details.

# Change

You can fork this project and build your own image. You will need to provide the following variables: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `HF_USERNAME`, `HF_TOKEN`.
See [this](https://github.com/docker/login-action#docker-hub) for more details.
