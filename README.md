# Miflorium
MiFlora BLE plant sensor status poller

[![Docker Pulls](https://img.shields.io/docker/pulls/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)
[![Docker Build](https://img.shields.io/docker/cloud/build/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)
[![Docker Build](https://img.shields.io/docker/cloud/automated/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)


#### Example usage using Python 3
```$bash
# setup environment
python3 -mvenv venv
. ./venv/bin/activate
pip install -r requirements.txt
# Give blupy helper required capabilities to allow run as non-root user
sudo setcap 'cap_net_raw,cap_net_admin+eip' $(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/bluepy/bluepy-helper

# run the app
python miflorium.py --scan
Scanning for 10 seconds...
Found 3 devices:
  XX:XX:XX:XX:XX:X1
  XX:XX:XX:XX:XX:X2
  XX:XX:XX:XX:XX:X3

python miflorium.py XX:XX:XX:XX:XX:X1 XX:XX:XX:XX:XX:X2
===
 MAC: XX:XX:XX:XX:XX:X1
     Firmware: 3.2.2
  Temperature: 24.1
     Moisture: 1
        Light: 396
 Conductivity: 0
      Battery: 100

===
 MAC: XX:XX:XX:XX:XX:X2
     Firmware: 3.2.2
  Temperature: 20.2
     Moisture: 15
        Light: 741
 Conductivity: 105
      Battery: 0
```

#### Run in Docker
```$bash
docker run --net=host --cap-add=NET_ADMIN -ti miflora-poller:latest --scan
docker run --net=host --cap-add=NET_ADMIN -ti miflora-poller:latest XX:XX:XX:XX:XX:X1 XX:XX:XX:XX:XX:X1
```

#### Build your own docker image
```$bash
docker build -t miflora-poller .

# Based on Debian buster (slightly larger)
docker build -t miflora-poller -f Dockerfile.buster .
```
