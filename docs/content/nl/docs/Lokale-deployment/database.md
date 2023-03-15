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

#### Postgresql installeren
Download en installeer [postgresql](https://www.postgresql.org/download/) op uw lokale machine.<br>
Zorg er vervolgens voor dat deze server lokaal draait - dit kan bijvoorbeeld bevestigd worden door met [pgadmin](https://www.pgadmin.org/download/) proberen te verbinden met _localhost_. Maak nu eventueel een databank en/of gebruiker aan in psql of pgadmin, zoals hieronder getoond wordt.

![](/docs/lokale-deployment/pgadmin.png)