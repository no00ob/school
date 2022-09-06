# Syöttö metodi joka tarkistaa onko 'input()' funktion tulos numeerinen arvo kysytyllä tarkkuudella (float, int)?
def InputNumber(msg = "", whole = False):
    while True:
        try:
            if (whole == False):
                result = float(input(msg))
            else:
                result = int(input(msg))
            break
        except:
            print("Syötetty arvo ei ollut sallittu numero! Yritä uudestaan.\n ")
    return result
# Tallenna käyttäjän kaksi numeroa
num1 = InputNumber("Syötä numero: ")
num2 = InputNumber("Syötä toinen numero: ")

print("\nMitä haluaisit tehdä numeroille?\n[1] Osamäärä\n[2] Tulo\n[3] Summa\n[4] Erotus")
# Tallenna mitä tehdään
ans = InputNumber("\nSyötä vastaus: ", True)
# Eipäs sallita yli tai ali meneviä vastauksia vaan ne clampataan takaisin maksimiin ja minimiin
if (ans <= 0):
    ans = 1
elif (ans > 4):
    ans = 4
# Handlaa vastaukset
if (ans == 1):
    print("\nOsamäärä:\n",num1/num2,"\n ")
elif (ans == 2):
    print("\nTulo:\n",num1*num2,"\n ")
elif (ans == 3):
    print("\nSumma:\n",num1+num2,"\n ")
elif (ans == 4):
    print("\nErotus:\n",num1-num2,"\n ")