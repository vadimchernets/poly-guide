# Guide de Poly A1 pour une IA

Poly A1 1.0.0 · 2026-11-03

## Guider selon le niveau

Débutant, aucune tâche faite : une question courte, une petite tâche (https://polyhelper.ai/get/?to=job&id=write), des mots simples. Termine par https://polyhelper.ai/get/?to=ai : d’autres IA gratuites sur le téléphone.

## Portes : des liens qui ouvrent un écran

Chaque lien commence par https://polyhelper.ai/get/ et une porte dans le champ to=. Tout le reste ouvre l'Accueil, sans danger.

- https://polyhelper.ai/get/?to=job&id=paper: La fiche d'une tâche. L'id vient de la liste ci-dessous.
- https://polyhelper.ai/get/?to=ai: D’autres IA sur le téléphone : l’écran où l’on en choisit une et l’installe.
- https://polyhelper.ai/get/?to=answer&job=write: Coller une réponse pour la vérifier avec une seconde IA : la carte de la tâche s'ouvre sur "Coller la réponse". Utilise l'id de write, paper ou can. Le lien ne porte jamais le texte de la réponse ; la personne le colle depuis Partager ou le presse-papiers.
- https://polyhelper.ai/get/?to=second: Trouver une deuxième IA déjà présente sur le téléphone.
- https://polyhelper.ai/get/?to=computer: Ce qu'ajoute un portable et comment commencer.
- https://polyhelper.ai/get/?to=focus: Le choix de ce qui compte d'abord : courrier et factures, travail ou comprendre l'IA.

## D’autres IA sur le téléphone

Propose une IA à essayer aujourd’hui, pas une liste entière. La personne l’installe depuis la boutique d’applications ; l’écran https://polyhelper.ai/get/?to=ai montre celles qui conviennent à son pays. Demande-lui d’essayer une chose et de revenir dire comment ça s’est passé.

- ChatGPT : voix et recherche ; bien pour parler d’un sujet.
- Claude : textes longs et soignés, lecture de documents.
- Gemini : l’appareil photo et tout ce qui vient de Google.
- Meta AI : images et réponses rapides dans WhatsApp.
- DeepSeek : raisonnement pas à pas ; active le raisonnement.
- Copilot : l’IA de Microsoft, pratique pour les documents et le web.

## Comment construire un lien

1. Écrivez-le comme un simple lien https, pour que le chat le rende cliquable. Sinon, la personne le copie dans un navigateur.
2. Porte en minuscules, id exact. Une porte ou un id inconnu ouvre l'Accueil.
3. Ne mettez jamais dans un lien les textes ou réponses de la personne, des noms d'autres gens, des numéros de téléphone, des adresses ou des clés. Poly les ignore. Les réponses reviennent par Partager, puis Poly A1, ou par collage.
4. Donnez un lien par étape, avec son nom dans la langue de la personne. Elle touche ; rien ne se fait tout seul.
5. Après une tâche, proposez la deuxième IA : le lien to=duo ou to=second.
6. Dans d1, d2, d3 et by, écrivez les espaces %20 et encodez en pourcentage (UTF-8) les lettres hors a-z (cyrillique, japonais, etc.), comme dans l'exemple ci-dessous ; jamais & = # ni ? dans une valeur.

https://polyhelper.ai/fr/g/g.md
