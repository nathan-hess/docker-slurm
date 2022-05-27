# Slurm in Docker

### Docker images with Slurm Workload Manager installed

This repository contains setup files for Ubuntu-based Docker images and containers with the [Slurm Workload Manager](https://slurm.schedmd.com/) installed.  These images are primarily designed to serve as an environment to experiment with Slurm or run unit/integration tests of code that will later be run on high-performance computing (HPC) resources.


## Image Descriptions and Tags

This repository contains files which can be used to configure Docker images with Slurm installed.  Two image versions are provided:
- A "base" version with Slurm installed and a minimal set of required packages
- A "full" version with everything in the base version, plus various system tools (Python, text editors, Git, GCC, etc.) meant to reflect the basic setup of typical HPC servers

Both image versions are configured such that the default user is either `root` (if the tag has "root" in the name) or a standard user with sudo privileges.

### Docker Hub repository: https://hub.docker.com/r/nathanhess/slurm

| Tag       | Base Image                                | Build Context      | Default User |  
|:----------|:------------------------------------------|:-------------------|:-------------|
| base      | [Ubuntu](https://hub.docker.com/_/ubuntu) | `dockerfile_base/` | standard     |
| base-root | [Ubuntu](https://hub.docker.com/_/ubuntu) | `dockerfile_base/` | root         |
| full      | [Ubuntu](https://hub.docker.com/_/ubuntu) | `dockerfile_full/` | standard     |
| full-root | [Ubuntu](https://hub.docker.com/_/ubuntu) | `dockerfile_full/` | root         |

> **Note**: For the images with a standard user, the default username is `docker` and the default password is `ubuntu`.

### GitHub repository: https://github.com/nathan-hess/docker-slurm

Dockerfiles and other configuration files for these images are stored in GitHub.  The images are automatically built and published to [Docker Hub](https://hub.docker.com/) with a GitHub Actions workflow.  The workflow runs twice a month, in addition to any time a change is made to the `Dockerfile` for either image, the workflow file itself, or configuration files (`.env`).


## References

- [Slurm](https://slurm.schedmd.com/)
  - [Official Project Documentation](https://slurm.schedmd.com/)
  - [SUSE Slurm Setup Guide](https://documentation.suse.com/sle-hpc/15-SP3/html/hpc-guide/cha-slurm.html)
- [Docker](https://www.docker.com/)
  - [Getting Started Overview](https://docs.docker.com/get-started/overview/)
  - [Command-Line Reference](https://docs.docker.com/engine/reference/commandline/docker/)
  - [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
  - [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Visual Studio Code](https://code.visualstudio.com/)
  - [Docker Extension](https://code.visualstudio.com/docs/containers/overview)
  - [Developing Inside a Container](https://code.visualstudio.com/docs/remote/containers)
  - [Attach to a Container](https://code.visualstudio.com/docs/remote/attach-container)
