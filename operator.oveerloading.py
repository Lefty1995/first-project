from abc import ABC, abstractmethod


class Conto(ABC):
    def __init__(self, intestatario, saldo_iniziale=0):
        self._intestatario = intestatario
        self._saldo = saldo_iniziale

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valore):
        self._saldo = valore

    @staticmethod
    def valida_importo(importo):
        return importo > 0

    @abstractmethod
    def deposita(self, importo):
        pass

    @abstractmethod
    def preleva(self, importo):
        pass

    def __str__(self):
        return f"Conto di {self._intestatario} - Saldo {self._saldo:.2f}$"


class ContoCorrente(Conto):
    Commissione = 1.5

    def deposita(self, importo):
        if self.valida_importo(importo):
            self.saldo += importo
        else:
            print("Importo non valido per il deposito")

    def preleva(self, importo):
        totale = importo + ContoCorrente.Commissione
        if self.valida_importo(importo) and self.saldo >= totale:
            self.saldo -= totale
        else:
            print("Saldo insufficiente")

    def __add__(self, altro):
        nuovo_saldo = self.saldo + altro.saldo
        return ContoCorrente(f"{self._intestatario} e {altro._intestatario}", nuovo_saldo)


if __name__ == "__main__":
    cc1 = ContoCorrente("Luca", 1000)
    cc2 = ContoCorrente("Giulia", 500)

    # Operazioni di base
    cc1.deposita(300)   # saldo Luca: 1300
    cc1.preleva(50)     # 50 + 1.5 commissione → 51.5 → saldo: 1248.5
    print(cc1)          # Conto di Luca - Saldo 1248.50$

    # Fusione conti
    conto_fuso = cc1 + cc2   # saldo: 1248.5 + 500 = 1748.5
    print(conto_fuso)        # Conto di Luca e Giulia - Saldo 1748.50$
