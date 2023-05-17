---
categories: ["api", "planning"]
tags: ["api", "examples", "planning"]
title: "Planning API"
linkTitle: "Planning API"
date: 2023-03-14
description: >
  Deze pagina geeft meer info over de verschillende **planning** endpoints
---
## Planning endpoints

Hier kan u uitleg vinden over alle endpoints die met de planning te maken hebben.

### buildingpicture/

Geeft via een GET request alle buildingpicture objecten terug. Deze horen bij een infoperbuilding en bevatten een link naar een foto.

### buildingpicture/\<int:pk\>/
### infoperbuilding/
### infoperbuilding/\<int:pk\>/
### weekplanning/\<int:year\>/\<int:week\>/
### dagplanning/\<int:year\>/\<int:week\>/\<int:day\>
### dagplanning/\<int:pk\>/
### dagplanning/\<int:year\>/\<int:week\>/\<int:pk\>/status/
### dagplanning/\<int:year\>/\<int:week\>/\<int:pk\>/pictures/
### studenttemplates/find/planning/\<int:pk\>/
### studenttemplates/rondes/\<int:year\>/\<int:week\>/\<int:day\>/\<int:location\>/
### studenttemplates/
### studenttemplates/\<int:template_id\>
### studenttemplates/\<int:template_id\>/rondes/
### studenttemplates/\<int:template_id\>/rondes/\<int:ronde_id\>
### studenttemplates/\<int:template_id\>/rondes/\<int:ronde_id""\>/dagplanningen/
### studenttemplates/\<int:template_id\>/dagplanningen/\<int:dag_id\>/
### studenttemplates/\<int:template_id\>/dagplanningen/\<int:dag_id\>/eenmalig/
