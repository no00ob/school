def sum(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def printList(results = []):
    print("\nTulokset:")
    for x in range(0,len(results)):
        if (x == 0):
            m_str = "Summa: "
        elif (x == 1):
            m_str = "Tulo: "
        elif (x == 2):
            m_str = "Erotus: "
        else:
            m_str = "-"
        print(m_str,results[x])

while True:
    try:
        num1i = int(input("Syötä ensimmäinen numero: "))
        break
    except:
        print("\nVastauksesi ei ollut numero!")
        print("\nSyötä uusi numero!\n")
while True:
    try:
        num2i = int(input("Syötä toinen numero: "))
        break
    except:
        print("\nVastauksesi ei ollut numero!")
        print("\nSyötä uusi numero!\n")

nums = []
nums.append(sum(num1i,num2i))
nums.append(mul(num1i,num2i))
nums.append(div(num1i,num2i))
printList(nums)