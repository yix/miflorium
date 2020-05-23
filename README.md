# Miflorium
MiFlora BLE plant sensor status poller

[![Build](https://img.shields.io/github/workflow/status/yix/miflorium/build%20image/v0.0.1)](https://github.com/yix/miflorium/actions)
[![Docker Build](https://img.shields.io/docker/cloud/build/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)
[![Docker Pulls](https://img.shields.io/docker/pulls/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)
[![Docker Build](https://img.shields.io/docker/cloud/automated/mcgunn/miflora-poller.svg?style=plastic)](https://hub.docker.com/r/mcgunn/miflora-poller/)


### Example usage using Python 3
Setup environment (scripts are copy/paste'able)
```bash
git clone https://github.com/yix/miflorium.git
python3 -mvenv venv
. ./venv/bin/activate
pip install -r requirements.txt
sudo setcap 'cap_net_raw,cap_net_admin+eip' $(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')/bluepy/bluepy-helper
```
### Run the app
#### Scan for MiFlora devices
```bash
python miflorium.py --scan
```
Output should be similar to shown below if you have MiFlora devices close by

```Scanning for 10 seconds...
Found 3 devices:
  XX:XX:XX:XX:XX:X1
  XX:XX:XX:XX:XX:X2
  XX:XX:XX:XX:XX:X3
```
#### And fetch some data from them
```bash
python miflorium.py XX:XX:XX:XX:XX:X1 XX:XX:XX:XX:XX:X2
```
```===
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

### Run in Docker
(replace XX:XX:XX:XX:XX:X1 with MAC of your MiFlora device(s))
```bash
docker run --net=host --cap-add=NET_ADMIN -ti mcgunn/miflora-poller:latest --scan
docker run --net=host --cap-add=NET_ADMIN -ti mcgunn/miflora-poller:latest XX:XX:XX:XX:XX:X1 XX:XX:XX:XX:XX:X2
```

### Build docker image locally
```bash
docker build -t miflora-poller .
```

Based on Debian buster (slightly larger)
```
docker build -t miflora-poller -f Dockerfile.buster .
```
To-do: :shipit:
 - add support for MQTT
