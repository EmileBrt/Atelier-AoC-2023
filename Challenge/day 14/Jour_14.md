# Jour 14 : Parabolic Reflector Dish

## Difficulté 3.5/5

### Partie 1

Tu arrives à l'endroit où pointaient tous les miroirs : un immense réflecteur parabolique attaché à flanc d'une autre grande montagne.

L'antenne parabolique est composée de nombreux petits miroirs, mais bien que les miroirs eux-mêmes soient à peu près en forme de parabole, chaque miroir semble légèrement mal orienté. Si l'antenne est censée concentrer la lumière, pour le moment, elle ne fait que l'envoyer dans une direction vague.

Ce système doit être ce qui fournit l'énergie pour la lave ! Si tu réussis à focaliser l'antenne parabolique, peut-être que tu pourras aller à l'endroit où elle pointe et utiliser la lumière pour réparer la production de lave.

En y regardant de plus près, chaque miroir semble être relié par un système complexe de cordes et de poulies à une grande plateforme métallique située en dessous de l'antenne. La plateforme est recouverte de gros rochers de diverses formes. En fonction de leur position, le poids des rochers déforme la plateforme, et la forme de la plateforme détermine quelles cordes se tendent et, finalement, la direction du faisceau de l'antenne.

En résumé : si tu déplaces les rochers, tu peux focaliser l'antenne. La plateforme dispose même d'un panneau de commande sur le côté, te permettant de l'incliner dans quatre directions différentes ! Les rochers arrondis (O) rouleront lorsque la plateforme sera inclinée, tandis que les rochers cubiques (#) resteront en place. Tu notes les positions de tous les espaces vides (.) et des rochers (voici ton entrée de casse-tête). Par exemple :

```
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
```

Commence par incliner le levier pour que tous les rochers glissent vers le nord, aussi loin qu'ils peuvent aller :

```
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
```

Tu remarques que les poutres de soutien le long du côté nord de la plateforme sont endommagées ; pour t'assurer que la plateforme ne s'effondre pas, tu dois calculer la charge totale sur les poutres de soutien nord.

La charge causée par un seul rocher arrondi (O) est égale au nombre de rangées entre le rocher et le bord sud de la plateforme, y compris la rangée sur laquelle se trouve le rocher. (Les rochers cubiques (#) ne contribuent pas à la charge.) Ainsi, la charge exercée par chaque rocher dans chaque rangée est la suivante :

```
OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
```

La charge totale est la somme des charges causées par tous les rochers arrondis. Dans cet exemple, la charge totale est de 136.

Incline la plateforme pour que tous les rochers arrondis roulent vers le nord. Ensuite:

**Quelle est la charge totale sur les poutres de soutien nord ?**

---

### Partie 2

Le réflecteur parabolique se déforme, mais pas de manière à concentrer le faisceau. Pour y parvenir, tu devras déplacer les rochers vers les bords de la plateforme. Heureusement, un bouton sur le côté du panneau de commande, intitulé "cycle de rotation", tente de faire exactement cela !

Chaque cycle incline la plateforme quatre fois de façon à ce que les rochers arrondis roulent vers le nord, puis vers l'ouest, ensuite vers le sud, et enfin vers l'est. Après chaque inclinaison, les rochers arrondis roulent aussi loin qu'ils le peuvent avant que la plateforme ne s'incline dans la direction suivante. Après un cycle, la plateforme aura fait rouler les rochers arrondis dans ces quatre directions, dans cet ordre.

Voici ce qui se passe dans l'exemple ci-dessus après chacun des premiers cycles :

Après 1 cycle :

```
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
```

Après 2 cycles :

```
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
```

Après 3 cycles :

```
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
```

Ce processus devrait fonctionner si tu le laisses tourner suffisamment longtemps, mais tu t'inquiètes toujours pour les poutres de soutien nord. Pour t'assurer qu'elles survivront assez longtemps, tu dois calculer la charge totale sur les poutres de soutien nord après ``1 000 000 000`` cycles.

Dans l'exemple ci-dessus, après 1 000 000 000 cycles, la charge totale sur les poutres de soutien nord est de 64.

Fais tourner le cycle de rotation pendant 1 000 000 000 cycles. Ensuite:

**Quelle est la charge totale sur les poutres de soutien nord ?**