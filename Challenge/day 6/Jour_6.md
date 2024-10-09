# Jour 6 : Wait For It

## Difficulté 1/5

### Partie 1

L'organisateur vous conduit ensuite à l'endroit où les courses de bateaux ont lieu. Les bateaux sont beaucoup plus petits que ce à quoi vous vous attendiez — ce sont en fait des bateaux jouets, chacun avec un gros bouton sur le dessus. En maintenant le bouton enfoncé, vous chargez le bateau, et en relâchant le bouton, vous le faites avancer. Les bateaux vont plus vite si le bouton a été maintenu plus longtemps, mais le temps passé à maintenir le bouton est déduit du temps total de la course. Vous ne pouvez maintenir le bouton enfoncé qu'au début de la course, et les bateaux ne bougent pas tant que le bouton n'est pas relâché.

Par exemple :

```
Temps : 7 15 30
Distance : 9 40 200
```

Ce document décrit trois courses :

La première course a duré 7 millisecondes. La distance record pour cette course est de 9 millimètres.
La deuxième course a duré 15 millisecondes. La distance record pour cette course est de 40 millimètres.
La troisième course a duré 30 millisecondes. La distance record pour cette course est de 200 millimètres.
Votre bateau avec une vitesse nulle. Pour chaque milliseconde que vous passez à maintenir le bouton enfoncé, la vitesse du bateau augmente d'un millimètre par milliseconde.

Ainsi, comme la première course dure 7 millisecondes, vous avez plusieurs options :

- Ne pas maintenir le bouton du tout (c'est-à-dire le maintenir pendant 0 milliseconde) au début de la course. Le bateau ne bougera pas ; il aura parcouru 0 millimètre à la fin de la course.
- Maintenir le bouton pendant 1 milliseconde au début de la course. Ensuite, le bateau avancera à une vitesse de 1 millimètre par milliseconde pendant 6 millisecondes, atteignant une distance totale de 6 millimètres.
- Maintenir le bouton pendant 2 millisecondes, donnant au bateau une vitesse de 2 millimètres par milliseconde. Il lui restera alors 5 millisecondes pour avancer, atteignant une distance totale de 10 millimètres.
- Maintenir le bouton pendant 3 millisecondes. Après ses 4 millisecondes restantes de temps de déplacement, le bateau aura parcouru 12 millimètres.
- Maintenir le bouton pendant 4 millisecondes. Après ses 3 millisecondes restantes, le bateau aura parcouru 12 millimètres.
- Maintenir le bouton pendant 5 millisecondes, faisant parcourir au bateau une distance totale de 10 millimètres.
- Maintenir le bouton pendant 6 millisecondes, faisant parcourir au bateau une distance totale de 6 millimètres.
- Maintenir le bouton pendant 7 millisecondes. C'est la durée totale de la course. Vous n'avez jamais relâché le bouton. Le bateau ne peut pas bouger tant que vous ne relâchez pas le bouton. Assurez-vous de le relâcher pour que le bateau puisse bouger. Résultat : 0 millimètre.

Comme le record actuel de cette course est de 9 millimètres, il y a en fait 4 façons différentes de gagner : vous pouvez maintenir le bouton pendant 2, 3, 4 ou 5 millisecondes au début de la course.

Dans la deuxième course, vous pourriez maintenir le bouton pendant au moins 4 millisecondes et au plus 11 millisecondes pour battre le record, ce qui vous offre 8 façons différentes de gagner.

Dans la troisième course, vous pourriez maintenir le bouton pendant au moins 11 millisecondes et au plus 19 millisecondes pour battre le record, ce qui vous offre 9 façons différentes de gagner.

Pour connaître votre marge d'erreur, déterminez le nombre de façons dont vous pouvez battre le record dans chaque course ; dans cet exemple, si vous multipliez ces valeurs ensemble, vous obtenez ``288 (4 * 8 * 9)``.

Déterminez le nombre de façons dont vous pouvez battre le record dans chaque course:

**Que trouvez-vous si vous multipliez ces nombres ensemble ?**

---

### Partie 2

Alors que la course est sur le point de commencer, vous réalisez que le morceau de papier avec les temps de course et les distances records que vous avez reçu plus tôt avait en fait un espacement très mauvais entre les caractères. Il n'y a en réalité qu'une seule course - ignorez les espaces entre les chiffres sur chaque ligne.

Donc, l'exemple précédent :

```
Temps : 7 15 30
Distance : 9 40 200
```

... signifie maintenant ceci :

```
Temps : 71530
Distance : 940200
```

Vous devez maintenant déterminer combien de façons il existe pour gagner cette seule et longue course. Dans cet exemple, la course dure 71 530 millisecondes et la distance record que vous devez battre est de 940 200 millimètres. Vous pourriez maintenir le bouton enfoncé entre 14 et 71 516 millisecondes pour battre le record, soit un total de 71 503 façons !

**Combien de façons pouvez-vous battre le record dans cette longue course ?**