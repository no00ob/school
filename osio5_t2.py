from osio5_t1_tili import tili

m_tili = tili()
print("Tili.Talleta(int)")
m_tili.Talleta(int(input("Syötä raha joka talletetaan ")))
print("Tili.Korko(float)")
m_tili.Korko(float(input("Syötä korko prosentti desimaalina ")))
print("Tili.Tiliote()")
print(m_tili.Tiliote())
print("Tili.KorkoEnnuste(int))")
print(m_tili.KorkoEnnuste(int(input("Syötä kuinka monen vuoden päähän korko lasketaan "))))