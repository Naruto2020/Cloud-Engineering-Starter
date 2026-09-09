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


