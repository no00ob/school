class tili:
    saldo = 0
    korko = 0
    def __init__(self):
        self.saldo = 0
        self.korko = 0
    def Talleta(self,summa):
        self.saldo += summa
    def Nosta(self,summa):
        temp = self.saldo - summa
        if (temp > 0):
            self.saldo = temp
    def Tiliote(self):
        return self.saldo
    def KorkoEnnuste(self,vuodet):
        return self.saldo + int((self.saldo*(1+self.korko)**vuodet)-self.saldo) 
    def Korko(self,m_korko):
        self.korko = m_korko
        self.saldo = self.KorkoEnnuste(1)