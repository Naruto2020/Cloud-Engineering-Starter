#!/bin/bash

server_name=$(hostname)
environment="production"
status=$(systemctl is-active nginx)
exit_code=$?


echo "$exit_code"

if [ "$exit_code" -eq 0 ]; then
    echo "Server: $server_name"
    echo "Environment: $environment"
    echo "Status: $status -> nginx is running"
else
    echo "Server: $server_name"
    echo "Environment: $environment"
    echo "Status $status -> nginx is not running"
fi

echo "=================== && and || ==============================="

systemctl is-active nginx && echo "Nginx is running"
systemctl is-active nginx || echo "Nginx is not running"

echo "=================== one line health check =================== "

systemctl is-active nginx &&
    echo "Server: $server_name Environment: $environment Nginx is running" ||
    echo "Server: $server_name Environment: $environment Nginx is not running"
