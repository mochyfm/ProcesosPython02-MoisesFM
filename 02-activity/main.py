# -*- coding: utf-8 -*-

from ping import Ping

goodPing = Ping('google.com', 3);

info = goodPing.ping();

# When we call it, it will return a dictionary with 2 keys:

# outputInfo: Will return a dictionary with all the information about the ping command.
# state: It returns a boolean for the correct output of the ping command.

# After all its made we can show it.

print(info);