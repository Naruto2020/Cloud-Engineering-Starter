# ============================================================
# Exercise 10 — First Function
# ============================================================
#
# Write a function called `check_cpu` that takes a `cpu`
# value as a parameter.
#
# The function must display:
#
#     CPU usage is normal
#
# when the CPU usage is less than or equal to 80.
#
# The function must display:
#
#     WARNING: High CPU usage
#
# when the CPU usage is greater than 80.
#
# ============================================================


CPU_LIMIT = 80

def check_cpu(cpu: int):
    if cpu > CPU_LIMIT:
        return f"WARNING: High CPU usage {cpu}%"
    else:
        return f"CPU usage is normal {cpu}%"

result_1 = check_cpu(45)
result_2 = check_cpu(85)

print(result_1)
print(result_2)


# ============================================================
# Exercise — Using the Function
# ============================================================
#
# Loop through the `servers` list and use the `check_cpu()`
# function for each server.
#
# The output should follow this format:
#
#     web-01 -> CPU usage is normal 45%
#     web-02 -> CPU usage is normal 0%
#     db-01 -> WARNING: High CPU usage 87%
#     api-01 -> WARNING: High CPU usage 92%
#     cache-01 -> WARNING: High CPU usage 95%
#
# ============================================================



servers = [
    {"name": "web-01", "status": "running", "cpu": 45},
    {"name": "web-02", "status": "stopped", "cpu": 0},
    {"name": "db-01", "status": "running", "cpu": 87},
    {"name": "api-01", "status": "stopped", "cpu": 92},
    {"name": "cache-01", "status": "running", "cpu": 95}
]


for server in servers:
   result = check_cpu(server['cpu'])
   print(f"{server['name']} -> {result}")


# ============================================================
# Exercise 13 — Analyze a Server
# ============================================================
#
# Write a function that analyzes a complete server.
#
# The function receives a dictionary containing:
#
#     server = {
#         "name": "db-01",
#         "status": "running",
#         "cpu": 87
#     }
#
# The function must analyze the server and return an appropriate
# message based on its CPU usage.
#
# For a server with high CPU usage, the expected result is:
#
#     db-01 -> WARNING: High CPU usage
#
# ============================================================

server_1 = {
    "name": "db-01",
    "status": "running",
    "cpu": 87
}

server_2 = {
    "name": "web-01",
    "status": "running",
    "cpu": 45
}

def check_server(srv):
    if srv['cpu'] > CPU_LIMIT:
        return f"{srv['name']} -> WARNING: High CPU usage"
    else:
        return f"{srv['name']} -> CPU usage is normal"

result_1 = check_server(server_1)
result_2 = check_server(server_2)
print(result_1)
print(result_2)
