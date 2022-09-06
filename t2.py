from random import randint

tilinSaldo = randint(100,10000)

tuet = int(input("Paljonko sait tukia? "))
tilinSaldo += tuet
print("Tilin saldo:", tilinSaldo - tuet, "\nTilin saldo tukien jälkeen:", tilinSaldo)

menot = int(input("\nPaljonko kulutit viikonloppuna? "))
tilinSaldo -= menot
print("Tilin saldo:", tilinSaldo - menot, "\nTilin saldo menojen jälkeen:", tilinSaldo)

if (tilinSaldo <= 0):
    print("\nTaisi rahat loppua lol")