#!/bin/bash

echo "$HOSTNAME"

/home/pi/start_ovs.sh

ip addr flush eth0
ip addr flush eth1
ip addr flush eth2
ip addr flush eth3

ovs-ofctl dump-flows br0 -O OpenFlow13
