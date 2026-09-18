
from monitoring import check_cpu, check_memory, check_disk, check_server
from monitoring import CPU_LIMIT
#import monitoring

# result = monitoring.check_cpu(90)

cpu_status = check_cpu(90)
memory_status = check_memory(75)
disk_status = check_disk(85)

print(f"CPU: {cpu_status}")
print(f"Memory: {memory_status}")
print(f"Disk: {disk_status}")

server = {
    "name": "web-01",
    "cpu": 90,
    "memory": 65,
    "disk": 85
}

result = check_server(server)

print(result)
print(f"CPU limit: {CPU_LIMIT}%")
