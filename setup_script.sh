#!/bin/bash
sudo apt-get update
sudo apt remove -y unattended-upgrades
sudo apt-get -y upgrade
sudo apt-get install -y python3 python3-pip python3-venv nodejs npm
sudo npm install -g vuepress
sudo npm install -g npm@7.14.0
