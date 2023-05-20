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
Zorg eerst dat [de backend]({{< relref "/docs/server-deployment/backend" >}}) is ingesteld vooraleer u aan deze stap begint.
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

#### Website publiceren
De website is nu klaar om op de productieserver gedeployed te worden; hiervoor moet allereerst
het frontend project gebuild worden:
```bash
npm run build
```
Dit zal een map `dist` aanmaken met alle benodigde bestanden voor de website.
Om zeker te zijn dat nginx toegang heeft tot al deze bestanden, gebruiken we het volgende commando:
```bash
mkdir -p /var/www/html/dist
sudo bindfs -u www-data -g www-data /home/<gebruikersnaam>/Dr-Trottoir-5/frontend/dist /var/www/html/dist
```
Dit maakt een map aan die altijd dezelfde bestanden zal bevatten als de `dist` map in ons project.
Deze map is reeds als pagina opengesteld in de backend stappen dus na het uitvoeren van deze laatste stap
zou de webapplicatie volledig moeten werken.