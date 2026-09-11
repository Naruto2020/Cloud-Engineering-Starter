# 5.11 — Starting, stopping, and restarting services
# With `systemctl`, you can also control services.
#
# ### Start
#
# sudo systemctl start nginx
#
# Starts nginx if it isn't running.
#
# ### Stop
#
# sudo systemctl stop nginx
#
# Stops nginx.
#
# ### Restart
#
# sudo systemctl restart nginx
#
# Stops and starts it again.
#
# ### Enable at boot
#
# sudo systemctl enable nginx
#
# This tells Linux to **automatically start nginx when the system boots**.
#
# ### Disable at boot
#
# sudo systemctl disable nginx
#
# Prevents automatic startup at boot.
#
# ---
#
# ## Very important distinction
#
# These are two different concepts:
#
# systemctl start nginx
#
# ➡️ Start nginx **now**.
#
# systemctl enable nginx
#
# ➡️ Configure nginx to **start automatically at boot**.
#
# So:
#
# start   → now
# enable  → boot
#
# And similarly:
#
# stop     → stop now
# disable  → don't automatically start at boot
#
# ---
#
# # 🧪 Exercise 10
#
# You have a server running nginx.
#
# For each requirement, give the correct command:
#

**1.** Start nginx right now. 

systemctl start nginx 

**2.** Stop nginx right now. 

systemctl stop nginx 

**3.** Restart nginx right now. 

systemctl restart nginx 

**4.** Make nginx automatically start when the server boots. 

systemctl enable nginx 

**5.** What is the difference between: systemctl start nginx and 
systemctl enable nginx 

The first start nginx now while the second ask linux to start it at boot
