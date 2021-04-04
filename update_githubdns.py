'''
This script is to check and update the github dns, so that images can display properly.
step1: open CMD in windows and run below lines;
step2: python your_path_to_this_file\update_githubdns.py
step3: ipconfig /flushdns
'''
import socket

def get_hostname_IP():
    #hostname = input("Please enter URL:")
    hostname = "camo.githubusercontent.com"
    try:
        #print (f'Hostname: {hostname}')
        #print (f'IP: {socket.gethostbyname(hostname)}')
        return socket.gethostbyname(hostname)
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

for_github_ip = get_hostname_IP()
for_github_ip_split=for_github_ip.split(".")
for_github=[
"\n# GitHub Start\n", 
for_github_ip,"    cdn-",for_github_ip_split[0],"-",for_github_ip_split[1],"-",for_github_ip_split[2],"-",for_github_ip_split[3],".github.com\n",
for_github_ip,"    aw.githubusercontent.com\n",
for_github_ip,"    raw.githubusercontent.com\n",
for_github_ip,"    gist.githubusercontent.com\n",
for_github_ip,"    cloud.githubusercontent.com\n",
for_github_ip,"    camo.githubusercontent.com\n",
for_github_ip,"    user-images.githubusercontent.com\n",
for_github_ip,"    repository-images.githubusercontent.com\n",
for_github_ip,"    avatars.githubusercontent.com\n",
for_github_ip,"    avatars0.githubusercontent.com\n",
for_github_ip,"    avatars1.githubusercontent.com\n",
for_github_ip,"    avatars2.githubusercontent.com\n",
for_github_ip,"    avatars3.githubusercontent.com\n",
for_github_ip,"    avatars4.githubusercontent.com\n",
for_github_ip,"    avatars5.githubusercontent.com\n",
for_github_ip,"    avatars6.githubusercontent.com\n",
for_github_ip,"    avatars7.githubusercontent.com\n",
for_github_ip,"    avatars8.githubusercontent.com\n",
"# GitHub End\n"]

#edit and close the file:
with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as modify_file:
    modify_file.writelines(for_github)
    
