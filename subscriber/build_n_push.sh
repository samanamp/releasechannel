#!/bin/bash
docker build -t subscriber .
docker tag subscriber 152648440807.dkr.ecr.us-east-1.amazonaws.com/subscriber
docker push 152648440807.dkr.ecr.us-east-1.amazonaws.com/subscriber