---
title: "Incroyable ce repo. X depuis le terminal."
source: "https://x.com/iamsupersocks/status/2033681113059643608?s=46"
date: 2026-03-17
tags: ["clix", "X", "CLI", "automation", "MCP"]
platform: x
author: "@iamsupersocks"
summary: "The author reviews \u0027clix\u0027, a CLI tool for controlling X via terminal using browser cookies, and outlines plans to automate their AI news curation and publishing pipeline."
---
Incroyable ce repo. X depuis le terminal.

Accès complet à X depuis le CLI. Pas d'API, pas d'OAuth, juste des cookies de navigateur et c'est parti.

On parlait MCP vs CLI dans un long pavé qui en a fait crisser plus d'un par sa longueur. On y est.

clix : X sans l'API

Setup en quelques minutes via Claude Code sur ma machine Ubuntu. Je peux maintenant piloter @llmgram sans passer par l'API X qui s'est vachement durcie et coûte bien trop cher pour ce que j'en fais.

Le principe : clix utilise l'authentification par cookies de ton navigateur. Tu te connectes à X normalement, clix auth extrait les cookies, et tu as un accès complet. Lecture, écriture, DMs, listes, bookmarks : tout.

C'est à mes risques et périls. Mais le compte est bien marqué "automatisé par la super chaussette" et je ne vais pas en abuser. Pas d'objectifs commerciaux également. Juste de la vieille. 

Le repo : https://github.com/spideystreet/clix

Ce que clix sait faire

Lire
clix feed — ta timeline (for-you ou following)
clix search "query" — rechercher des tweets
clix trending — tendances
clix tweet  — voir un tweet + thread
clix user  — profil d'un utilisateur
clix bookmarks — tes bookmarks
clix dm inbox — tes DMs

Agir
clix post "texte" — poster (avec images, reply, quote)
clix delete  — supprimer un tweet
clix like/unlike  — liker
clix retweet/unretweet  — retweeter
clix bookmark/unbookmark  — bookmarker
clix follow/unfollow  — follow
clix block/unblock  — bloquer
clix mute/unmute  — muter
clix dm send  "texte" — envoyer un DM
clix download  — télécharger les médias
Programmer
clix schedule "texte" --at  — programmer un tweet
clix scheduled — voir les tweets programmés

Listes
clix lists — tes listes
clix lists create/delete/members/add-member/remove-member
MCP — clix mcp lance un serveur MCP avec 38 outils, connectable à Claude ou tout client MCP.

L'objectif : AI Signal automatisé sur X

L'idée c'est d'aller plus loin sur la veille du signal AI que j'ai mise à disposition et que je vous ai dévoilée il y a quelques jours.

Pour ceux qui ont raté : https://iamsupersocks.com/veille.html

Toutes les heures, le système va récupérer 5 à 10 articles sur les 70+ sources de référence qui viennent de blogs, RSS et X. J'ai une gateway OpenClaw dédiée sur ce signal. 100% opérationnel. Base de données en local et site en HTML/CSS/JS, rien de compliqué. Analyse grok via API pour sortir les vrais signaux. Encore à peaufiner. 

Et maintenant le AI Signal est dispo en .md pour vos agents : https://iamsupersocks.com/ai-signal.md. Actu IA en temps réel, faites-en ce que vous voulez. C'est tout frais, il y a sûrement des coquilles ; soyez indulgents, on va améliorer ça. Pour nous, pour vous et pour nos agents.

L'idée avec clix : sortir les articles les plus pertinents et les publier sur X de manière concise avec l'info importante sans le bruit. Sommaire + analyse critique.

J'aime bien lire X, ce sera un bon moyen d'avoir un compte fiable avec du contenu sourcé et vérifié.

X c'est mon carnet de bord sur le pouce. Le site Supersocks sera celui sur la durée avec quelques expérimentations.

Le pipeline : veille automatique → sélection par pertinence → publication concise sur X via clix → tout piloté depuis le terminal.  Build en cours.

Un agent scrute, trie, et publie le signal utile. Pas du spam de la curation automatisée, sourcée, avec analyse critique.

Merci @spideystreet pour cette jolie brique