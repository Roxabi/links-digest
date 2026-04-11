---
title: "Jour 3 : Mon homelab IA tourne. 23 mod\u00e8les locaux. Z\u00e9ro cloud. Et j\u2019ai tout f..."
source: "https://x.com/iamsupersocks/status/2033149337820168224?s=46"
date: 2026-03-16
tags: ["AI", "Homelab", "Local LLM", "Ryzen AI", "Ollama"]
platform: x
author: "@iamsupersocks"
summary: "A non-engineer documents building a local AI inference station in three days using a Ryzen AI mini PC, successfully running 23 models while optimizing VRAM management and storage."
---
Jour 3 : Mon homelab IA tourne. 23 modèles locaux. Zéro cloud. Et j’ai tout fait en 3 jours sans jamais avoir vraiment touché Linux avant. 

Samedi (hier) était intense : levé tôt, pas trop mangé, à 19 h toujours debout, pas mal de café et une machine qui ronronne jusqu’au bout de la nuit (j’ai toujours un œil ouvert quand je dors depuis qu’elle trône dans mon salon).

Le contexte :  
GMKtec EVO-X2. Ryzen AI MAX+ 395. 96 Go de mémoire unifiée partagée entre CPU et GPU. 143 Go de VRAM exploitable. 2 To de SSD.

Jour 1 : installation d’Ubuntu, Open WebUI, Ollama et des premiers modèles.  
Jour 2 : Premier benchmark de l'engin.  
Jour 3 : Tout a failli casser, tout a été réparé, et la machine est devenue une vraie station d’inférence.

Non, je ne suis pas ingénieur système. Je suis de formation ingénieur en énergétique, je fais du business development dans l'industrie. Mon quotidien c'est la récupération de chaleur et l'approvisionnement énergétique y compris pour des datacenters. Deux mondes qui convergent : décentraliser l'énergie, décentraliser le compute. Faire tourner des modèles en local plutôt que dans le cloud, c'est le même raisonnement que produire son électricité plutôt que de dépendre du réseau. 

Mon meilleur allié pour tout construire ? Claude Code, directement sur la bécane.

Télécharger 450 Go de cerveaux artificiels.

La journée a commencé par du téléchargement massif : pas un modèle, pas deux, vingt. De 4B à 72B. Abliterated, MoE, reasoning, créatifs. Une vingtaine au total, tous en GGUF (format optimisé pour faire tourner les LLM en local, avec différents niveaux de compression selon le compromis qualité/taille), téléchargés en parallèle depuis Hugging Face.

Les 70B : une heure. Pendant que ça tourne et que Claude implémente, tu fais autre chose. 450 Go de cerveaux artificiels.

Tout piloté depuis Claude Code. Je tape « télécharge-le stp » et ça part. Un peu de recherche et de réflexion en parallèle. Deux trois coups sur sa caboche et on test.

Ollama décharge automatiquement les modèles après 5 min d’inactivité. llama-server, non : le modèle reste en VRAM jusqu’à ce que tu tues le process manuellement. Sauf que j’ai besoin de llama.cpp pour les gros modèles que ma config Strix Halo peut gérer mais qu’Ollama refuse de charger. llama.cpp tape directement dans la mémoire unifiée. Un 70B en Q4 = 40 Go bloqués pour rien. J’ai implémenté un truc sympa : le lazy proxy. Charger à la demande, libérer la VRAM. Je ne sais pas encore si c’est optimal, mais on bricole, on teste ; la machine n’a pas encore assez fumé pour que je m’inquiète.

Ollama ajoute une couche d’abstraction qui bride la machine. Nemotron 120B ? Il tourne sur llama.cpp. Ollama ne le charge même pas.

D’où le proxy : il donne à llama-server le même comportement de déchargement automatique qu’Ollama nativement. Il s’intercale entre Open WebUI et llama-server. 

Open WebUI, c’est mon interface chat pour jouer avec les modèles à la main, un peu comme ChatGPT avant de passer en API.

