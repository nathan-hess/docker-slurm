## SETTINGS ------------------------------------------------------------------
ARG USER_PRIVILEGE_LEVEL=standard

# Settings for all images
ARG TIMEZONE="UTC"
ARG UBUNTU_VERSION=22.04

# Settings for standard user images
ARG USERNAME
ARG PASSWORD
ARG UID=1000
ARG GID=1000


## BUILD IMAGE: ROOT USER ----------------------------------------------------
FROM ubuntu:${UBUNTU_VERSION} as stage-root
ARG TIMEZONE

# Run system updates
RUN apt update && apt -y upgrade

# Set time zone
RUN ln -sn /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
    && echo ${TIMEZONE} > /etc/timezone \
    && apt -y install tzdata

# Install system packages
RUN DEBIAN_FRONTEND=noninteractive \
    apt -y install munge \
                   slurm-wlm

# Slurm configuration
COPY slurm.conf /etc/slurm/slurm.conf
RUN mkdir -p /var/spool/slurmctld \
    && chown slurm:slurm /var/spool/slurmctld

# Startup configuration
COPY startup.sh /etc/startup.sh

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


# SELECT DESIRED USER PRIVILEGE LEVEL ----------------------------------------
FROM stage-${USER_PRIVILEGE_LEVEL}

# Set default command when running container
CMD /etc/startup.sh ; /bin/bash
