# TP secure chat

## Prise en main

1. Comment s'appelle cette topologie ?

*C'est une topologie client/serveur.*

2. Que remarquez vous dans les logs ? 

*On remarque que chaque action est incrite dans les logs. On y voit que "client_1" envoie un message au serveur, et que ce dernier transmet le message aux autres clients connectés au serveur, dans mon cas "client_2".*

*De plus, chaque message est visible en clair depuis les logs du server.*

3. Pourquoi est-ce un problème et quel principe cela viole t-il ?

*C'est un problème car n'importe quel message est lisible en clair et que cela viole le principe de confidentialité.*

4. Quelle solution la plus **simple** pouvez-vous mettre en place pour éviter cela ? Détaillez votre réponse.

*Pour cela, on peut mettre un système de chiffrement afin de rendre les messages illisibles sans la clé de déchiffrement. De plus, il faut que chaque client puisse s'authentifier avant de se connecter au serveur.*


