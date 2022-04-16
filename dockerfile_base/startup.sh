#!/bin/bash

# Determine whether script is running as root
sudo_cmd=""
if [ "$(id -u)" != "0" ]; then
    sudo_cmd="sudo"
    sudo -k
fi

# Configure Slurm to use maximum available processors and memory
# and start required services
${sudo_cmd} bash <<SCRIPT
sed -i "s/<<CPU>>/$(nproc)/" /etc/slurm-llnl/slurm.conf
sed -i "s/<<MEMORY>>/$(awk '/MemTotal/ { printf "%.0f \n", $2/1024 }' /proc/meminfo)/" /etc/slurm-llnl/slurm.conf
service munge start
service slurmd start
service slurmctld start
SCRIPT

# Revoke sudo permissions
if [[ ${sudo_cmd} ]]; then
    sudo -k
fi
