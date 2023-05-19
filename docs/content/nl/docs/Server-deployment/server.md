---
categories: ["Deployment"]
tags: ["backend", "server", "frontend"]
title: "Server"
weight: 1
linkTitle: "Server"
date: 2023-03-11
description: >
    Hoe stel je de server in
---

##### Benodigde pakketten
* nginx
* python 3.11
* git
* postgresql
* nodejs
* bindfs

Deze pakketten zijn op de volgende manier te installeren:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.11 nginx git postgresql postgresql-contrib
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&\
sudo apt-get install -y nodejs bindfs
```

Clone vervolgens de [github repo](https://github.com/SELab-2/Dr-Trottoir-5):
```bash
git clone git@github.com:SELab-2/Dr-Trottoir-5.git
cd Dr-Trottoir-5
```

Ga nu verder met het instellen van [de database]({{< relref "/docs/server-deployment/database" >}}).