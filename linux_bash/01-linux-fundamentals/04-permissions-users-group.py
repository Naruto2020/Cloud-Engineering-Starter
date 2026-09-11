# Exercise 7 — Users and groups
# Now let's connect **permissions + users + groups**.
#
# Imagine a Linux server has:
#
# Users:
# steve
# alice
# bob
#
# Groups:
# developers
# admins
#
# And:
#
# config.txt
# Owner: steve
# Group: developers
# Permissions: rw-r-----
#
# ### Question
#
# Who can do what?
#
**1. Steve** — can he read the file? Can he write to it?

Yes steve can read and write

**2. Alice**, who belongs to `developers` — can she read it? 
Can she write to it?

Alice can only read it

**3. Bob**, who belongs to neither `developers` nor `admins` — 
can he read it?

Bob cannot read , write or execute


# Break down:
#
# rw-r-----
# ││ ││ │││
# ││ ││ └└└ → others
# ││ └└──── → group
# └└──────── → owner
#
# This is the last important concept before we move 
#toward **permissions on directories**.


# 4.6 — Permissions on directories
# Now comes a **very important Linux concept**.
#
# For a directory, `r`, `w`, and `x` don't mean exactly 
#the same thing as for a file.
#
# For a directory:
#
# | Permission | Meaning                        |
# |------------|--------------------------------|
# | `r`        | List the directory contents    |
# | `w`        | Create/delete/rename entries   |
# | `x`        | Enter/access the directory    |
#
# For example:
#
# drwxr-x---
#
# means:
#
# Owner  → rwx
# Group  → r-x
# Others → ---
#
# So the owner can:
#
# - list files
# - create/delete files
# - enter the directory
#
# The group can:
#
# - list files
# - enter the directory
# - ❌ cannot create/delete files
#
# Others have no access.
#
# ---
#
# ## 🎯 Exercise 8
#
# You have:
#
# drwxr-x---
#
# for a directory called:
#
# /home/steve/app/
#
# And:
#
# Owner = steve
# Group = developers
#
# Answer:
#

1. Can Steve enter the directory?

Yes as (Owner: rwx) he can


2. Can Steve create a new file inside it?

Yes as (Owner: rwx) he can

3. Can someone in `developers` enter the directory?

Yes someone in `developers` (Group: r-x) can
enter directory

4. Can someone in `developers` create a new file inside it?

No someone in `developers` (Group: r-x) can't
create file

5. Can someone outside the group enter the directory?

No Other (---) can't enter directory


# Think carefully about the difference between **`r`**, **`w`**, and **`x`**
# **on a directory**.


# Exercise 9 — `chmod` on a directory
# Suppose we have:
#
# /home/steve/app/
#
# with:
#
# drwxr-x---
#
# Owner: `steve`
#
# Group: `developers`
#
# You want to change it so that:
#
# - **Steve** → can enter, list, create/delete files
# - **developers** → can enter and list, but **cannot create/delete**
# - **others** → have no access
#
# ### Question 1
#

Which numeric permission should you use?
Choose:

A. 700
B. 750
C. 755
D. 770

B => 750

# ### Question 2

What will the resulting permission string be?

drwxr-x---

# ### Question 3

Explain what each number means:

750
Owner -> rwx -> 4 + 2 + 1 = 7
Group -> r-x -> 4 + 0 + 1 = 5
Other -> --- -> 0 + 0 + 0 = 0

# Exercise 10 — Permissions troubleshooting 🔧
# Now let's put everything together.
#
# You're working on a Linux server and have this directory:
#
# /home/steve/app/
#
# You run:
#
# ls -ld /home/steve/app
#
# and get:
#
# drwxr-x--- 2 root developers 4096 Sep 11 app
#
# You are logged in as:
#
# steve
#
# and `steve` belongs to the `developers` group.
#
# You try:
#
# touch /home/steve/app/test.log
#
# but Linux gives you:
#
# Permission denied
#
# ### Questions
#

**1.** Why can't `steve` create `test.log`?

Because `steve` is not the Owner of this directory
it bellong to root and only root can create/delete
or rename entries


**2.** Which permission does `steve` actually get here: 
**owner** or **group**?

`steve` get group permission



**3.** What permission is missing for `steve` to create the file?

`steve` miss w permission

**4.** What would be one way to fix the problem?

The way to fix it is to set `steve` Owner

chown steve /home/steve/app

or give the developers group permission
chmod g+w /home/steve/app
