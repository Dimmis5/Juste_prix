import random
print("Quelle est le prix de l'object X...?")
cible = random.randint(1,10)
print(cible)
for k in range (0,6):
    if k > 4 :
        print("vous avez perdu")
        break
    prop = int(input(f"Votre propositon entre 1 et 10 ({5-k} essaie restants) :"))
    if prop>cible :
        print("Trop grand")
    elif prop < cible :
        print("Trop bad")
    else :
        print("Bravo !")
        break