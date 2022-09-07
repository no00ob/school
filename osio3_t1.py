age = 19
guess = -1

while guess != age:
    try:
        guess = int(input("Arvaa ikä: "))
    except:
        print("\nVastauksesi ei ollut kokonaisluku!")
    if (guess != age):
        print("\nYritä uudelleen!\n")

print("\nOikein arvattu! Ikä oli",age)