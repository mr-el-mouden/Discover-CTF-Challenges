# ========================================================================


                    Author : Ayoub EL MOUDEN


# ========================================================================

# Challenge: BrainCheck

## Category
Misc/Reverse

## Difficulty
Easy

## File
challenge.bf

## Description general

Had fichier mektob b wahid langage ismo brainfuck.
Had language fih ghir 8 dial les symbols hom : '+' '-' '<' '>' '.' ',' '[' ']'
A partir dial had les symbols nkedro ndiro par exemple wahid text
+ kate3ni le numero 1
Ida ana ktebt 97+ fa ana kankon ktebt 97 = 'a' f ASCCI table
- kad3ni nakkas 1
. kad3ni afficher
> kad3ni avancer a droite
< kad3ni retour a gauche
, Saisir un caractere
[ Début d’une boucle tant que la cellule actuelle ≠ 0
] Fin d'une boucle


# Exemple

1/
++++++++++. = 10

Fhad le cat ++++++++++ Kad3ni 10, o le . kad3ni afficher, alors la resultat hia 10

2/
++++++++++.--. = 10 8

Fhad le cat ++++++++++ kad3ni 10, le . afficher 10, et -- kad3ni ghadi nenkass 2 o ghadi drja3 8, et le . kad3ni afficher. Alors la resultat final ghadi dkon 10 8

3/
++++++++[>++++++++<-]+.+. = AB

Fhad l'exemple ana sta3mlt les boucles

++++++++          cellule 0 = 8
Une fois ghadi dedkhol n la boucle ghadi khassni nemxi nwahid la cellule akhra o ghadi khassni nkteb fiha ++++++++, 

[>++++++++<-]     répète 8 fois:
                  cellule 1 += 8
o mn ba3d ghadi khassni nrja3 n la cellule lowla
                  cellule 0 -= 1
cellule 0 = 7

oghadi nbka n3awed hta la cellul lowla drja3 0

Résultat :
cellule 0 = 0
cellule 1 = 64

Fax ghadi nkhrej mn la boucle la cellule 1 = 64 mn ba3d ghadi nzid 1+ ghadi drja3 65, et le . affiche A (ASCCI Table), mn ba3d gahdi nzid 1+ ghadi drja3 66, et le . affiche B (ASCCI Table). La resultat final hia AB



# Solution

Ana hatit likom 2 codes python wahid kan3tih text kirej3o brainfuck language, o akhor kan3tih brainfuck language kirej3o text

Code python li kidir traduction mn text n brainfuck hoa ---to_brainfuck.py--
Use case dialo la commande suivante: python3 to_brainfuck.py text.txt

Code python li kidir traduction mn brainfuck n text hoa --bf.py--
Use case dialo la commande suivante: python3 bf.py brainfuck.bf

Une fois ghadi dir la commande : python3 bf.py challenge.bf , l'output ghadi dkon le code python suivant:

def check(user_input):
    secret = [73, 67, 79, 68, 69, 123, 52, 51, 103, 97, 101, 103, 122, 103, 104, 115, 97, 103, 50, 97, 113, 103, 99, 120, 122, 55, 56, 51, 48, 125]
    return [ord(c) for c in user_input] == secret

user = input("flag: ")

if check(user):
    print("Correct")
else:
    print("Wrong")
    
    
La liste secret fiha bzzaf dial les nombres, ida hna dirnalom traduction n ASCII code ghadi nl9aw lflag li hoa: 

ICODE{43gaegzghsag2aqgcxz7830}