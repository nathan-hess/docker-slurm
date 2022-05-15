## SETTINGS ------------------------------------------------------------------
ARG USER_PRIVILEGE_LEVEL=standard

# Settings for all images
ARG BASE_DOCKER_REPO
ARG TIMEZONE="UTC"

# Settings for standard user images
ARG USERNAME
ARG PASSWORD
ARG UID=1000
ARG GID=1000


## BUILD IMAGE: ROOT USER ----------------------------------------------------
FROM ${BASE_DOCKER_REPO}:base-root as stage-root

# Run system updates
RUN apt update && apt -y upgrade

# Install system packages
RUN DEBIAN_FRONTEND=noninteractive \
    apt -y install build-essential \
                   curl \
                   dos2unix \
                   gdb \
                   git \
                   graphviz \
                   htop \
                   lshw \
                   nano \
                   munge \
                   net-tools \
                   openssl \
                   python3-pip \
                   python3-tk \
                   python3-venv \
                   slurm-wlm \
                   slurm-wlm-doc \
                   slurm-wlm-basic-plugins \
                   slurm-wlm-basic-plugins-dev \
                   tree \
                   vim \
                   wget \
                   zip

# Set working directory
WORKDIR /root


## BUILD IMAGE: STANDARD USER ------------------------------------------------
FROM stage-root as stage-standard
ARG USERNAME
ARG PASSWORD
ARG UID
ARG GID

# Create user account and add to "sudo" group
RUN apt -y install sudo openssl
RUN useradd --create-home --uid=${UID} ${USERNAME} -p "$(openssl passwd -1 ${PASSWORD})" \
    && usermod -a -G sudo ${USERNAME}

# Set standard user as default
USER ${UID}:${GID}

# Set working directory
WORKDIR /home/${USERNAME}

# Enable colored Bash terminal prompt
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/' /home/${USERNAME}/.bashrc

# Add Python package executables to PATH
ENV PATH="${PATH}:/home/${USERNAME}/.local/bin"


# SELECT DESIRED USER PRIVILEGE LEVEL ----------------------------------------
FROM stage-${USER_PRIVILEGE_LEVEL}

# Set default command when running container
CMD /etc/startup.sh ; /bin/bash -l