Pour les curieux (j'en parlerai dans un post séparé):
> Strix Halo : architecture AMD où CPU et GPU partagent la même mémoire. Pas de carte graphique séparée avec sa petite VRAM. 96 Go d’un bloc, accessibles au GPU. C’est comme ça qu’un Nemotron 120B tient sur un mini PC.

Idée → script → service → fonctionnel. Temps total : quelques heures. Merci Claude Code.

L’import Ollama : la duplication imprévue

Le piège : Ollama copie chaque fichier dans son propre storage (~/.ollama/models/). Résultat : duplication complète. 450 Go × 2 = 900 Go. Sur 2 To, ça commence à piquer.

Solution : rationaliser. On garde Ollama comme système principal (23 modèles). Le lazy proxy ne sert plus que pour 4 modèles aux quantisations spéciales qu’Ollama n’a pas et où llama.cpp apporte de meilleures perfs. Pour la phase de test, c’est parfait.

Optimisation de la bécane :

Il existe un wiki communautaire dédié à cette puce : http://strixhalo.wiki. Écrit par des gens qui ont la même machine et qui ont passé des semaines à tester ce qui marche ou pas. Tout le monde est encore en phase d’expérimentation ; partager les bonnes pratiques fait sens.

Claude Code a lu le wiki en entier, comparé avec ma config, identifié ce qui manquait et appliqué les réglages un par un. Concrètement :

- GPU plus réactif : paramètres d’économie d’énergie désactivés → moins de latence, réponses plus fluides. 
 
- Mémoire mieux exploitée : compression du cache de contexte → même qualité, moins de place occupée, plus de modèles ou contextes longs possibles.
  
- Kernel Linux mis à jour : meilleur support de la puce + nettoyage des anciennes versions.  

- Gros modèles ne timeout plus : timeout étendu (un 70B qui met 45 s à charger faisait planter la connexion).

Je n’ai pas compris chaque ligne changée. Mais je sais vérifier que ça marche, comparer avant/après, voir la différence. Et c’est ça qui compte quand on apprend en faisant, en itérant. Y'a que ceux qui font rien qui font pas d'erreurs. Et bien sûr j’ai pris le temps de lire le wiki et d'autres ressources : pas mettre la charrue avant les bœufs.

Résultat : prompt processing sensiblement plus rapide, longs contextes mieux gérés, bande passante mémoire optimale.

Tests manuels : maths, physique, raisonnement. Résultats impressionnants. Chaque modèle testé individuellement, de 4B à 72B.

On a fait tourner les modèles. Pas juste « est-ce que ça charge », mais « est-ce que ça pense ». Beaucoup de jours de test à venir.

Constat : les 70B raisonnent correctement sur des problèmes complexes. Les 27-35B tiennent bien même compressés à 25% de leur taille originale (ce qu'on appelle Q4_K_M -> une méthode de compression qui réduit le poids du modèle en gardant l'essentiel de la qualité). Les 8B sont utilisables pour des tâches simples, du routing, de l'exécution de compétences : des agents. Mais Qwen est étonnamment performant en 9B et même 4B ; sur certaines tâches, on se demande pourquoi charger un 70B.

Et c’est là que le post de LottoLabs que j'ai partagé hier sur X prend tout son sens :

Qwen 3.5 4B est capable d'exécuter 40 tool calls construits par un 27B. Sans broncher avec les bons skills. Sur 3 Go de VRAM.

Le modèle n’a pas besoin d’être un demi-dieu de l'intelligence et d'être chargé comme un boeuf. Il a besoin de bonnes compétences à exécuter. Le gros modèle écrit les skills. Le petit les appelle. Un dev senior qui code les fonctions, un junior qui les utilise.

Le LLM devient chef d’orchestre, plus cerveau universel.

Et sur une machine avec 96 Go de mémoire unifiée ? Tu fais tourner plusieurs modèles en même temps. Le gros qui réfléchit et planifie, les petits qui exécutent chacun leur tâche. Une vraie équipe d'agents locaux qui bossent en parallèle. Et quand la machine principale est occupée, tu décharges sur ce que t'as sous la main : un vieux PC portable, un Raspberry Pi, un téléphone qui traîne dans un tiroir. 3 Go de RAM suffisent pour un 4B qui exécute des skills. Tout ce qui a un processeur devient un nœud de calcul.

Hermes Agent : la découverte, le début du vrai build

Tout ce qui avait été fait sur OpenClaw sous Windows a été migré ici et maintenant on fait mumuse avec Hermes pour comparer. Début de la phase « pas juste faire tourner des modèles, mais faire tourner des agents ». Le fine-tuning arrive. Et avec lui, la plongée dans les entrailles des modèles : comprendre ce qu'on compresse, ce qu'on perd, ce qu'on peut spécialiser. Pour l'instant on fait tourner et on teste. Bientôt on adapte.

La suite au prochain épisode. Pas de jour 4 aujourd'hui : quelques rendez-vous B2B pour des apps que je développe à côté, et la semaine prochaine est chargée en déplacements. Je vais me concentrer sur le build et les tests, et partager au fil de l'eau. L'idée c'est aussi de monter un wiki sur mon site (lien en bio) pour capitaliser tout ça. Les tweets c'est bien pour raconter en live. Mais faut pas laisser mourir l'info et l'expérience dans un feed que personne ne scrollera dans deux semaines.

Ce que les puristes ne comprennent pas

Je publie tout. Le parcours, les erreurs, les trucs qui cassent, les commandes qui foirent. Et pas que le homelab : l'IA en général, les modèles, l'écosystème, les outils. Je suis à fond dans l'apprentissage et je cache rien du processus.

Deux types de réactions :

Les puristes : commentaires « bienveillants » qui virent au blocage dès qu'ils voient que tu avances, que tu build, que ça tourne. Sympa les gars. Mais tout le monde n'a pas 10 ans de Linux et de sysadmin derrière soi. C'est en pratiquant qu'on apprend, pas en attendant la permission. Ne sous-estimez pas un néophyte déterminé avec Claude dans la poche. Quand j'étais en bac pro, ce même genre de personne dans mon domaine ne m'imaginait pas devenir ingénieur et bosser à l'international à l'époque je comprenais à peine comment un fluide circulait dans une tuyauterie. Et pourtant.

Les vrais : ceux qui lisent, répondent, engagent, partagent un tip, un lien. L’effort qu’ils mettent à aider un inconnu sur internet force le respect. Merci. 

Et le troisième acteur : Claude. Mon premier gosse s’appellera Claude si ça continue.

Pas Claude le chatbot (bon je le kiff bien aussi celui là). Mais je parle bien de Claude Code. Le terminal. L’outil qui te permet de piloter une machine Linux complète depuis un prompt. Télécharger des modèles. Compiler. Debugger. Configurer des variables GPU. Optimiser un kernel.

« En faisant » en 2026, ça veut dire avec un LLM qui comprend ce que tu veux et qui le fait.

La facilité est déconcertante. Tu décris ce que tu veux en français approximatif, avec des fautes. Et ça marche.

C'est le nouveau workflow pour les grands bricoleurs que nous sommes.

Les prochains jours : prendre le temps de tester Hermes Agent. Benchmarker les modèles (classique et à la mano) pour voir lesquels me correspondent vraiment. Migrer mes services cloud en local (n8n, Supabase et d'autres). Faire tourner mes scripts existants pour voir ce que ça donne sur une appli concrète. Tester le coding. Et surtout : monter une vraie architecture d'agents : les 4B/9B qui exécutent, un 27B ou plus gros qui orchestre. 

Bref on bricole, on kiff, on va rentrer dans le dur avec les outils adéquate pour bien comprendre la théorie à présent.