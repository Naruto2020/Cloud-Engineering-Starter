# ============================================================
# Exercise 3 — Numeric Permissions
# ============================================================

# Now we'll learn the numeric notation, which you'll see
# constantly on Linux servers:

# chmod 755 script.sh
# chmod 64# What permissions do these represent?


# A.

# 755
Owner : rwx
Group : r-x
Other : r-x


# B.

# 644
Owner: rw-
Group: r--
Other: r--

# C.

# 600
Owner: rw-
Group: ---
Other: ---
4 config.txt
# chmod 600 secret.txt


# Before we use it, answer this:

# Linux assigns numbers to permissions:

# r = 4
# w = 2
# x = 1
# - = 0


# Therefore:

# rwx = 4 + 2 + 1 = 7
# rw- = 4 + 2 + 0 = 6
# r-x = 4 + 0 + 1 = 5
# r-- = 4 + 0 + 0 = 4


# ============================================================
# Question
# ============================================================

# What permissions do these represent?


# A.

# 755
Owner : rwx
Group : r-x
Other : r-x


# B.

# 644
Owner: rw-
Group: r--
Other: r--

# C.

# 600
Owner: rw-
Group: ---
Other: ---

# Give me the permissions for owner / group / others
# for each one.

# ============================================================
# Important Shortcut
# ============================================================

# Memorize these:

# 755 → rwxr-xr-x
# 644 → rw-r--r--
# 600 → rw-------


# You'll encounter them frequently when working with Linux,
# SSH keys, scripts, configuration files, and cloud servers.


# ============================================================
# One Important Distinction
# ============================================================

# For a file:

# x = execute the file


# For a directory:

# x = enter/access the directory


# We'll come back to that because it's important.


# ============================================================
# Exercise 4 — Real Cloud/DevOps Scenario
# ============================================================

# You have these files:

# app.sh
# config.env
# private.key


# You want:

# app.sh → owner can read/write/execute;
#          everyone else can read/execute.

# config.env → owner can read/write;
#              group and others can only read.

# private.key → only the owner can read/write.


# ============================================================
# Question
# ============================================================

# Which chmod should you use for each?

app.sh      → chmod 755 app.sh
Because : Owner : rwx / Group : r-x / Other : r-x

config.env  → chmod 644 config.env
Because : Owner : rw- / Group : r-- / Other : r--

private.key → chmod 600 private.key
Because : Owner : rw- / Group : --- / Other : ---


# Choose from:

# 755
# 644
# 600


# And explain why for each one.


# ============================================================

# ⭐ Cloud/DevOps Relevance

# ============================================================

# These three are particularly useful to remember:

# chmod 755 app.sh

# chmod 644 config.env

# chmod 600 private.key

# Especially:

# chmod 600 private.key

# because private keys should not be accessible by other users.


# ============================================================

# 4.5 — chown: Changing Ownership

# ============================================================

# So far we've learned how to change permissions with:

# chmod

# Now we need to learn how to change ownership.

# The command is:

# chown

# For example:

# chown steve config.txt

# means:

#

# Make steve the owner of config.txt.

# You can also change owner + group:

# chown steve:developers config.txt

# Meaning:

# owner → steve

# group → developers

# You can verify it with:

# ls -l config.txt

# ============================================================

# 🎯 Exercise 5

# ============================================================

# Suppose we have:

# -rw-r--r-- 1 root developers 250 Sep 9 config.txt

# You want:

#

# steve should become the owner, while the group developers

# stays unchanged.

# Question

#

# Which command is correct?

# A

# chown steve:developers config.txt

# B

# chown steve config.txt

# C

# chmod steve config.txt

# And explain what happens to the owner and group after

# the command.

B `chown steve config.txt`

Because `chown` is used to change the owner of a file,
and we want `steve` to become the owner while keeping the 
`developers` group unchanged.


# ============================================================

# Exercise 6 — chgrp

# ============================================================

# There is also a command specifically for changing the group:

# chgrp

# Suppose:

# -rw-r--r-- 1 steve developers config.txt

# You want to change the group from developers to devops,

# while keeping steve as the owner.

# What command would you use?

# A

# chgrp devops config.txt

# B

# chown devops config.txt

# C

# chmod devops config.txt

# And tell me what the resulting owner and group will be.

A chgrp devops config.txt
Result : -rw-r--r-- 1 steve devops config.txt


# ============================================================

# 🧠 The Three Commands to Remember

# ============================================================

# chmod          # change permissions

# chown          # change owner

# chgrp          # change group

# And:

# chown steve config.txt

# → owner

# chown steve:devops config.txt

# → owner + group

# chgrp devops config.txt

# → group only
