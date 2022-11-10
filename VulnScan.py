#!/usr/bin/env python3

import socket
from IPy import IP
import pyfiglet
import subprocess
import time

#//Clear the terminal window//
subprocess.call('clear', shell=True)

#//Port Scanner banner//
Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

#//wait one second before proceeding//
time.sleep(1)

#list to store open ports 
ports = [] 
#list to store discovered banners   
banners = [] 

def scan(target):
        '''//scan target function//'''
        converted_ip = convert_ip(target)
        print('\n' + 'Scanning Target : ' + str(target))
        for port in range(21, 80):
                scan_port(converted_ip, port)

def convert_ip(ip):
        '''//Function Converts the hostname if not already an IP//'''
        try:
                IP(ip)
                return(ip)
        except ValueError:
                return socket.gethostbyname(ip)
#def get_banner(s):
#       '''//function grabs any port banner and returns the data received//''' 
#       return s.recv(1024)

def scan_port(ipaddress, port):
        '''//function scans PORTS of the target and sets the connection timeout>
try: 
        sock = socket.socket() 
        sock.settimeout(0.1) 
        sock.connect((ipaddress, port)) 
    
try:
        banner = get_banner(sock) 
        print('[+] Port ' + str(port) + '  is Open '  + ' : ' + str(banner.deco>
except: 
         print('[+] Port ' + str(port) + ' is Open ')        
except: 
 pass 

try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))

        try:
                ports.append(port)
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                banners.append(banner) 
        except:
                banners.append(' ')
        sock.close()
except:
                pass

#//Scan multiple targets specified with a comma else scan one specified target/>
#//Line 55 prevents the scan function from being called twice if the script is >
if __name__ == "__main__":
        targets = input('[+] Enter Target/s To Scan(for multiple targets use a >
        if ',' in targets:
                for ip_address in targets.split(','):
                        scan(ip_address.strip(' '))
        else: 
                scan(targets)

with open("vulnerable_banners.txt", 'r') as file: 
    count = 0 
    for banner in banners: 
        file.seek(0) 
        for line in file.readlines(): 
            if line.strip() in banner: 
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + st>
        count += 1 
