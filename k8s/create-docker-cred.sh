#!/bin/bash

# Clear old secret
kubectl delete secret --ignore-not-found --namespace=personal-website aws-ecr 
# Create a new one
kubectl create secret docker-registry aws-ecr \
  --docker-server=573500965530.dkr.ecr.us-east-2.amazonaws.com \
  --docker-username=AWS \
  --docker-password=$(aws ecr get-login-password --region us-east-2 --profile ecrpersonalwebsite) \
  --namespace=personal-website