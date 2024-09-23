#!/usr/bin/env python3
try:
    import yaml
except:
    print("pyyaml is not installed")
    exit(1)


def invalid_choice():
    print("Invalid choice")
    exit(1)


def print_list(lst):
    for i, item in enumerate(lst):
        print(f"{i+1}) {item}")


def get_index(lst, choice):
    if not choice.isdigit():
        invalid_choice()

    choice = int(choice)
    if choice == 0:
        invalid_choice()

    index = choice - 1
    if index >= len(lst):
        invalid_choice()

    return index


def get_choice(lst, msg=None, default_choice="1"):
    if msg:
        print(msg)
    print_list(lst)
    choice = input(f"Enter choice [{default_choice}]: ") or default_choice
    print()
    return get_index(lst, choice)


def get_choices(lst, msg=None):
    if msg:
        print(f"{msg} (separated by a space):")
    print_list(lst)
    choices = input(f"Enter choices: ").split()
    print()
    indexes = []
    for choice in choices:
        indexes.append(get_index(lst, choice))
    return indexes


with open("nodes.yaml") as f:
    nodes = yaml.safe_load(f.read())

# Select monero network
monero_nets = ["mainnet", "stagenet", "testnet"]
monero_net = monero_nets[get_choice(monero_nets, "Select monero network:")]

# Select anonymity network
anon_nets = ["tor", "i2p", "clearnet"]
anon_net = anon_nets[get_choice(anon_nets, "Select anonymity network:")]

node_list = nodes[monero_net][anon_net]
hosts = list(node_list)

host_options = ["include all hosts", "include specific hosts", "exclude specific hosts"]
host_option = get_choice(host_options, "Which hosts to include?")

selected_nodes = []
match host_option:
    case 0:
        for nodes in node_list.values():
            selected_nodes += nodes

    case 1:
        selected_indexes = get_choices(hosts, "Select hosts to include", )
        for index in selected_indexes:
            selected_nodes += node_list[hosts[index]]

    case 2:
        excluded_indexes = get_choices(hosts, "Select hosts to exclude", )
        selected_indexes = set(range(len(hosts))) - set(excluded_indexes)
        for index in selected_indexes:
            selected_nodes += node_list[hosts[index]]

    case default:
        invalid_choice()

print("\n".join(selected_nodes))
