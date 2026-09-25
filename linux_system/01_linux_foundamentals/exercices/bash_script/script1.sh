#!/bin/bash

server_name=$(hostname)
environment="production"
status=$(systemctl is-active nginx)
echo $? "test"

if [ "$status" = "active" ]; then
    echo "Server: $server_name"
    echo "Environment: $environment"
    echo "Nginx is running"
elif [ "$status" = "inactive" ]; then
    echo "Server: $server_name"
    echo "Environment: $environment"
    echo "Warning: Nginx is not running"
else
    echo "ERROR: Nginx has failed"
fi


