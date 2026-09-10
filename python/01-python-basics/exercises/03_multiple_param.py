# ============================================================
# Stage 5.4 — Multiple Parameters + Calculations
# Exercise 16 — Calculate Memory Usage
# ============================================================
#
# Imagine a server has:
#
#     total_memory = 16  # GB
#     used_memory = 12   # GB
#
# Write a function:
#
#     def memory_usage(total, used):
#         ...
#
# The function must:
#
# - calculate the percentage of memory being used
# - return a message containing the memory usage percentage
#
# ============================================================
#
# Exercise 17 — Add a memory warning
#
# Now let's make it more Cloud-oriented.
#
# Modify memory_usage() so that:
#
# ≤ 80% → Memory usage is normal: 75%
# > 80% → WARNING: High memory usage: 90%
#
#
# ===========================================================

print("======================================================")
print("Function : Memory Usage")
print("======================================================")


MEMORY_LIMIT = 80

def memory_usage (total_memory: int, used_memory: int) -> str:
    used_percentage = used_memory * 100 / total_memory

    memory_stat = (
        f"WARNING: High memory usage: {used_percentage:g}%"
        if used_percentage > MEMORY_LIMIT
        else  f"Memory usage is normal: {used_percentage:g}%"
    )

    return memory_stat

result_1 = memory_usage(16, 12)
result_2 = memory_usage(16, 15)
print(result_1)
print(result_2)


# ============================================================
# Exercise 18 — Return a Number Instead of a Message
# ============================================================
#
# Until now, your function returned a formatted message:
#
#     return memory_stat
#
# In real automation, we often want a function to return data
# and let another part of the program decide what to do with it.
#
# Goal:
#
# Create a function called:
#
#     calculate_memory_percentage()
#
# It should return only the calculated memory usage percentage.
#
# ============================================================

print("======================================================")
print("Function Calculate Memory %")
print("======================================================")

```python
def calculate_memory_percentage(total: int, used: int) -> float:
    percentage = used * 100 / total
    return percentage


# A function can return a value that we store in a variable.
#
# Here, calculate_memory_percentage() returns the calculated
# percentage, and we store that result in 'percentage'.
#
# We can then use 'percentage' later in our program.
percentage = calculate_memory_percentage(16, 15)


if percentage > MEMORY_LIMIT:
    print(f"Memory usage: {percentage}%")
    print("WARNING: High memory usage")
else:
    print(f"Memory usage: {percentage}%")
    print("Memory usage is normal")


# A ternary expression is a short way to write a simple
# if/else condition when we want to assign a value.
#
# Use a ternary when the condition is simple and both
# possible results are short and easy to understand.
#
# Syntax:
#
#     value_if_true if condition else value_if_false
#
# Here, the result of the condition is assigned to 'status'.
status = (
    f"Memory: {percentage}% -> WARNING"
    if percentage > MEMORY_LIMIT
    else f"Memory: {percentage}% -> NORMAL"
)

print(status)


# The same function can be called multiple times.
#
# The returned value can be stored in the same variable.
#
# Here, 'result' first contains 75%, then it is replaced
# by the result of the second function call.

result = calculate_memory_percentage(16, 12)
print(result)

result = calculate_memory_percentage(16, 15)
print(result)


def get_memory_status(percentage: float) -> str:
    status = (
        "WARNING"
        if percentage > MEMORY_LIMIT
        else "NORMAL"
    )

    return status


# ============================================================
# Using the result of one function as a parameter of another
# ============================================================
#
# A function can return a value, and that value can then be
# passed directly to another function.
#
# Here, we first calculate the memory percentage:
#
#     calculate_memory_percentage(16, 15)
#
# The result is stored in 'percentage_2'.
#
# Then we pass 'percentage_2' as the parameter of
# get_memory_status().
#
# Data flow:
#
#     calculate_memory_percentage()
#                ↓
#          percentage_2
#                ↓
#       get_memory_status()
#                ↓
#             status_1
#
# This allows us to separate different responsibilities:
#
# - calculate_memory_percentage() -> calculates the data
# - get_memory_status()           -> analyzes the data
#
# ============================================================

percentage_2 = calculate_memory_percentage(16, 15)
status_1 = get_memory_status(percentage_2)

percentage_3 = calculate_memory_percentage(16, 12)
status_2 = get_memory_status(percentage_3)

print(f"Memory: {percentage_2}% -> {status_1}")
print(f"Memory: {percentage_3}% -> {status_2}")


# ============================================================
# Optional / Default Parameters
# ============================================================
#
# A function parameter can have a default value.
#
# Here:
#
#     limit: int = 80
#
# means that 'limit' has a default value of 80.
#
# Therefore, 'limit' is optional when calling the function.
#
# If we write:
#
#     check_cpu(75)
#
# Python automatically uses:
#
#     limit = 80
#
# We can also provide another value to replace the default:
#
#     check_cpu(75, 70)
#
# In this case:
#
#     cpu   = 75
#     limit = 70
#
# ============================================================


def check_cpu(cpu: int, limit: int = 80) -> str:
    status = (
        f"WARNING: high CPU usage: {cpu}%"
        if cpu > limit
        else f"CPU usage is normal: {cpu}%"
    )

    return status


# No value is provided for 'limit'.
# The default value of 80 is therefore used.
result_4 = check_cpu(75)

result_5 = check_cpu(90)


# Here, we provide a value for 'limit'.
# This replaces the default value of 80.
result_6 = check_cpu(75, 70)


print(result_4)
print(result_5)
print(result_6)


# ============================================================
# Keyword Arguments
# ============================================================
#
# We can also specify the parameter name when calling
# the function.
#
# For example:
#
#     check_cpu(90, limit=85)
#
# 'limit=85' is called a keyword argument.
#
# It explicitly tells Python:
#
#     limit = 85
#
# When using keyword arguments, we don't have to rely
# only on the position of the argument.
#
# For example, these two calls will be equivalent if we set cpu optional 
# (ex: def check_cpu(cpu: int = 0, limit: int = 80) -> str: ):
#
#     check_cpu(90, limit=85)
#
#     check_cpu(limit=85, cpu=90)
#
# Python knows which value belongs to which parameter
# because we explicitly provide the parameter names.
#
# This is useful when a function has several parameters,
# especially when some parameters are optional.
#
# ============================================================

result_7 = check_cpu(75)

result_8 = check_cpu(90, limit=85)

result_9 = check_cpu(75, limit=70)


print(result_7)
print(result_8)
print(result_9)
