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
    {"name": "api-01", "status": "stopped", "cpu": 92}
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