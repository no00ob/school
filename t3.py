monthlyIncome = float(input("Paljonko rahaa jää kuukaudessa keskimäärin elämiseen? "))
daysMonthlyAtCampus = float(input("Kuinka monta päivää vietät aikaa kampuksella kuukausittain? "))
schoolFoodCost = float(input("Mitä maksaa kouluruoka? "))
monthlyIncome -= daysMonthlyAtCampus * schoolFoodCost
print("Kouluruokaan kuluu kuukaudessa {0}\nYlimääräistä rahaa jää jäljelle {1}".format(daysMonthlyAtCampus * schoolFoodCost, monthlyIncome))

otherExpenses = float(input("\nPaljonko rahaa kuluu muihin asioihin? "))

monthlyIncome -= otherExpenses
savings = monthlyIncome * 0.2
print("Jos ylimääräisestä rahasta laittaisi 20 prosenttia säästön, säästyisi {0}".format(savings))
print("Ja neljässä vuodessa säästyisi {0}".format(savings * 10 * 4))