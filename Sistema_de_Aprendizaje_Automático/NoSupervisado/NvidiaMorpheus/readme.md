## Docker Installation for Morpheus

### Requirements
- Volta architecture GPU or better
- CUDA 12.5
- Docker
- The NVIDIA Container Toolkit
- NVIDIA Triton Inference Server 24.09 or higher

---

## Using Pre-Built Docker Containers

### Pull the Morpheus Image
1. Visit: [NGC Morpheus Containers](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/morpheus/containers/morpheus/tags)
2. Choose a version.
3. Download the selected version, e.g., for 25.02:

```sh
docker pull nvcr.io/nvidia/morpheus/morpheus:25.02-runtime
```

#### Optional: Download Triton Server Models
If required, download the Morpheus Triton Server Models container, ensuring the version number matches the Morpheus container:

```sh
docker pull nvcr.io/nvidia/morpheus/morpheus-tritonserver-models:25.02
```

### Morpheus Versioning
- **YY.MM-runtime**: Latest point release for that version.
- **vYY.MM.00-runtime**: Initial point release for that version.
- **Bug fixes**: Additional point releases (e.g., v25.02.01-runtime, v25.02.02-runtime, etc.)
- **Recommendation**:
  - Use `YY.MM-runtime` for latest bug fixes.
  - Use `vYY.MM.00-runtime` for production deployments.

---

## Starting the Morpheus Container
Ensure **The NVIDIA Container Toolkit** is installed.

Start the container:

```sh
docker run --rm -ti --runtime=nvidia --gpus=all --net=host -v /var/run/docker.sock:/var/run/docker.sock nvcr.io/nvidia/morpheus/morpheus:25.02-runtime bash
```

### Explanation of Flags
| Flag | Description |
|------|------------|
| `--runtime=nvidia` | Choose the NVIDIA Docker runtime (required for GPU access). Omit if NVIDIA runtime is default. |
| `--gpus=all` | Grant access to all GPUs. Use `--gpus=<gpu-id>` to specify a GPU. |
| `--net=host` | Grants the container access to the host system’s network (useful for NVIDIA Triton Inference Server). |
| `-v /var/run/docker.sock:/var/run/docker.sock` | Enables launching other Docker containers from within the Morpheus container. Required for launching Triton with Morpheus models. |

### Install Docker Tools in the Container
To launch Triton with the included Morpheus models, install Docker tools inside the Morpheus container:

```sh
./external/utilities/docker/install_docker.sh
```

Proceed to acquiring the Morpheus Models Container.

## Reference
https://docs.nvidia.com/morpheus/getting_started.html#starting-the-morpheus-container
