---
categories: ["Deployment"]
tags: ["docker", "frontend", "backend", "database", "docs"]
title: "docker"
linkTitle: "docker"
date: 2023-03-11
description: >
    Hoe je de applicatie met docker kan opstarten
---
# Project Opstarten met Docker Compose

> Instructies voor het opstarten van het project met behulp van Docker Compose.
> Dit geeft je een production environment

## Inhoudsopgave

- [Inleiding](#inleiding)
- [Vereisten](#vereisten)
- [Aanpassen van .env-bestanden](#aanpassen-van-env-bestanden)
- [Project starten](#project-starten)
- [Controleren van de applicatie](#controleren-van-de-applicatie)
- [Aanvullende informatie](#aanvullende-informatie)
- [Herstarten na changes](#herstarten-na-changes)

## Inleiding

Dit document bevat instructies voor het opstarten van een project dat uit 3 delen bestaat met behulp van Docker Compose. Het project is opgebouwd uit de volgende delen:

1. Frontend: Vue.js-applicatie
2. Backend: Django-applicatie
3. Docs: Hugo docsy documentatie-applicatie

Elk deel van het project heeft een bijbehorend .env-bestand dat aangepast moet worden met de juiste configuratie voordat het project gestart kan worden.

## Vereisten

Voordat je het project kunt starten, zorg ervoor dat de volgende software geïnstalleerd is op je systeem:

- Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Aanpassen van .env-bestanden

Voor elk deel van het project zijn er .env of config bestanden aanwezig die aangepast moeten worden met de juiste configuratie.

1. Frontend:
    - Navigeer naar de frontend-map: `cd frontend`.
    - Dupliceer het voorbeeldbestand `.env.template` en hernoem het naar `.env.production.local`.
    - Open het `.env.production.local`-bestand en pas de configuratie aan volgens je eigen omgeving.

2. Backend:
    - Navigeer naar de backend-map: `cd backend/backend`.
    - Dupliceer het voorbeeldbestand `.env.example` en hernoem het naar `.env`.
    - Open het `.env`-bestand en pas de configuratie aan volgens je eigen omgeving.

3. Docs:
    - Navigeer naar de database-map: `cd docs`.
    - Open het `config.toml`-bestand en pas de configuratie aan volgens je eigen omgeving.

## Project starten

1. Ga terug naar de hoofdmap van het project: `cd ..`.
2. Start het project met behulp van Docker Compose: `docker-compose up -d`.
3. Docker Compose zal nu alle containers bouwen en starten op basis van de configuratie in het `docker-compose.yml`-bestand.
4. Wacht tot het opstarten is voltooid en controleer of alle containers succesvol zijn gestart.

## Controleren van de applicatie

Om te controleren of de applicatie correct is gestart, volg je deze stappen:

1. Open een webbrowser en navigeer naar de frontend-applicatie op `http://localhost:8080`.
2. Als alles correct is geconfigureerd, zou je de frontend van de applicatie moeten zien.
3. Test de functionaliteit van de applicatie en zorg ervoor dat alles naar behoren werkt.
4. Open een webbrowser en navigeer naar de documentatie applicatie op `http://localhost:1313`.

## Aanvullende informatie

- Voor meer informatie over het project, bekijk de README van het project in de repository.
- Raadpleeg de documentatie van de respectieve delen (frontend, backend, database) voor gedetailleerde instructies over het configureren en ontwikkelen van die delen.
- Op `http://localhost:8081` kan je een admin panel voor de databank vinden waar je gemakkelijk rechtstreekse queries kan uitvoeren op de database. De default login en ww hiervan zijn de waarden die in de `backend/backend/.env` file staan.

## Herstarten na changes

Indien je bestanden veranderd hebt en 1 deel of alle delen van de applicatie wil herstarten kan je dit doen met:
```bash
docker-compose up --build
```
Om alles te herstarten en opnieuw te builden.
```bash
docker-compose up --build <onderdeel>
```
Om maar 1 van de onderdelen opnieuw te builden en te herstarten. Waarbij <onderdeel> 1 van deze is:
- backend
- frontend
- docs
- database
