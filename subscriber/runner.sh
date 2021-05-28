#!/bin/sh

sudo docker run -d --env-file /home/ubuntu/env-file -p 80:80 subscriber
