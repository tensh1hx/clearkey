import os
import sys
import re

os.system('cls')

os.popen('netsh wlan show profiles')

output = os.popen('netsh wlan show profiles').read()

wifis = re.sub('''\nProfiles on interface Wi-Fi?(.*?)User profiles
-------------\n''', '', output, flags=re.DOTALL)

content = wifis
toDel = "    All User Profile     : "
content = content.replace(toDel, '')
wifi = content.split('\n')[:-2]

clk = '\033[94m' + """
  /$$$$$$  /$$                               /$$   /$$                    
 /$$__  $$| $$                              | $$  /$$/                    
| $$  \__/| $$  /$$$$$$   /$$$$$$   /$$$$$$ | $$ /$$/   /$$$$$$  /$$   /$$
| $$      | $$ /$$__  $$ |____  $$ /$$__  $$| $$$$$/   /$$__  $$| $$  | $$
| $$      | $$| $$$$$$$$  /$$$$$$$| $$  \__/| $$  $$  | $$$$$$$$| $$  | $$
| $$    $$| $$| $$_____/ /$$__  $$| $$      | $$\  $$ | $$_____/| $$  | $$
|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$      | $$ \  $$|  $$$$$$$|  $$$$$$$
 \______/ |__/ \_______/ \_______/|__/      |__/  \__/ \_______/ \____  $$
                                                                 /$$  | $$
                                                                |  $$$$$$/
                                                                 \______/ 

"""

print(clk)

print('')
print('\033[95m' + "By @tensh1hx | https://github.com/tensh1hx | You can modify or redistribute the script.")
print('')
print('')

print('\033[92m' + "[*] Available networks: \n")

a = 0

for i in wifi:
    print('\033[97m' + "[{}]".format(a), end=" ")
    print(i)
    a += 1

print("[X] Give me all the keys for the available networks")

a -= 1

selectNet = input('\033[92m' + "\n[?] Choose a network: ")

if selectNet == 'x':
    selectNet = 'X'
else:
    pass

print('')

if selectNet == 'X':
    while a >= 0:
        targ = wifi[a]
        os.popen('netsh wlan show profiles NAME="{}" key=clear'.format(targ))
        output = os.popen('netsh wlan show profiles NAME="{}" key=clear'.format(targ)).read()
        skey = re.search('Security key           : (.*)\n', output)
        present = "Present"
        if present in str(skey):
            pass
        else:
            print('\033[91m' + "[!] Security key is absent for '{}'.".format(targ) + '\033[99m')
            continue
        key = re.search('Key Content            : (.*)\n', output)
        print('\033[97m' + "Key for '{}' is '{}'.".format(targ, key.group(1)))
        a -= 1
else:
    selectNet = int(selectNet)
    try:
        targ = wifi[selectNet]
    except IndexError:
        print('\033[91m' + "\n[!] This element doesn't exist!")
        sys.exit()
    os.popen('netsh wlan show profiles NAME="{}" key=clear'.format(targ))
    output = os.popen('netsh wlan show profiles NAME="{}" key=clear'.format(targ)).read()
    skey = re.search('Security key           : (.*)\n', output)
    present = "Present"
    if present in str(skey):
        pass
    else:
        print('\033[91m' + "[!] Security key is absent for '{}'.".format(targ))
        exit()
    key = re.search('Key Content            : (.*)\n', output)
    print('\033[97m' + "Key for '{}' is '{}'.".format(targ, key.group(1)))

print('\033[99m' + '')

sys.exit()
