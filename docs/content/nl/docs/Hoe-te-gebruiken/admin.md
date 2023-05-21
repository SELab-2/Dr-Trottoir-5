---
categories: ["how to", "admin"]
tags: ["UI", "UX", "docs", "how to", "admin"]
title: "admin"
linkTitle: "admin"
date: 2023-21-05
description: >
  Hoe gebruik je de applicatie als een admin
---

# Admin

## Inhoudstafel

- [Dashboard](#dashboard)
  - [Ronde info](#ronde-info)
- [Studenten Templates](#studenten-templates)
  - [Aanmaken](#aanmaken)
  - [Aanpassen](#aanpassen)
    - [Rondes](#rondes)
    - [Dagplanning](#dagplanning)
- [Afval Templates](#afval-templates)
  - [Aanmaken](#aanmaken-1)
  - [Aanpassen](#aanpassen-1)
    - [Vuilnisbakken](#vuilnisbakken)
    - [Gebouwen](#gebouwen)
- [Locaties](#locaties)
- [Rondes](#rondes)
- [Gebouwen](#gebouwen-1)
- [Studenten](#studenten)
- [Syndici](#syndici)
- [Email Templates](#email-templates)

## Dashboard

Op de front pagina voor admins bevat alle plannings die momenteel actief zijn en al dan niet ingepland op een bepaalde dag.

### Ronde info
Na het klikken op het info icoon naast een ronde krijgt de admin een overzicht te zien over die bepaalde ronde.
- Of die al dan niet al klaar is.
- Welke studenten er mee bezig zijn.
- De opmerkingen indien er zijn.
- Uitgebreide info over de gebouwen.

De specifieke ronde kan op dit scherm ook aangepast worden. De velden die op dit punt nog aan te passen zijn, zijn:
- De studenten voor de ronde
- Het start en eind uur van de ronde

## Studenten Templates

Studenten templates zijn vaste sets van rondes op 1 locatie waar de studenten altijd gelijk blijven. Deze templates zijn net zoals de [Afval Templates](#afval-templates) voor even en/of oneven weken.

### Aanmaken
Bij het aanmaken van een Studenten Template wordt een naam verwacht, de locatie voor deze template en de start en eind uren die meestal gebruikt gaan worden.

### Aanpassen
Na het aanmaken van de template kan die aangepast worden. Enkel onderstaande velden kunnen aangepast worden.
- Naam
- Startuur
- Einduur

Bij het aanpassen kunnen rondes toegevoegd worden aan de template.

#### Rondes

Elke ronde die gemaakt is in [Rondes](#rondes-1) kan meerdere keren toegevoegd worden.

Elke ronde heeft voor elke dag van de week, startend op zondag, een lege dagplanning.

#### Dagplanning
Bij elke dag in de dagplanning kunnen er 1 of meerdere studenten aangewezen worden om op die dag van de week die ronde te doen.
Een dag kan ook een 2de keer toegevoegd worden indien dit gewenst is en kan zelfs dezelfde uren krijgen als 1 die al bestaat.

Elke dag heeft dezelfde start en eind uren als de template maar die kunnen aangepast worden.

## Afval Templates
 
Deze templates volgen hetzelfde principe als de [Studenten Templates](#studenten-templates).

### Aanmaken
Bij het aanmaken van de templates hebben ze elk een locatie, naam en even/oneven weken.

### Aanpassen
Na het aanmaken van een lege template kunnen er gebouwen en vuilnisbakken toegevoegd worden.

#### Vuilnisbakken
Bij elke template moet je de vuilnis ophaling toevoegen per dag van de week. Welk type en tussen welke uren het buiten moet staan.

#### Gebouwen
Bij elke template kunnen de gebouwen die deel gaan uitmaken van deze template toegevoegd worden.
Op elk gebouw dat toegevoegd is kan men klikken en een permanente of eenmalige container selectie toepassen.

## Locaties

Hier heeft men de oplijsting van alle locaties.

Ze kunnen verwijderd worden en er kunnen nieuwe gemaakt worden.

## Rondes

Hier kan men een oplijsting zien van alle rondes in de applicatie. Ze kunnen aangepast of verwijderd worden.
Er kunnen er ook nieuwe gemaakt worden.

Een ronde bestaat uit:
- Een naam
- Locatie
- Lijst van gebouwen



## Gebouwen

Hier kan men een lijst van alle gebouwen in het systeem zien.
Elk gebouw heeft:
- Naam
- Adres
- Efficiëntie
  - Dit is de efficiëntie van het gebouw t.o.v. kost
  - Dit is een work in progress, werkt nog niet
- Handleiding
- Document status
  - Dit is de status van de Handleiding momenteel.

Als een gebouw aangepast wordt kan:
- Naam
- Adres
- Klanten nummer
- Handleiding status
- Handleiding

Aangepast worden, de locatie van een gebouw kan niet aangepast worden.
## Studenten

Op deze pagina kan men een lijst zien van alle studenten die momenteel een account hebben. De info over elke student kan bekeken worden en aangepast worden.

Vanboven links is er een knop `Studenten registreren`. Dit is waar alle accounts die geregistreerd zijn maar nog geen rol hebben gekregen staan.
Daar kan elke user de juiste rol krijgen.

Een syndicus die een account aanmaakt gaat ook in deze lijst terecht komen tot die juiste `syndicus` rol heeft gekregen.

## Syndici

Hier kan men een lijst van alle Syndici terugvinden en voor elke syndicus aanpassen voor welke gebouwen ze verantwoordelijk zijn.

Syndici kunnen hier ook verwijderd worden.

## Email Templates

Om het gemakkelijk te maken om emails te versturen kunnen templates aangemaakt worden hiervoor. Deze kunnen argumenten krijgen die erna ingevuld kunnen worden.

Een argument kan genoteerd worden als `#argument#` met 2 hashtags rond de naam van het argument. Bij de preview tab staan de argumenten in het **vet**
