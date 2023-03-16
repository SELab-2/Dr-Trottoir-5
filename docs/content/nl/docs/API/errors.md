---
categories: ["api", "error"]
tags: ["api", "examples"]
title: "API errors"
linkTitle: "API errors"
date: 2023-03-14
description: >
  Deze pagina toont voorbeelden van hoe de fouten in de api worden teruggestuurd
---

## Algemene fouten
De algemene fouten van de api worden met deze structuur terug gestuurd:

```json
{
  "errors": [
    {
      "message": "Building does not exist"
    },
    {
      "message": "You do not have access to this"
    }
  ]
}
```

## Form input fouten
De fouten indien er verdeerde formulier invoer gegeven wordt volgen deze structuur:

```json
{
  "errors": [
    {
      "message": "email bestaat al",
      "field": "email"
    },
    {
      "message": "Het wachtwoord is niet lang genoeg",
      "field": "wachtwoord"
    }
  ]
}
```
