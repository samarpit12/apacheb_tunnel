import os
import threading
from netifaces import interfaces, ifaddresses, AF_INET
from multiprocessing import Pool
import multiprocessing.dummy as mp
import thread
import subprocess


list_of_URL = []
N = 20000
url_loadList = []

def ip4_addresses():
    ip_list = []
    matching = [s for s in interfaces() if "tun" in s]
    for interface in matching:
                for link in ifaddresses(interface)[AF_INET]:
                        ip_list.append(link['addr'])
    return ip_list

tunnel_addr =  ip4_addresses()

def processor(cmd):
	print cmd
	proc = subprocess.Popen(cmd,shell=True,)
	return

def begin_load(urls):
	global tunnel_addr
	cmd = "ab -n 100 -c 10 " + "-B " + tunnel_ip +" "+ urls



with open("/root/top-1m.csv", "r") as file:
	for i in range(N):
		url1 =file.next().split(',')[1].strip('\r\n')
		list_of_URL.append(url1)

for URL in list_of_URL:
	for t in tunnel_addr:
		cmd = "ab -n 100 -c 10 " + "-B " + t +" http://"+ URL + "/"
		url_loadList.append(cmd)

print len(url_loadList)

for i in url_loadList:
	thread.start_new_thread(processor, (i,))



