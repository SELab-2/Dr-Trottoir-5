---
categories: ["Deployment"]
tags: ["backend", "database"]
title: "Backend"
linkTitle: "Backend"
date: 2023-03-11
description: >
    Hoe start je de backend op
---
#### Backend instellen
Zorg dat [de database]({{< relref "/docs/lokale-deployment/database" >}}) is ingesteld alvorens aan deze setup te beginnen.<br>
Clone vervolgens het project:
```bash
git clone git@github.com:SELab-2/Dr-Trottoir-5.git
cd Dr-Trottoir-5
cd backend
```
Maak nu een virtual environment aan om de benodigde pakketten op te installeren:
```bash
virtualenv2 --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
```

#### Database en Gmail instellen
Vul het bestand **backend/.env.example** aan met jouw database en Gmail gegevens.
Naast het Gmail adres moet er ook een [app-wachtwoord](https://support.google.com/mail/answer/185833?hl=nl)  aangemaakt worden. 

Nu moeten deze gegevens alleen nog maar opgeslagen worden als een env bestand:

```bash
cp backend/.env.example backend/.env
```

#### Backend opstarten
Om de django server lokaal op te starten kan het volgende commando worden gebruikt:
```bash
python manage.py runserver
```

Deze zal nu bereikbaar zijn op `http://127.0.0.1:8000`.