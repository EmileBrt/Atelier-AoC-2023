# Jour 8 : Haunted Wasteland

## Difficulté 2/5

### Partie 1

Un des sacs du chameau est étiqueté "cartes" - et effectivement, il est rempli de documents (ton entrée de puzzle) sur comment naviguer dans le désert. Du moins, tu es à peu près sûr que c'est ce qu'ils sont ; un des documents contient une liste d'instructions gauche/droite, et le reste semble décrire un genre de réseau de nœuds étiquetés.

Il semble que tu sois censé utiliser les instructions gauche/droite pour naviguer dans le réseau. Peut-être que si tu fais suivre ces instructions au chameau, tu pourras échapper à ce désert hanté !

Après avoir examiné les cartes pendant un moment, deux nœuds ressortent : ``AAA`` et ``ZZZ``. Tu as l'impression que ``AAA`` est la position de **départ**, et tu dois suivre les instructions gauche/droite jusqu'à atteindre ``ZZZ``.

Ce format définit chaque nœud du réseau individuellement. Par exemple :

```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```

En commençant par ``AAA``, tu dois consulter l'élément suivant en fonction de la prochaine instruction gauche/droite dans tes données d'entrée. Dans cet exemple, commence par ``AAA`` et va à droite (R) en choisissant l'élément de droite de ``AAA``, soit ``CCC``. Ensuite, ``L`` signifie choisir l'élément de gauche de ``CCC``, soit ``ZZZ``. En suivant les instructions gauche/droite, tu atteins ``ZZZ`` en 2 étapes.

Bien sûr, il se peut que tu ne trouves pas ``ZZZ`` immédiatement. Si tu arrives au bout des instructions gauche/droite, répète toute la séquence d'instructions autant de fois que nécessaire : ``RL`` signifie en réalité ``RLRLRLRLRLRLRLRL...`` et ainsi de suite. Par exemple, voici une situation où il faut 6 étapes pour atteindre ``ZZZ`` :

```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```

En commençant à ``AAA``, suis les instructions gauche/droite:

**Combien d'étapes sont nécessaires pour atteindre ``ZZZ`` ?**

---

### Partie 2

Après avoir examiné les cartes un peu plus longtemps, ton attention est attirée par un fait curieux : le nombre de nœuds dont les noms se terminent par A est égal au nombre de nœuds dont les noms se terminent par Z !

```
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
```

Ici, il y a deux nœuds de départ, 11A et 22A (car ils se terminent tous les deux par A). En suivant chaque instruction gauche/droite, utilise cette instruction pour naviguer simultanément loin de chacun des nœuds où tu te trouves actuellement. Répète ce processus jusqu'à ce que tous les nœuds où tu te trouves se terminent par Z. (Si seulement certains des nœuds où tu te trouves se terminent par Z, ils fonctionnent comme n'importe quel autre nœud et tu continues normalement.) Dans cet exemple, tu procéderais comme suit :

- Étape 0 : Tu es à 11A et 22A.
- Étape 1 : Tu choisis tous les chemins de gauche, te menant à 11B et 22B.
- Étape 2 : Tu choisis tous les chemins de droite, te menant à 11Z et 22C.
- Étape 3 : Tu choisis tous les chemins de gauche, te menant à 11B et 22Z.
- Étape 4 : Tu choisis tous les chemins de droite, te menant à 11Z et 22B.
- Étape 5 : Tu choisis tous les chemins de gauche, te menant à 11B et 22C.
- Étape 6 : Tu choisis tous les chemins de droite, te menant à 11Z et 22Z.

Ainsi, dans cet exemple, tu finis entièrement sur des nœuds se terminant par Z après 6 étapes.

Commence simultanément sur chaque nœud se terminant par A:

**Combien d'étapes faut-il avant que tu ne sois uniquement sur des nœuds se terminant par Z ?**