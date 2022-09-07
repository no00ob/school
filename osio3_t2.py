stop = "amongus"
shoppingList = []

while stop != "valmis" and stop != "Valmis":
    newItem = input("Syötä uusi tuote tai 'valmis' kun olet valmis: ")
    stop = newItem
    if (stop != "valmis" and stop != "Valmis"):
        shoppingList.append(newItem)
    else:
        shoppingList.sort()

print("\nLista valmis!")
for x in shoppingList:
    print("-",x)