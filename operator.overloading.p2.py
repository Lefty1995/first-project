from abc import ABC, abstractmethod
import math

class Forma (ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __eq__(self, altra):
        return math.isclose(self.area(), altra.area())
    
    def __str__ (self):
            return f"{self.__class__.__name__} - Area: {self.area():.2f}, Perimetro: {self.perimetro():.2f}"
    
class Rettangolo(Forma):
    def __init__(self, base, altezza):
            self.base = base
            self.altezza = altezza
    
    def area(self):
            return self.base * self.altezza
    
    def perimetro(self):
            return 2 * (self.base + self.altezza)
        
class Cerchio(Forma):
    def __init__(self, raggio):
            self._raggio = raggio
    
    @property
    def raggio(self):
        return self._raggio

    @property
    def diametro(self):
        return self._raggio * 2
    def area(self):
        return math.pi * self._raggio **2
    def perimetro(self):
        return 2 * math.pi * self._raggio
    
class FiguraComposta(Forma):

    def __init__(self, forma1, forma2):
        self.forma1 = forma1
        self.forma2 = forma2

    def area(self):
        return self.forma1.area() + self.forma2.area()

    def perimetro(self):
        return f"FiguraComposta - Area Totale: {self.area():, 2f}"
    
Forma.__add__ = lambda self, altra: FiguraComposta(self, altra)

