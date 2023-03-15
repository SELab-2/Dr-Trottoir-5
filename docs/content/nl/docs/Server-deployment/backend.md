---
categories: ["Deployment"]
tags: ["backend", "database"]
title: "Backend"
linkTitle: "Backend"
date: 2023-03-11
description: >
    Hoe start je de backend op
---

#### Environment instellen
Maak een python environment aan om de nodige pakketten op te installeren:
```bash
cd backend
python3.11 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### Django instellen
Om te beginnen zal django correct moeten worden ingesteld.<br>
Daarvoor zullen we eerst de correcte gegevens voor de database uit [de vorige stap]({{< relref "/docs/server-deployment/database#database-aanmaken" >}}) invullen in het bestand **backend/.env**.
Vul deze als volgt in:
```bash
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
Open hierna het bestand **backend/settings.py** en wijzig hierin ALLOWED_HOSTS op de volgende manier: ['localhost', 'server_domein', 'server_ip'].

Laat django tot slot de benodigde databanktabellen aanmaken:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Nginx instellen
Om de backend API en mogelijkse media en statische content publiek bereikbaar te maken zal het nginx configuratiebestand bewerkt moeten worden:
```bash
sudo vim /etc/nginx/sites-available/default
```
Hier zal in het server block het volgende moeten worden toegevoegd:
```bash
location /static/ {
    alias /var/www/html/static/;
}
location /media/ {
    alias /var/www/html/media/;
}
location /api {
    include proxy_params;
    proxy_pass http://unix:/run/gunicorn.sock;
}
```

Dit zal de backend API bereikbaar maken op de /api URL gebruikmakend van gunicorn, een server bovenop django die de backend geschikter maakt op een productieserver.

#### Gunicorn instellen
Als laatst zal dan ook gunicorn ingesteld moeten worden opdat deze de django API op kan starten.
Hiervoor beginnen we met het aanmaken van een socket **/etc/systemd/system/gunicorn.socket** met de volgende inhoud:
```bash
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Vervolgens maken we een service aan die de applicatie zal gaan draaien. Maak hiervoor het bestand **/etc/systemd/system/gunicorn.service** aan met de volgende inhoud:
```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=<gebruikersnaam>
Group=www-data
WorkingDirectory=/home/<gebruikersnaam>/Dr-Trottoir-5/backend
ExecStart=/home/<gebruikersnaam>/Dr-Trottoir-5/backend/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          backend.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start en activeer nu de socket om de backend setup te voltooien:
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```