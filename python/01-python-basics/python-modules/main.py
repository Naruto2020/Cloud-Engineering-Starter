
from monitoring import check_cpu, check_memory, check_disk
#import monitoring

# result = monitoring.check_cpu(90)

cpu_status = check_cpu(90)
memory_status = check_memory(75)
disk_status = check_disk(85)

print(f"CPU: {cpu_status}")
print(f"Memory: {memory_status}")
print(f"Disk: {disk_status}")


