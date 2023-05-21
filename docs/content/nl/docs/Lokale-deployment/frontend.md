---
categories: ["Deployment"]
tags: ["frontend", "local"]
title: "Frontend"
linkTitle: "Frontend"
date: 2023-03-11
description: >
    Hoe je de frontend moet opstarten
---
# frontend
Zorg eerst dat [de backend]({{< relref "/docs/lokale-deployment/backend" >}}) is ingesteld vooraleer u aan deze stap begint.

## Frontend installeren
Startend vanuit de root van het project voer deze commando's uit om de frontend te installeren
```bash
cd frontend/
git submodule update --init --recursive
cd ./src/api/EchoFetch
npm install
npm run build
cd ../../..
npm install --force
```

## Frontend opstarten
Als de vorige stap doorlopen is, kan nu de frontend worden opgestart zodat de webapplicatie lokaal bezocht kan worden.

Enkel op de production manier is de applicatie als [PWA](https://web.dev/learn/pwa/) beschikbaar.

### Hot-reload
Het volgende commando zal de applicatie starten en direct bijwerken zodra een bestand wordt aangepast:
```bash
npm run serve
```
### Production
Het volgende commando zal de applicatie compilen met minification voor production environments:
```bash
npm install --global serve
npm run build
serve -s dist -l 8080
```
De website zal nu bereikbaar zijn op `http://127.0.0.1:8080`.
