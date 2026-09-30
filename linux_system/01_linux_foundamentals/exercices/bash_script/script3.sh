#!/bin/bash


services="nginx ssh cron"

for service in $services
do
    systemctl is-active "$service" > /dev/null&& echo "$service: ok" || echo "$service: FAILED"
done
