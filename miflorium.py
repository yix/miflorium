import argparse
import json

from btlewrap.bluepy import BluepyBackend
from miflora import miflora_scanner
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY


def poll_miflora(mac):
    """Poll data from specific MiFlora sensor."""
    poller = MiFloraPoller(mac, BluepyBackend)
    data = {
        'fw': poller.firmware_version(),
        'temperature': poller.parameter_value(MI_TEMPERATURE),
        'moisture': poller.parameter_value(MI_MOISTURE),
        'light': poller.parameter_value(MI_LIGHT),
        'conductivity': poller.parameter_value(MI_CONDUCTIVITY),
        'battery': poller.parameter_value(MI_BATTERY),
    }
    return data


def scan(format='text'):
    """Scan for sensors."""
    if format == 'text': print('Scanning for 10 seconds...')
    devices = miflora_scanner.scan(BluepyBackend, 10)
    if format == 'text':
        print('Found {} devices:'.format(len(devices)))
        for device in devices:
            print('  {}'.format(device))
    elif format == 'json':
        print(json.dumps(devices, indent=1))


def poll_all_devices(devices, format='json'):
    data = {}
    for mac in devices:
        data[mac] = poll_miflora(mac)
    if format == 'text':
        for mac in data.keys():
            device = data[mac]
            print('===')
            print(' MAC: {:>12}'.format(mac))
            print(' {:>12}: {}'.format('Firmware', device['fw']))
            print(' {:>12}: {}'.format('Temperature', device['temperature']))
            print(' {:>12}: {}'.format('Moisture', device['moisture']))
            print(' {:>12}: {}'.format('Light', device['light']))
            print(' {:>12}: {}'.format('Conductivity', device['conductivity']))
            print(' {:>12}: {}'.format('Battery', device['battery']))
            print()
    elif format == 'json':
        print(json.dumps(data, indent=1))


if __name__ == '__main__':
    # sudo setcap 'cap_net_raw,cap_net_admin+eip' .../<venv or /usr>/lib/python3.7/site-packages/bluepy/bluepy-helper
    # or use --cap-add=NET_ADMIN if run in Docker. --scan also requires root
    parser = argparse.ArgumentParser(description='MiFlora poller.')
    parser.add_argument('macs', metavar='MAC', type=str, nargs='*',
                        help='MAC address of the MiFlora device to poll')
    parser.add_argument('--scan', dest='scan', action='store_const',
                        const=True, default=False,
                        help='Scan for the MiFlora devices')
    parser.add_argument('-o', '--output-format', dest='format',
                        choices=['text', 'json'], default='text',
                        help='Output format JSON or YAML')
    args = parser.parse_args()
    if args.scan:
        scan(format=args.format)
    else:
        poll_all_devices(args.macs, format=args.format)
