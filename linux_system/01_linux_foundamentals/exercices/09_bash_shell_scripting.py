# ============================================================
# Bash — Exit Codes, `&&` and `||`
# ============================================================

# 1. Exit Codes

Linux commands return an exit status after they finish.

0 → success
non-zero → failure / error / condition not satisfied

Bash makes the exit status of the previous command available through `$?`.

Example:

systemctl is-active nginx
echo $?

The command output and its exit code are two different things.

If Nginx is inactive:

systemctl is-active nginx

can print:

inactive

while the exit code can be:

3

If Nginx is active:

systemctl is-active nginx
echo $?

the exit code should normally be:

0.


# 2. Practice — Checking a Service

systemctl is-active nginx
echo $?

This connects:

systemctl
↓
service state
↓
exit code
↓
Bash decision


# 3. Command Substitution and Variables

server_name=$(hostname)
environment="production"

echo "Server: $server_name Environment: $environment"


# 4. Using Exit Codes with `&&` and `||`

command && success_command || failure_command

Example:

systemctl is-active nginx && echo "running" || echo "not running"

The logic is:

command
↓
exit 0 → execute the command after `&&`
↓
non-zero → skip `&&` and execute the command after `||`

Full health check:

server_name=$(hostname)
environment="production"

systemctl is-active nginx && \
echo "Server: $server_name Environment: $environment Nginx is running" || \
echo "Server: $server_name Environment: $environment Nginx is not running"


# 5. Three Ways to Handle Command Results

status=$(systemctl is-active nginx)

systemctl is-active nginx

if [ $? -eq 0 ]; then
    ...
fi

systemctl is-active nginx && echo "running" || echo "not running"


# 6. Important Caveat About `&&` and `||`

command && success_command || failure_command

If `command` succeeds but `success_command` fails,
`failure_command` can also be executed.

For more complex or production scripts,
an explicit `if/else` is often clearer.


# 7. Bash Skills Practiced So Far

- Shebang and script execution
- Variables
- Command substitution `$()`
- `if / elif / else`
- String comparison
- Exit codes `$?`
- `&&`
- `||`
- Checking the state of a systemd service
- Using command results in a health check
- Combining variables, commands and conditions
