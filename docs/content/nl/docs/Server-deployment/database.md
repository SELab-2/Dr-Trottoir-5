---
categories: ["Deployment"]
tags: ["backend", "database"]
title: "Database"
linkTitle: "Database"
date: 2023-03-11
weight: 30 #database moet vanboven staan want moet in orde zijn voor het opstarten van de backend
description: >
    Hoe start je de database op
---

#### Database aanmaken
Om te beginnen maak je een nieuwe gebruiker aan op postgresql die de database zal beheren:
```bash
su - postgres
createuser --interactive --pwprompt
Enter name of role to add: dbadmin
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) y

createdb -0 dbadmin drtrottoir
```
Dit zal een gebruiker *dbadmin* aanmaken die de databank *drtrottoir* zal kunnen beheren - deze gegevens zullen later nodig zijn bij het instellen van de backend.

#### Database beheren
Om de toegang tot de database makkelijker te maken zullen we remote access aanzetten, zodat bijvoorbeeld pgadmin gebruikt kan worden om de database te beheren.
Hiervoor openen we het volgende configuratiebestand:
```bash
sudo vim /etc/postgresql/14/main/postgresql.conf
```
Zoek de lijn met de volgende inhoud op:
```bash
#listen_address = 'localhost'
```
En wijzig dit zodat de database via het internet bereikt kan worden:
```bash
listen_address = '*'
```

Om binnenkomende verbindingen naar de database toe te staan zal nog een bestand bewerkt moeten worden:
```bash
sudo vim /etc/postgresql/14/main/pg_hba.conf
```
Zoek de lijn met de volgende inhoud op:
```bash
# IPv4 local connections:
host  all all 127.0.0.1/32  md5
```
En wijzig deze:
```bash
# IPv4 local connections:
host  all all 0.0.0.0/0  md5
```
Eventueel kan de toegang beperkt worden door slechts één of enkele ip addressen toe te laten in het bovenstaande bestand, als extra beveiliging.

Pas ten slotte deze wijzigingen toe door postgresql te herstarten:
```bash
sudo systemctl restart postgresql
```