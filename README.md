# FS
Easily Sort Files with their Formats



# INSTALL

For install clamAV:

> Ubuntu

$ sudo apt update

$ sudo apt-get install clamav clamav-daemon

$ sudo systemctl stop clamav-freshclam

$ sudo freshclam


Note : I recomend To Download Database Signature File manually.

$ wget https://database.clamav.net/daily.cvd
$ sudo mkdir /var/lib/clamav
$ cp daily.cvd /var/lib/clamav/daily.cvd
$ sudo systemctl start clamav-freshclam



> centos 8

$ sudo su -

$ dnf install epel-release -y

$ dnf install clamav -y

$ dnf install clamd -y

$ dnf install clamav clamd clamav-update -y

 Configure SElinux for ClamAV

$ setsebool -P antivirus_can_scan_system 1

Download latest Signature

$ freshclam

ClamAV configuration

$ sed -i 's/#LocalSocket \/run/LocalSocket \/run/g' /etc/clamd.d/scan.conf

Create ClamAV Systemd Service

 Create ClamAV Systemd Service

$ vi /usr/lib/systemd/system/freshclam.service

add below lines in freshclam.service file and save the changes.

[Unit]
Description = ClamAV Scanner
After = network.target

[Service]
Type = forking
## if you want to scan more than one in a day change the number 1 with your desired number in below line.
ExecStart = /usr/bin/freshclam -d -c 1
Restart = on-failure
PrivateTmp =true

[Install]
WantedBy=multi-user.target

Start and enable services

$ systemctl start clamd@scan
$ systemctl start freshclam
$ systemctl enable clamd@scan
$ systemctl enable freshclam


==> Install FS

$ wget https://github.com/KooshaYeganeh/FS/archive/refs/heads/main.zip

$ unzip main.zip

$ cd FS-main

Ubuntu :

$ python3 sort.py

centos8:

$ python sort.py



