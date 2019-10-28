#!/bin/bash

echo "$HOSTNAME"

apt update
apt upgrade -y

apt install vim -y
