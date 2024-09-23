## Default Node List

A node may be added if:
- The host has an established presence in a privacy-focused community
- The host makes an effort to keep their node up-to-date and online
- The host can be contacted in case there are problems
- The node does not have RPC payments enabled

A node may be removed if:
- The host cannot be contacted
- The host no longer wants it listed
- The node has RPC payments enabled
- The node consistently fails to relay transactions
- The node fails to synchronize to the latest block
- The node is offline for an extended period of time
- The node is shown to be malicious or misconfigured
- The node is on a fork that does not have community consensus
- The node has other problems that are not remedied within a reasonable time
- The maintainers of this repo determine that the Monero community does not trust the host

### Creating a copy-pasteable custom list

```shell
$ pip3 install pyyaml
$ python get_node_list.py
Select monero network:
1) mainnet
2) stagenet
3) testnet
Enter choice [1]: 1

Select anonymity network:
1) tor
2) i2p
3) clearnet
Enter choice [1]: 3

Which hosts to include?
1) include all hosts
2) include specific hosts
3) exclude specific hosts
Enter choice [1]: 2

Select hosts to include (separated by a space):
1) cakewallet
2) lza_menace
3) majesticbank
4) plowsof
5) ravfx
6) rino
7) rucknium
8) selsta
9) sethforprivacy
10) stormycloud.org
11) trocador
12) xmr.ru
Enter choices: 4 8

node.monerodevs.org:18089
node2.monerodevs.org:18089
node3.monerodevs.org:18089
selsta1.featherwallet.net:18081
selsta2.featherwallet.net:18081
```
