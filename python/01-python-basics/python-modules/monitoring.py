
CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISC_LIMIT = 80


def check_cpu(cpu: int, limit: int = CPU_LIMIT) -> str:
    return(
        "WARNING"
        if cpu > limit
        else "NORMAL"
    )


def check_memory(percentage: float, limit: int = MEMORY_LIMIT) -> str:
    return (
        "WARING"
        if percentage > limit
        else "NORMAL"
    )


def check_disk(percentage: float, limit: int = DISC_LIMIT) -> str:
    return (
        "WARNING"
        if percentage > limit
        else "NORMAL"
    )


def check_server(server: dict) -> str:
    cpu_status = check_cpu(server["cpu"])
    memory_status = check_memory(server["memory"])
    disk_status = check_disk(server["disk"])

    return (
        f"{server['name']} -> "
        f"CPU: {cpu_status}, "
        f"Memory: {memory_status}, "
        f"Disk: {disk_status} "
)



if __name__ == "__main__":
    print("Monitoring module executed directly")


