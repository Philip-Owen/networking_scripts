from napalm import get_network_driver
import json

driver = get_network_driver('ios')

devices = [
    '10.10.50.254',
    '10.10.50.1',
    '10.10.50.2',
    '10.10.50.3',
]

for device in devices:
    print('******************************************************************')
    dev = driver(hostname=device, username="admin", password="cisco")
    dev.open()
    facts = dev.get_facts()
    hostname = facts["hostname"]
    int = dev.get_interfaces_ip()
    dev.close()
    print(hostname)
    print(json.dumps(int, sort_keys=False, indent=4))
