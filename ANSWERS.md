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


## Chiffrement

1. Est ce que urandom est un bon choix pour de la cryptographie ? Pourquoi ?

*urandom est un bon choix pour la cryptographie car l'aléatoire est généré selon du bruit.*

2. Pourquoi utiliser ses primitives cryptographiques peut être dangereux ?

*Le principal danger est l'assemblage des différentes primitives cryotographiques. Chaque primitive, ewt faite pour réaliser une opération précise, et par conséquent répondre à une seule propriété.*

3. Pourquoi malgré le chiffrement un serveur malveillant peut il nous nuire encore ?

*Un serveur malveillant peut encore nuire, en altérant les messages échangés.*

4. Quelle propriété manque t-il ici ?

*La propriété manquante ici est l'intégrité, c'est-à-dire qu'il n'y a pas de manière de vérifier si les données ont été altérées.*


## Authenticated Symetric Encryption

1. Pourquoi Fernet est moins risqué que le précédent chapitre en terme d'implémentation ?

*Fernet est moins risqué, car il implémente plusieurs fonctionnalités qui permettent de subvenir aux différentes propriétés de la cybersécurité.*

2. Un serveur malveillant peut néanmoins attaqué avec des faux messages, déjà utilisé dans le 
passé. Comment appel t-on cette attaque ?

*Cette attaque s'appelle la replay attack, un attaquant vient s'interposer entre deux personnes. Il intercepte un message envoyé, et le réémet vers la personne destinatrice.* 

3. Quelle méthode simple permet de s'en affranchir ?

*La méthode de l'utilisation d'un mot de passe unique permet de s'affranchir de ce problème car un mot de passe unique ne peut être utilisé qu'une seule fois. De plus, on peut utiliser l'horodatage, car un message horodaté ne peut pas être rejoué une seconde fois.* 

## TTL

1. Remarquez vous une différence avec le chapitre précédent ?

*Je ne remarque aucune différence en utilisant les fonctions encrypt_at_time et decrypt_at_time.*

2. Maintenant soustrayez 45 au temps lors de l'émission. Que se passe t-il et pourquoi ? 

*Les messages ne peuvent pas être déchiffrer car le TTL est trop faible. Le TTL étant expiré, le message ne peut pas être déchiffré.*

3. Est-ce efficace pour se protéger de l'attaque du précédent chapitre ? 

*Ce n'est pas suffisament efficace pour se protéger de ce genre car rien n'empeche un attaquant de s'immiscer au milieu, mais cela peut prévenir en cas d'intrusion.*

4. Quelle(s) limite(s) cette solution peut rencontrer dans la pratique ?

*Fernet est une méthode faite pour répondre à un besoin spécifique, et non à un besoin général.* 


## Regard critique

Une des vulnérrabilités, c'est le fait qu'il suffit d'avoir le mot de passe afin de pouvoir déchiffrer chaque message. Pour ce faire, il faudrait implémenter du chiffrement symétrique, afin d'augmenter le niveau de sécurité. 