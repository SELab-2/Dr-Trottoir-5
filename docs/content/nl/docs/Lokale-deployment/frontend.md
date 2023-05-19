---
categories: ["Deployment"]
tags: ["frontend"]
title: "Frontend"
linkTitle: "Frontend"
date: 2023-03-11
description: >
    Hoe je de frontend moet opstarten
---
#### Frontend instellen
Zorg eerst dat [de backend]({{< relref "/docs/lokale-deployment/backend" >}}) is ingesteld vooraleer u aan deze stap begint.
Veronderstellend dat u de backend stappen zojuist heeft doorlopen, kunt u nu de frontend map betreden en de benodigde pakketten installeren met de
volgende commando's:
```bash
cd ../frontend
git submodule update --init --recursive
cd ./src/api/EchoFetch
npm install
npm run build
cd ../../..
npm install --force
```

#### Frontend opstarten
Als de vorige stap doorlopen is, kan nu de frontend worden opgestart zodat de webapplicatie lokaal bezocht kan worden.
Het volgende commando zal de applicatie starten en direct bijwerken zodra een bestand wordt aangepast:
```bash
npm run serve
```

De website zal nu bereikbaar zijn op `http://127.0.0.1:8080`.
