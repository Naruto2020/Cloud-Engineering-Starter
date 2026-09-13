
CPU_LIMIT = 80

def check_cpu(cpu: int, limit: int = CPU_LIMIT) -> str:
    return(
        "WARNING"
        if cpu > limit
        else "NORMAL"
    )


def check_memory(percentage: float, limit: int = 80) -> str:
    return (
        "WARING"
        if percentage > limit
        else "NORMAL"
    )


def check_disk(percentage: float, limit: int = 80) -> str:
    return (
        "WARNING"
        if percentage > limit
        else "NORMAL"
    )



