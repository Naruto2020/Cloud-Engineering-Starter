 #!/bin/bash


services="nginx ssh cron"
action="$1"
for service in $services
do
    systemctl is-active "$service" > /dev/null&& echo "$service: ok" || echo "$service: FAILED"
done



counter=1

while [ "$counter" -le 3 ]
do
    echo "Checking server #$counter"
    counter=$((counter + 1))
done


case "$action" in
    start)
        echo "Starting service"
        ;;
    stop)
        echo "Stopping service"
        ;;
    status)
        echo "Checking service status"
        ;;
    *)
        echo "Unknown action"
        ;;
esac

