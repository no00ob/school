from osio5_t1_tili import tili

m_tili = tili()

print("Tilin saldo aluksi",m_tili.saldo,"\ntili.Talleta()")
m_tili.Talleta(int(input("Syötä raha joka talletetaan ")))
print("Tilin saldo talletuksen jälkeen",m_tili.saldo,"\ntili.Nosta()")
m_tili.Nosta(int(input("Syötä raha joka nostetaan ")))
print("Tilin saldo noston jälkeen",m_tili.saldo,"\ntili.Tiliote()")
print(m_tili.Tiliote())