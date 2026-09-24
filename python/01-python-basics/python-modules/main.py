
from monitoring import check_cpu, check_memory, check_disk, check_server
from monitoring import CPU_LIMIT
#import server.conf
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

config = {}

with open("python/01-python-basics/python-modules/server.conf", "r") as file:
    for line in file:
        destructure_line = line.strip().split("=")
        config[destructure_line [0]] = destructure_line [1]
        #print(f"current prop: {line.strip()}")
        print(f"current prop2: {destructure_line}")


print(config)
