#!/bin/bash

# Add patchlogger user and group
sudo useradd -r patchlogger -b /opt -s /bin/bash

# Add logger directory
sudo mkdir /opt/patchlogger
sudo chown patchlogger:root /opt/patchlogger
sudo cp -R ./source/. /opt/patchlogger/
sudo chown -R patchlogger:patchlogger /opt/patchlogger/*

# Add to sudoers
sudo cp ./source/patchlogger /etc/sudoers.d/

# Add cron job for patchlogger user
sudo bash -c "echo '0 */12 * * * patchlogger python /opt/patchlogger/patchInventory.py > /dev/null 2>&1' > /etc/cron.d/patchlogger"

# Logrotate setup
sudo bash -c "echo '0 */12 * * * patchlogger /usr/sbin/logrotate -s /opt/patchlogger/patchlogger-status /opt/patchlogger/patchlogrotate.conf > /dev/null 2>&1' >> /etc/cron.d/patchlogger"

# Do an initial run
sudo -u patchlogger bash -c 'python /opt/patchlogger/patchInventory.py'


