card_suits = ["♥", "♠", "♦", "♣"]
card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit_dict = {"♠": "_piky", "♥": "_herce", "♦": "_kule", "♣": "_kříže"}

# třída pro vytváření objektů karet do hry
class Card:
    def __init__(self, suit, value):
        self.name = value + suit_dict[suit]
        self.suit = suit
        self.value = value
        
    #vypíše hodnoty karty
    def get_card(self):
        print(f"Tvoje karta je {self.name}, ozančení {self.suit}")

    #metoda k možnému zápisu karty do adresáře
    def to_dict(self):
        return {"symbol": self.suit, "value": self.value}

#založení objektů karet
prvniKarta = Card("♥","5")
druhaKarta = Card("♠","A")

#adresář karet
card_dict = []

#volání metod karet
prvniKarta.get_card()
druhaKarta.get_card()

#přidání karet do adresáře
card_dict.append(prvniKarta.to_dict())
card_dict.append(druhaKarta.to_dict())

#výpis karet v adresáři
print(card_dict)