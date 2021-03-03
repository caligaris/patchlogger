#!/bin/bash

# How to add as custom extension to existing vm, need to do az login prior to run the following command
# Update fileUris with appropiate release tag 
group=''
vmName=''

az vm extension set \
  --resource-group $group \
  --vm-name $vmName \
  --name customScript \
  --publisher Microsoft.Azure.Extensions \
  --protected-settings '{"fileUris": ["https://github.com/caligaris/patchlogger/releases/download/v0.0.1-alpha.3/patchlogger.tar.gz"],"commandToExecute": "sudo tar zxvf patchlogger.tar.gz && sh ./patchloggerSetup.sh"}'