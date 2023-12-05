
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard

import random


class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.result_label = Label(size_hint=(1, 0.8))
        self.add_widget(self.result_label)
        self.generate_button = Button(text="Genereer Karakter", size_hint=(1, 0.2))
        self.generate_button.bind(on_press=self.generate_character_prompt)
        self.add_widget(self.generate_button)
        self.copy_button = Button(text="Copy de lijst", size_hint=(1, 0.2))
        self.copy_button.bind(on_press=self.copy)
        self.add_widget(self.copy_button)

    def generate_character_prompt(self, instance=None):
        # Karaktereigenschappen
        geslacht = random.choice(["Man", "Vrouw"])
        etniciteit = random.choice(["Zombie", "Heks/Tovenaar", "Alien", "Superheld", "Fee", "Vampier", "Hond", "Kat", "Draak", "Mens", "Rat"])
        haar_style = random.choice(["Krullend haar", "Kaalkop", "Knot", "Vlecht", "Golvend", "Paardenstaart", "Staartjes"])
        hoofdac = random.choice(["Muts", "Hoed", "Niks", "Kroon", "Hoorns", "Hoofdoek"])
        gezicht = random.choice(["Niks", "Bril", "Snor", "Baard", "Sproeten", "Litteken", "Masker", "Pukkel"])
        bovenlichaam_kleding = random.choice(["T-shirt", "Trui", "Overhemd", "Vest", "Bloot + borsthaar", "Bloot", "Jas", "Jurk", "BH", "Naveltrui", "Hemdje", "Colbert"])
        onderlichaam_kleding = random.choice(["Broek", "Rok", "Korte broek", "Onderbroek", "Panty", "Legging", "Kousen", "Lingerie", "Pantalon"])
        schoenen = random.choice(["Sneakers", "Hakken", "Laarzen", "Slippers", "Niks", "Kisten", "Balerina's"])
        accessoires1 = random.choice(["Handschoenen", "Ketting", "Tattoo", "Niks", "Bezem", "Rugzak", "Handtas", "Verrekijker", "Oorbellen", "Paraplu"])
        accessoires2 = random.choice(["Handschoenen", "Ketting", "Tattoo", "Niks", "Bezem", "Rugzak", "Handtas", "Verrekijker", "Oorbellen", "Paraplu"])
        leeftijd = random.choice(["Baby", "Kind", "Tiener", "Volwassen", "Oud"])
        emotie = random.choice(["Blij", "Boos", "Verdrietig", "Angstig", "Verliefd"])

        # Resultaat weergeven
        self.result_label.text = f"Geslacht: {geslacht}\nEtniciteit: {etniciteit}\nLeeftijd: {leeftijd}\nEmotie: {emotie}\nHaarstijl: {haar_style}\nHoofdaccessoires: {hoofdac}\nGezicht: {gezicht}\nBovenlichaam kleding: {bovenlichaam_kleding}\nOnderlichaam kleding: {onderlichaam_kleding}\nSchoenen: {schoenen}\nAccessoires 1: {accessoires1}\nAccessoires 2: {accessoires2}"
        
   
    def copy(self, instance=None):
        copyresult = str(self.result_label.text)
        Clipboard.copy(copyresult)
        
class TekenPoppetjeApp(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    TekenPoppetjeApp().run()
