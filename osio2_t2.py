# Syöttö metodi joka tarkistaa onko 'input()' funktion tulos numeerinen arvo kysytyllä tarkkuudella (float, int)? !Muokattu tehtävää varten!
def InputNumber(whole = False, clamp = True):
    while True:
        try:
            if (whole == False):
                result = float(input())
            else:
                result = int(input())
            break
        except:
            print("Syötetty arvo ei ollut sallittu numero! Yritä uudestaan.\n ")
    if (clamp):
        if (result > 2):
            result = 2
        elif (result < 1):
            result = 1
    return result

print("Heräät aamulla ja olet myöhässä töistä. Mitä teet?\n[1] Lähdet välittömästi töihin\n[2] Toimit normaalin aamu rytmin mukaan")
lateChoice1 = InputNumber(True)
print("Juuri astuttuasi ulos, muistat unohtaneesi lompakkosi. Mitä teet?\n[1] Jätä lompakko ja lähde töihin\n[2] Lähde hakemaan lompakkoa")
lateChoice2 = InputNumber(True)


if (lateChoice1 == 1 & lateChoice2 == 1):
    print("Saavut töihin 5 minuuttia myöhässä. Mitä teet?\n[1] Välttele pomoa\n[2] Kävele suoraan työpisteelle")
    bossChoice = InputNumber(True)
elif (lateChoice1 == 1 & lateChoice2 == 2 or lateChoice1 == 2 & lateChoice2 == 1):
    print("Saavut töihin 20 minuuttia myöhässä. Mitä teet?\n[1] Välttele pomoa\n[2] Kävele suoraan työpisteelle")
    bossChoice = InputNumber(True)
    if (bossChoice == 1):
        bossChoice = 3
    else:
        bossChoice = 4
elif (lateChoice1 == 2 & lateChoice2 == 2):
    print("Saavut töihin 45 minuuttia myöhässä. Mitä teet?\n[1] Välttele pomoa\n[2] Kävele suoraan työpisteelle")
    bossChoice = InputNumber(True)
    if (bossChoice == 1):
        bossChoice = 5
    else:
        bossChoice = 6

gameOver = False

if (bossChoice == 2 or bossChoice == 5 or bossChoice == 6 or bossChoice == 4):
    print("Pomo näkee sinut matkalla ja kysyy miksi olet myöhässä. Mitä teet?\n[1] Vastaa rehellisesti\n[2] Keksi tekosyy")
    bossQuestionChoice = InputNumber(True)
    if (bossQuestionChoice == 1):
        if (bossChoice == 2):
            print("Pomo on ymmärtäväinen ja laskee sinut työpisteellesi päin. Saavut työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
            workPowerChoice = InputNumber(True)
            if (workPowerChoice == 1):
                workPowerChoice = 3
            else:
                workPowerChoice = 4
        elif (bossChoice == 4):
            print("Pomo kehottaa tulemaan ajoissa töihin jatkossa, mutta sallii sinun jatkaa matkaasi. Saavut työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
            workPowerChoice = InputNumber(True)
            if (workPowerChoice == 1):
                workPowerChoice = 5
            else:
                workPowerChoice = 6
        elif (bossChoice == 6):
            print("Pomo arvostaa rehellisyyttäsi, mutta kysyy sinulta montako kertaa olet jo ollut myöhässä tällä viikolla. Mitä teet?\n[1] Syötä vastauksesi:")
            howManyDaysLate = InputNumber(True, False)
            if (howManyDaysLate < 3):
                print("Pomon mukaan tuo on paska puhetta. Saat potkut. Hävisit.")
                gameOver = True
            else:
                print("Pomo arvostaa taas rehellisyyttäsi ja armahtaa myöhästymisesi. Etenet työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
                workPowerChoice = InputNumber(True)
                if (workPowerChoice == 1):
                    workPowerChoice = 7
                else:
                    workPowerChoice = 8
        elif (bossChoice == 5):
                print("Pomo kysyy sinulta miksi yritit paeta hänen luotaan ja alkaa syyttämään sinua yrityksen tappiosta. Saat potkut. Hävisit.")
                gameOver = True
    else:
        if (bossChoice == 2):
            print("Pomo kyseenalaistaa syytäsi, mutta kuitenkin laskee sinut työpisteellesi päin. Saavut työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
            workPowerChoice = InputNumber(True)
            if (workPowerChoice == 1):
                workPowerChoice = 3
            else:
                workPowerChoice = 4
        elif (bossChoice == 4):
            print("Pomo armahtaa sinut juuri ja juuri tämän kerran. Jatkat matkaasi kunnes Saavut työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
            workPowerChoice = InputNumber(True)
            if (workPowerChoice == 1):
                workPowerChoice = 5
            else:
                workPowerChoice = 6
        elif (bossChoice == 6):
                print("Pomo valittaa myöhästymisestäsi. Saat potkut. Hävisit.")
                gameOver = True
        elif (bossChoice == 5):
                print("Pomo kysyy sinulta miksi yritit paeta hänen luotaan ja alkaa syyttämään sinua yrityksen tappiosta. Saat potkut. Hävisit.")
                gameOver = True
elif (bossChoice == 1 or bossChoice == 3):
    print("Näet pomon matkalla, mutta onnistut täpärästi välttämään kontaktin. Saavut työpisteellesi. Mitä teet?\n[1] Työskentele tehokkaasti\n[2] Laiskottele")
    workPowerChoice = InputNumber(True)

if (gameOver == False):
    if (workPowerChoice == 1):
        print("Olet suoriutunut työpäiväsi erinomaisesti! Arvosana: S")
    elif (workPowerChoice == 2 or workPowerChoice == 3):
        print("Olet suoriutunut työpäiväsi hyvin! Arvosana: A")
    elif (workPowerChoice == 4 or workPowerChoice == 5):
        print("Olet suoriutunut työpäiväsi tyydyttävästi! Arvosana: B")
    elif (workPowerChoice == 6 or workPowerChoice == 7):
        print("Olet suoriutunut työpäiväsi välttävästi! Arvosana: C")
    elif (workPowerChoice == 8):
        print("Olet suoriutunut työpäiväsi puutteellisesti! Arvosana: D")
else:
    print("Olet suoriutunut työpäiväsi hylätysti! Arvosana: F")