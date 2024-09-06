#!/usr/bin/env python3

import os

ip = input("Please enter an IP address: ")
className = input("Please enter the class name: ")
os.chdir("/home/kali/Documents/TryHackMe")
os.mkdir(className)
os.chdir(className)

# nmap scan the ip
os.system("nmap -sC -sV -Pn " + ip + " --stats-every 30s > nmap_results.txt")

# nikto scan the ip
os.system("nikto -h " + ip + " >> nikto_results.txt")
