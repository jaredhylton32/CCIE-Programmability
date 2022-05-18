from cli import *
import sys

clip(‘command’)
execute(‘command’)
configure(‘command one’, ‘command two’, ‘command three’)


my_var = '''int loop1
            ip address 10.1.1.1 255.255.255.0
            description added by Python
            '''
configurep(my_var)

for i in range(1,6):
	clip(‘ping 10.0.0.’ + str(i))

cli.configure([“interface Loopback1”, “ip address 192.168.255.1 255.255.255.255”, “end”])