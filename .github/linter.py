import yaml

with open('nodes.yaml') as f:
    nodes = yaml.safe_load(f.read())

with open('hosts.yaml') as f:
    hosts = yaml.safe_load(f.read())

has_errors = False

def error(msg):
    print(f"error: {msg}")
    global has_errors
    has_errors = True

def warning(msg):
    print(f"warning: {msg}")

for net in ["mainnet", "testnet", "stagenet"]:
    for type in ["tor", "i2p", "clearnet"]:
        if not nodes[net][type]:
            warning(f"no nodes for {net}.{type}")
            continue

        keys = list(nodes[net][type])
        if keys != sorted(keys):
            error(f"keys in {net}.{type} aren't sorted alphabetically\n  Current: {keys}\n  Sorted:  {sorted(keys)}")

        for key in keys:
            if key not in hosts:
                error(f"no host information defined in hosts.yaml for {key}")

contact_keys = set({"email", "github", "matrix", "reddit", "twitter", "website"})
verification_key = "verification"

host_keys = list(hosts)
if host_keys != sorted(host_keys):
    error(f"keys in hosts.yaml aren't sorted alphabetically\n  Current: {host_keys}\n  Sorted:  {sorted(host_keys)}")

for host in hosts:
    contact_info = hosts[host]

    invalid_keys = set(contact_info) - contact_keys.union({verification_key})
    if invalid_keys:
        error(f"host {host} has invalid keys: {invalid_keys}")

    valid_contact_keys = set(contact_info) & contact_keys
    if len(valid_contact_keys) < 2:
        warning(f"please add at least two contacts for {host}")
        # Not an error for now

    if verification_key not in contact_info:
        warning(f"no verification URL for {host}")
        # Not an error for now

if has_errors:
    exit(1)
