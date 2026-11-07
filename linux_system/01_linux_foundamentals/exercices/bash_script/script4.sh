#!/bin/bash

set -e

ENVIRONMENT="$1"
service="nginx"
log_file="deployment.log"

# To reset log before script execution
: > "$log_file"


# Reject if no environment is provide
if [ -z "$ENVIRONMENT" ]; then
   echo "Error: ENVIRONMENT is required" >> "$log_file"
   exit 1
fi

# Reject unsupported environments
if [[ "$ENVIRONMENT" == "staging" || "$ENVIRONMENT" == "production" ]]; then
   echo "Continue to deploy on $ENVIRONMENT ENVIRONMENT" >> "$log_file"
else
   echo "Error Environment must be staging or production." >> "$log_file"
   exit 1
fi


if systemctl is-active --quiet "$service" ; then
   echo "ENVIRONMENT: $ENVIRONMENT | Service: $service is running" >> "$log_file"
else
   echo "ENVIRONMENT: $ENVIRONMENT | Service: $service is not running." >> "$log_file" 
   exit 1
fi


