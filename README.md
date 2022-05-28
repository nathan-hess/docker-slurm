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


---

## Introduction to Docker

Docker is a platform designed for setting up and running containers.  On a high level, containers bundle software, files, and system configuration options into a single, distributable environment.

From Docker's [official documentation](https://docs.docker.com/get-started/overview/):
> Docker provides the ability to package and run an application in a loosely isolated environment called a container. [...] Containers are lightweight and contain everything needed to run the application, so you do not need to rely on what is currently installed on the host. You can easily share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

Containers in many ways function similar to a virtual machine: you can install required dependencies, set configuration options, and define environment variables inside a container, and then share the container to any other system to reproduce a nearly identical environment.  However, it is important to note that containers and virtual machines are NOT equivalent, and each has their own capabilities and limitations.

Some of the advantages of containers include:

- **Bundled dependencies**: Setting up a development environment or dependencies required to run an application often involves many manual steps.  These steps can become time-consuming and tedious if performed manually on a per-system basis.  However, if instead all dependencies are installed in a container, then the container can simply be transferred to different systems, and all dependencies and configuration will be transferred with it.  This makes it extremely easy to set up and run your code on different systems.
- **Reproducibility**: Using containers allows you to run your code with identical dependency versions and system configuration, so the same code should behave identically on different machines.
- **Ability to install software without administrator privileges**: In many cases, you may not have administrator privileges on computing systems such as HPC clusters, but you may need certain dependencies that require administrator privileges to install.  Many HPC clusters offer container software that provides a workaround: simply install your software in a container, and then you can transfer the container to the HPC cluster and run all required dependencies without administrator privileges.

For a list of useful Docker commands, refer to the [Docker Command-Line Reference](https://docs.docker.com/engine/reference/commandline/docker/).


## Project History, Features, and Limitations

This project began in March 2022 to solve a challenge in a code development project seeking to develop Python scripts to interact with Slurm.  While developing the code, it was necessary to repeatedly run Slurm commands for testing, but access to HPC systems often incurs financial costs and requires waiting in queues, slowing down the development process.  How could code invoking Slurm commands be tested rapidly and at no financial cost?

The answer was to use Docker containers.  This provides several benefits:
- As discussed in the [Introduction to Docker](#introduction-to-docker) section, Docker containers are lightweight, reproducible, and easily set up and removed -- conducive to code testing.
- Visual Studio Code has built-in mechanisms to set up Docker-based [development containers](https://code.visualstudio.com/docs/remote/containers), facilitating rapid code development, without the need to test code on HPC systems.
- GitHub Actions allows workflows to be [run in custom Docker containers](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container), facilitating automated code testing.

That said, as with any project, there are important limitations to be aware of:
- These images have a relatively basic Slurm setup.  They do not use Slurm configuration features such as cgroups or a job accounting database.
- These images define a single-node setup.  However, they could be relatively easily extended to a multi-node cluster through Docker Compose or Kubernetes.

If extending the existing Docker image configurations to overcome any of the above limitations would benefit your work, please [submit an issue](https://github.com/nathan-hess/docker-slurm/issues/new?labels=enhancement&template=feature_request.md).


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
- [GitHub Actions](https://docs.github.com/en/actions)
  - [Running jobs in a container](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container)
