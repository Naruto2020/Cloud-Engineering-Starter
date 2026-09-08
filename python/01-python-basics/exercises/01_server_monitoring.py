# ============================================================
# Exercise 01 - Server Monitoring
# ============================================================
#
# Create a Python program that displays information about a
# list of servers.
#
# Each server contains:
# - a name
# - a status
# - a CPU usage percentage
#
# Requirements:
# 1. Store the server information in a list of dictionaries.
# 2. Define a CPU limit of 80%.
# 3. Loop through all servers.
# 4. Display each server's name, status and CPU usage.
# 5. Display a warning when CPU usage is above the limit.
# 6. Use f-strings to format the output.
# 7. Use a ternary expression for the CPU warning.
#
# ============================================================
# Solution
# ============================================================

servers = [
    {"name": "web-01", "status": "running", "cpu": 45},
    {"name": "web-02", "status": "stopped", "cpu": 0},
    {"name": "db-01", "status": "running", "cpu": 87},
    {"name": "api-01", "status": "stopped", "cpu": 92},
    {"name": "cache-01", "status": "running", "cpu": 95}
]

CPU_LIMIT = 80

# Display each server
for server in servers:
    status_text = (
        f"-> WARNING: High CPU usage"
        if server["cpu"] > CPU_LIMIT
        else ""
    )

    print(
        f"{server['name']} -> "
        f"Server is {server['status']} -> "
        f"CPU: {server['cpu']}% {status_text}"
    )

# ============================================================
# Exercise — Server Attention Check
# ============================================================
#
# For each server, determine whether it requires special attention.
#
# A server requires attention if one of the following conditions
# is met:
#
# Condition 1:
# The server is running AND its CPU usage is above 80%.
#
# Condition 2:
# The server is stopped AND its CPU usage is different from 0.
#
#
# Display an appropriate message for each server.
#
# db-01 -> WARNING: High CPU usage
# cache-01 -> WARNING: High CPU usage
# api-01 -> WARNING: Server is stopped but CPU is not 0
#
# ============================================================

for server in servers:
    if server['status'] == "running" and server['cpu'] > CPU_LIMIT:
        status_run = f"-> WARNING: high CPU usage"
        print(f"{server['name']} -> {status_run}")
    elif server['status'] == "stopped" and not server['cpu'] == 0:
        status_stop = f"-> WARNING: Server is stopped but CPU is not 0"
        print(f"{server['name']} -> {status_stop}")