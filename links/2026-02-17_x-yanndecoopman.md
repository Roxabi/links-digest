---
title: "C'est un sujet récurrent la gestion de la « mémoire » (au sens persistance, p..."
source: "https://x.com/yanndecoopman/status/2023657474994151769?s=46"
date: 2026-02-17
tags: ["memory management", "Obsidian setup", "AI agents", "semantic indexing", "knowledge sharing"]
platform: x
author: "@YannDecoopman"
summary: "The author shares an effective OpenClaw memory management setup using Obsidian and Voyage AI for semantic indexing and automated knowledge propagation between agents."
---
C'est un sujet récurrent la gestion de la « mémoire » (au sens persistance, pas RAM) dans OpenClaw. 

Je suis moi même surpris positivement par son efficacité  donc je partage mon setup :

• J'utilise Obsidian (fichiers md légers et liés logiquement ) et mes agents ont dans leur http://AGENTS.md l'instruction de toujours tenir le répertoire à jour avec le résultat de leurs veilles et travaux 

• Chaque agent poste son bilan quotidien dans un format standardisé. Très utile pour les boucles de feedback et d'amélioration

• Le répertoire Obsidian est indexé par Voyage AI (l'API coûte quasi rien). C’est un tool recommandé par Anthropic qui fait de l’indexation sémantique, donc synonymes, contexte, pas juste du keyword matching

• Quand un agent cherche un truc , il indexe la mémoire pour tous les autres la connaissance se propage entre agents automatiquement

• Les PDF déposés dans le vault sont transformés en .md pour faciliter la recherche

Disclaimer : ne stockez PAS vos clés et accès dans le vault car ça se retrouve indexé par Voyage AI. Credentials dans un gestionnaire dédié (1Password, etc.)