# ParkAndGo-Detection-Model

![pandgo](resources/icon_small.png) 

## Introduction

This ParkAndGo solution intends to utlize the Faster RCNN Object Detection Model to analyze CCTV Footage and identify free and occupied Parking Spaces. These locations will be updated in firebase realtime database where they will be shown to prospective users through an Ionic Mobile App or an Angular Web App, which can be found [here](https://github.com/ranikamadurawe/ParkAndGo) and [here](https://github.com/ranikamadurawe/ParkAndGoweb) respectively

## High-Level Architecture Diagram

![arci](resources/architecture_model.png)

## Starting the server

### Prerequisites

Install all required prerequisites by issuing the command

`pip install requirement.txt`

Download the weight file from here and place it in the root directory

### Running the server locally

To run the server locally issue the following command. The flask application will listen on port 5000

`python app.py`

### Running the Server using Containers or through Kubernetes

Optionally to run the server as a container issue the following command to generate a Docker Container

`docker build --tag <container_name>:1.0 .`

To run the above container in a GPU enabled Kubernetes Cluster issue the following commands

```
kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/stable/nvidia-driver-installer/cos/daemonset-preloaded.yaml

kubectl get pods

kubectl run cuda --image=<container-repo>/<container_name>:1.0  --limits="nvidia.com/gpu=1" --port 5000

kubectl expose deployment cuda --type=LoadBalancer --port 80 --target-port 5000

```

Get the currently running container by issuing the command

```
kubectl get containers

```

And use the following command to enter into bash instance of the container

```
kubectl exec -it <container-name> /bin/bash

```

And execute the following commands

```
apt update && apt install -y libsm6 libxext6

apt-get install -y libfontconfig1 libxrender1

```

Exit the bash instance and run the following commands to expose the deployment 

```
kubectl expose deployment cuda --type=LoadBalancer --port 80 --target-port 5000

```

Use the following command to get the EXTERNAL_IP of the created port

```
kubectl get services

```



