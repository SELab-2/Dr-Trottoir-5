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

## Het installeren van de frontend
```
npm install
```

### Het compileren met hot-reload voor locale development
```
npm run serve
```

### Het compileren met minification voor production environments
```
npm run build
```

### Run your unit tests
```
npm run test:unit
```

## Aanvullende info

De frontend heeft code voor een [PWA](https://web.dev/learn/pwa/) dit is enkel beschikbaar indien er gecompileerd is voor production environments.

