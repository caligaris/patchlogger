# Patchlogger for Ubuntu Linux

A basic python script that executes `apt-get -s dist-upgrade | grep "^Inst"` and logs the pending packages for upgrade, the purpose is to use the generated log as a source for an Azure Log Analytics Workspace custom log table. All files will be deployed into /opt/patchlogger.

Sample log entry:

```2020-11-03 01:31:30,616 Name=openssh-server Architecture=amd64 Version=1:7.2p2-4ubuntu2.10 Repository=Ubuntu:16.04/xenial-updates```

## Architecture
* A new user **patchlogger** is created.
* A new file is created in `/etc/sudoers.d/` directory to grant sudo to **patchlogger** user to `/opt/patchlogger/APTUpdates.sh` script.
* All files are copied into `/opt/patchlogger/` directory.
* A file is placed into `/etc/cron.d/patchlogger`. 
    - It runs the patchInventory.py script every 12 hrs.
    - It adds a logrotate job to check every 12 hrs.

## Log Analytics Workspace
To setup the custom log as a data source for a log analytics workspace refer to the [official](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/data-sources-custom-logs) docs 
