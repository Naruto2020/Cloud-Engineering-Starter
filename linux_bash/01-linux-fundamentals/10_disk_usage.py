
=================================================================

5.15 — Disk Usage: df vs du

================================================================

Now let's learn two commands you'll use constantly as a Cloud/DevOps Engineer.

1. df — filesystem disk space

df shows how much disk space is available on filesystems.

df -h

Example:

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   42G  5.5G  89% /


Important columns:

Column	Meaning
Size	Total filesystem size
Used	Space currently used
Avail	Space available
Use%	Percentage used
Mounted on	Where the filesystem is mounted

The -h means human-readable (G, M, etc.).


2. du — directory/file usage

du shows how much disk space files/directories are actually consuming.

For example:

du -sh /var/log

Possible result:

2.4G    /var/log

Meaning /var/log is using approximately 2.4 GiB.

Useful commands:

du -sh /var/log
du -sh /home/steve
du -sh *

-s = summary
-h = human-readable


The key difference

Think of it this way:

df → "How full is my filesystem?"

du → "What is using all that space?"

For example, you notice:

df -h

shows:

Use% = 95%

Then you investigate:

du -sh /var/*

to find which directories are consuming the space.

This is a very common production troubleshooting workflow.


Exercise 15

Suppose you run:

df -h

and get:

Filesystem      Size  Used  Avail  Use%  Mounted on
/dev/sda1        50G   47G    3G    94%  /

Answer these one by one:

What is the total filesystem size?

==> 50G

How much space is currently used?

==> 47G

How much space is available?

==> 3G


Is 94% a value you should investigate on a production server?

==> Yes

Which command would you use to investigate which directory is consuming
the most disk space?

==> 1- du -sh *
    2- du -sh /var/*
