# Python Basics

This section covers the fundamental Python concepts I have learned and practiced as part of my Cloud Engineering journey.

The exercises are based on simple Cloud Engineering scenarios, such as managing and monitoring servers.

## 📚 Concepts Learned

### Variables

Using variables to store and manipulate values.

### Data Types

Working with basic Python data types and values.

### Conditions

Using conditional statements to make decisions in a program.

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

### For Loops

Using `for` loops to iterate over collections of data.

```python
for server in servers:
    ...
```

### Dictionaries

Using dictionaries to represent structured data.

For example, a server can be represented as:

```python
server = {
    "name": "web-01",
    "status": "running",
    "cpu": 45
}
```

Values can then be accessed using their keys:

```python
server["name"]
server["status"]
server["cpu"]
```

### Formatted Strings (f-strings)

Using f-strings to dynamically insert values into strings.

```python
print(f"{server['name']} -> {server['cpu']}%")
```

### Ternary Expressions

Using a conditional expression to assign a value depending on a condition.

```python
status_text = "Warning" if server["cpu"] > 80 else ""
```

## ☁️ Cloud Engineering Context

The exercises use server-related data to practice Python fundamentals.

For example:

* Checking whether a server is running
* Reading server information
* Checking CPU usage
* Displaying server status
* Detecting high CPU usage

This provides an introduction to using Python for **system monitoring and automation**.

## 🧪 Exercises

Practical exercises for this section are stored in the `exercises/` directory.

The exercises progressively combine the concepts learned in this section.

## 📝 Key Takeaways

* Variables allow data to be stored and manipulated.
* Conditions allow programs to make decisions.
* `for` loops allow data to be processed iteratively.
* Dictionaries are useful for representing structured data.
* f-strings make dynamic output easier to read.
* Ternary expressions provide a compact way to write simple conditional assignments.

---

> This section will be updated as I progress through the Python fundamentals.
