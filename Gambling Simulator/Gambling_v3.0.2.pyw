import tkinter as tk
import random
import os
import json
import pygame

#INHALT
    #Texte
    #Booleans
    #Haupt Varable
    #Check_for
    #Schleifen
    #Variablen
    #Tasten
    #Spielerdaten
        #Statistik
            #Klicks
            #Highscore
    #Benutzer
    #Menü
    #Verlieren
    #Audio
    #Labels & Buttons
    #Start()
    #Main()
#Variablen-------------------------------------->
coins = 100
zufallszahl = 9
zufallszahl_normal = 9
zahl_manipulation = 1
gewinnercoins = 100
gewinnercoins_trippel = 20
gewinnercoins_doppel = 5
gewinnercoins_zwei_doppel = 15
verlierercoins = 0
gewinn_coins = 10
clicks_angezeigt = 0
zwischen_coins = 0
#Variablen------------------------------------->
#Texte----------------------------------------->
def texte_var():
    global text_10, text_25, text_50, text_75, text_100, text_200, wähle_einsatz_text, beispiel_text, gewinntext4gleiche, verliertext, gewinntext2gleiche, gewinntext2x2gleiche, gewinntext3gleiche
    text_10 = "Keine 10 Coins mehr"
    text_25 = "Keine 25 Coins mehr"
    text_50 = "Keine 50 Coins mehr"
    text_75 = "Keine 75 Coins mehr"
    text_100 = "Keine 100 Coins mehr"
    text_200 = "Keine 200 Coins mehr"
    wähle_einsatz_text = "Wähle zuerst deinen Einsatz!"
    beispiel_text = "Dein Guthaben: 100 Coins"
    gewinntext4gleiche = "Jackpott"
    verliertext = "Du hast verloren"
    gewinntext2gleiche = "Doppel"
    gewinntext2x2gleiche = "Zwei Doppel"
    gewinntext3gleiche = "Trippel"
texte_var()
#Texte----------------------------------------->
#Booleans----------------------------------------->
var_liste_status = [False] * 8
gesetzt = [False] * 8
seiten = False
clicking = False
gewonnen_boo = None
zwischenschritt_boo = False
#Booleans----------------------------------------->
#Main_Window----------------------------------------->
root = tk.Tk()
root.geometry("550x800")
root.title("")
root.resizable(False, False)
icon_image = tk.PhotoImage(file="photos/icon.png")  # Pfad zu deinem Icon
root.iconphoto(False, icon_image)
root.overrideredirect(False)
#----------------------------------------->
pygame.mixer.init()
#Bilder----------------------------------------->
def bilder():
    global münzen_bild_10, münzen_bild_25, münzen_bild_50, münzen_bild_75, münzen_bild_100, fuck_it, start__button, background_image, seite_r_rot, seite_l_rot, seite_r_grün, seite_l_grün, rollen_bild, verlier_bild_kopf_oben, verlier_bild_kopf_unten, verlier_bild_kopf_mitte, _25_pos_200, _50_pos_200, _75_pos_200, _100_pos_200, _200_pos_200, _50_pos_500, _75_pos_500, _100_pos_500, _200_pos_500, _500_pos_500, _75_pos_1000, _100_pos_1000, _200_pos_1000, _500_pos_1000, _1000_pos_1000

    münzen_bild_10 = tk.PhotoImage(file="photos/10.png")
    münzen_bild_25 = tk.PhotoImage(file="photos/25.png")
    münzen_bild_50 = tk.PhotoImage(file="photos/50.png")
    münzen_bild_75 = tk.PhotoImage(file="photos/75.png")
    münzen_bild_100 = tk.PhotoImage(file="photos/100.png")
    fuck_it = tk.PhotoImage(file="photos/Photo_neustart.png")
    start__button = tk.PhotoImage(file="photos/Start.png")
    background_image = tk.PhotoImage(file="photos/gamblegame-hg-end2.png")
    seite_r_rot = tk.PhotoImage(file=r"photos\Rote_leiste_r.png")
    seite_l_rot = tk.PhotoImage(file=r"photos\Rote_leiste_l.png")
    seite_r_grün = tk.PhotoImage(file=r"photos\Grüne_leiste_r.png")
    seite_l_grün = tk.PhotoImage(file=r"photos\Grüne_leiste_l.png")
    rollen_bild = tk.PhotoImage(file=r"photos\menü_rolle.png")
    verlier_bild_kopf_oben = tk.PhotoImage(file=r"photos\verlier_bild_kopf_oben.png")
    verlier_bild_kopf_unten = tk.PhotoImage(file=r"photos\verlier_bild_kopf_unten.png")
    verlier_bild_kopf_mitte = tk.PhotoImage(file=r"photos\verlier_bild_kopf_mitte.png")
    _25_pos_200 = tk.PhotoImage(file="photos/coin25-pos200.png")
    _50_pos_200 = tk.PhotoImage(file="photos/coin50-pos200.png")
    _75_pos_200 = tk.PhotoImage(file="photos/coin75-pos200.png")
    _100_pos_200 = tk.PhotoImage(file="photos/coin100-pos200.png")
    _200_pos_200 = tk.PhotoImage(file="photos/coin200-pos200.png")
    _50_pos_500 = tk.PhotoImage(file="photos/coin50-pos500.png")
    _75_pos_500 = tk.PhotoImage(file="photos/coin75-pos500.png")
    _100_pos_500 = tk.PhotoImage(file="photos/coin100-pos500.png")
    _200_pos_500 = tk.PhotoImage(file="photos/coin200-pos500.png")
    _500_pos_500 = tk.PhotoImage(file="photos/coin500-pos500.png")
    _75_pos_1000 = tk.PhotoImage(file="photos/coin75-pos500.png")
    _100_pos_1000 = tk.PhotoImage(file="photos/coin100-pos500.png")
    _200_pos_1000 = tk.PhotoImage(file="photos/coin200-pos500.png")
    _500_pos_1000 = tk.PhotoImage(file="photos/coin500-pos500.png")
    _1000_pos_1000 = tk.PhotoImage(file="photos/coin500-pos500.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

bilder()
#Bilder----------------------------------------->
#Haupt_Funktion_Anfang----------------------------------------->
def generate_random_number():
    global coins, gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinn_coins, clicking, var_liste_status, seiten, random_number_4, random_number_1, random_number_2, random_number_3
    seiten = True
    clicking = True
    start()

    #Zufallszahlen werden erstellt
    random_number_1 = random.randint(1, zufallszahl)
    random_number_2 = random.randint(1, zufallszahl)
    random_number_3 = random.randint(1, zufallszahl)
    random_number_4 = random.randint(1, zufallszahl)
    aktualisiere_coins(0, 0, 1, 0)
    # Zeige die generierten Zahlen im Label an
    start_animation()
    start_animation_2()
    start_animation_3()
    start_animation_4()
    root.after(800, generate_label_0)
    
def generate_label_0():
    stop_animation()
    zufallszahlen_label_1.config(text=f" {random_number_1} ")
    zahlen_click_sound()
    
    root.after(1000, lambda: generate_label_1(zufallszahlen_label_2, random_number_2, random_number_1, random_number_3))
    
def generate_label_1(zufallszahlen_label_2, random_number_2, random_number_1, random_number_3):
    stop_animation_2()
    zufallszahlen_label_2.config(text=f" {random_number_2} ")
    zahlen_click_sound()
    root.after(1000, lambda: generate_label_2(zufallszahlen_label_4, random_number_1, random_number_2, random_number_3))

def generate_label_2(zufallszahlen_label_4, random_number_2, random_number_1, random_number_3):
    
    stop_animation_4()
    zufallszahlen_label_4.config(text=f" {random_number_4} ")
    zahlen_click_sound()
    root.after(1000, lambda: finalize_game(random_number_1, random_number_2, random_number_3))
    
def finalize_game(random_number_1, random_number_2, random_number_3):
    global coins, gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinn_coins, clicking, var_liste_status, gesetzt, gewonnen_boo
    
    stop_animation_3()
    # Zeige die letzte Zufallszahl an
    zufallszahlen_label_3.config(text=f" {random_number_3} ")
    zahlen_click_sound()
    # Überprüfe die Bedingungen für Gewinn oder Verlust
    if random_number_1 == random_number_2 == random_number_3 == random_number_4:
        zahlen_gewinn_schleife()
        coins += gewinnercoins
        gewinn_coins = gewinnercoins
        gewonnen_boo = True
        aktualisiere_coins(gewinnercoins, 0, 0, gewinnercoins)
        #Informationen was du Gewonnen oder Verloren hast
        text_label.config(text=f"Jackpott: {gewinn_coins} Coins gewonnen")
        root.after(0, lambda: schleife_seite_1())

    elif random_number_1 == random_number_2 == random_number_3 or random_number_2 == random_number_3 == random_number_4 or random_number_1 == random_number_3 == random_number_4 or random_number_1 == random_number_2 == random_number_4:
        coins += gewinnercoins_trippel
        gewinn_coins = gewinnercoins_trippel
        gewonnen_boo = True
        aktualisiere_coins(gewinnercoins_trippel, 0, 0, gewinnercoins_trippel)
        #Informationen was du Gwonnen oder Verloren hast
        text_label.config(text=f"Trippel: {gewinn_coins} Coins gewonnen")
        root.after(0, lambda: schleife_seite_1())

    elif random_number_1 == random_number_2 and random_number_3 == random_number_4 or random_number_1 == random_number_3 and random_number_2 == random_number_4 or random_number_1 == random_number_4 and random_number_2 == random_number_3:
        coins += gewinnercoins_zwei_doppel
        gewinn_coins = gewinnercoins_zwei_doppel
        gewonnen_boo = True
        aktualisiere_coins(gewinnercoins_zwei_doppel, 0, 0, gewinnercoins_zwei_doppel)
        #Informationen was du Gwonnen oder Verloren hast
        text_label.config(text=f"Pärchen: {gewinn_coins} Coins gewonnen")
        root.after(0, lambda: schleife_seite_1())

    elif random_number_1 == random_number_2 or random_number_2 == random_number_3 or random_number_1 == random_number_3 or random_number_1 == random_number_4 or random_number_2 == random_number_4 or random_number_3 == random_number_4:
        coins += gewinnercoins_doppel
        gewinn_coins = gewinnercoins_doppel
        gewonnen_boo = True
        aktualisiere_coins(gewinnercoins_doppel, 0, 0, gewinnercoins_doppel)
        #Informationen was du Gwonnen oder Verloren hast
        text_label.config(text=f"Doppel: {gewinn_coins} Coins gewonnen")
        root.after(0, lambda: schleife_seite_1())

    else:
        coins -= verlierercoins
        gewinn_coins = verlierercoins
        gewonnen_boo = False
        aktualisiere_coins(0, verlierercoins, 0, 0)
        #Informationen was du Gwonnen oder Verloren hast
        text_label.config(text=f"Du hast {gewinn_coins} Coins verloren")
    
    clicking = False
    anzeige_coins()
    coins_label.config(text=f"{formatted_coins}")
    var_liste_status = [False] * 8 # Damit man nochmal einen wert auswählen muss
    gesetzt = [False] * 8
    verlierercoins = 0
    verlieren() # Es wird gecheckt ob du verloren hast
    check_for_200()
    check_for_100()
    check_for_500()
    check_for_1000()

    root.after(2000, lambda: schleife())

#Haupt_funktion_ende----------------------------------------->
#Check_for_anfang----------------------------------------->

def check_for_100():
    global coins, hundert_button, zwei_hundert_button
    if 0 < coins < 2000:
        hundert_button.place(x=371, y=552, width=95, height=95)
        hundert_button.config(image=münzen_bild_100)

        fünfundsiebzig_button.place(x=337, y=644, width=95, height=95)
        fünfundsiebzig_button.config(image=münzen_bild_75)

        fünfzig_button.place(x=231, y=684, width=95, height=95)
        fünfzig_button.config(image=münzen_bild_50)

        fünfundzwanzig_button.place(x=127, y=645, width=95, height=95)
        fünfundzwanzig_button.config(image=münzen_bild_25)

        zehn_button.place(x=95, y=550, width=95, height=95)
        zehn_button.config(image=münzen_bild_10)

        tausend_button.place_forget()
        fünf_hundert_button.place_forget()
        zwei_hundert_button.place_forget()
    else:
        pass

def check_for_200():
    global coins
    if 2000 < coins < 5000:
        zwei_hundert_button.place(x=373, y=555, width=90, height=90)
        zwei_hundert_button.config(image=_200_pos_200)

        hundert_button.place(x=340, y=645, width=90, height=90)
        hundert_button.config(image=_100_pos_200)

        fünfundsiebzig_button.place(x=233, y=686, width=90, height=90)
        fünfundsiebzig_button.config(image=_75_pos_200)

        fünfzig_button.place(x=130, y=648, width=90, height=90)
        fünfzig_button.config(image=_50_pos_200)

        fünfundzwanzig_button.place(x=97, y=554, width=90, height=90)
        fünfundzwanzig_button.config(image=_25_pos_200)

        tausend_button.place_forget()
        zehn_button.place_forget()
        fünf_hundert_button.place_forget()
    else:
        pass

def beispiel():
    def check_for_500_end():
        if 2000 < coins < 5000:
            zwei_hundert_button.place(x=371, y=552, width=90, height=90)
            hundert_button.place(x=337, y=644, width=90, height=90)
            fünfundsiebzig_button.place(x=231, y=684, width=90, height=90)
            fünfzig_button.place(x=127, y=645, width=90, height=90)
            fünfundzwanzig_button.place(x=95, y=550, width=90, height=90)
            zehn_button.place_forget()
            fünf_hundert_button.place_forget()
        else:
            pass

def beispiel_1():
    def check_for_1000_end():
        if 5000 < coins < 10000:
            fünf_hundert_button.place(x=371, y=552, width=95, height=95)
            zwei_hundert_button.place(x=337, y=644, width=95, height=95)
            hundert_button.place(x=231, y=684, width=95, height=95)
            fünfundsiebzig_button.place(x=127, y=645, width=95, height=95)
            fünfzig_button.place(x=95, y=550, width=95, height=95)
            fünfundzwanzig_button.place_forget()
            zehn_button.place_forget()
        else:
            pass
        
def check_for_500():
    if 10000 > coins > 5000:
        fünf_hundert_button.place(x=373, y=556, width=90, height=90)
        fünf_hundert_button.config(image=_500_pos_500)

        zwei_hundert_button.place(x=340, y=645, width=90, height=90)
        zwei_hundert_button.config(image=_200_pos_500)

        hundert_button.place(x=234, y=686, width=90, height=90)
        hundert_button.config(image=_100_pos_500)

        fünfundsiebzig_button.place(x=131, y=647, width=90, height=90)
        fünfundsiebzig_button.config(image=_75_pos_500)

        fünfzig_button.place(x=96, y=554, width=90, height=90)
        fünfzig_button.config(image=_50_pos_500)

        tausend_button.place_forget()
        fünfundzwanzig_button.place_forget()
        zehn_button.place_forget()
    else:
        pass

def check_for_1000():
    if coins > 10000:
        tausend_button.place(x=371, y=552, width=90, height=90)
        tausend_button.config(image=_1000_pos_1000)

        fünf_hundert_button.place(x=337, y=644, width=90, height=90)
        fünf_hundert_button.config(image=_500_pos_1000)

        zwei_hundert_button.place(x=231, y=684, width=90, height=90)
        zwei_hundert_button.config(image=_200_pos_1000)

        hundert_button.place(x=127, y=645, width=90, height=90)
        hundert_button.config(image=_100_pos_1000)

        fünfundsiebzig_button.place(x=95, y=550, width=90, height=90)
        fünfundsiebzig_button.config(image=_75_pos_1000)

        fünfzig_button.place_forget()
        fünfundzwanzig_button.place_forget()
        zehn_button.place_forget()
    else:
        pass

#Check_for_ende----------------------------------------->
#Schleifen----------------------------------------->

def schleife():
    if any (gesetzt):
        pass
    else:
        text_label.config(text="Was willst du setzen?")
        root.after(800, lambda: schleife_1())

def schleife_1():
    if any (gesetzt):
        pass
    else:
        if gewonnen_boo:
            text_label.config(text=f"Du hast {gewinn_coins} Coins gewonnen")
            root.after(800, lambda: schleife())
        else:
            text_label.config(text=f"Du hast {gewinn_coins} Coins verloren")
            root.after(800, lambda: schleife())

def schleife_seite_1():
    if not seiten:
        pass
    else:
        seite_l_label.place(x=0, y=0, width=40, height=800)
        seite_r_label.place_forget()
        root.after(200, lambda: schleife_seite_2())

def schleife_seite_2():
    if not seiten:
        pass
    else:
        seite_r_label.place(x=510, y=0, width=40, height=800)
        seite_l_label.place_forget()
        root.after(200, lambda: schleife_seite_1())

color = True

def zahlen_gewinn_schleife():
    global color
    if color is True:
        zufallszahlen_label_1.config(foreground="red")
        zufallszahlen_label_2.config(foreground="red")
        zufallszahlen_label_3.config(foreground="red")
        zufallszahlen_label_4.config(foreground="red")
        color = False
        root.after(1000, zahlen_gewinn_schleife)
    elif color is False:
        zufallszahlen_label_1.config(foreground="black")
        zufallszahlen_label_2.config(foreground="black")
        zufallszahlen_label_3.config(foreground="black")
        zufallszahlen_label_4.config(foreground="black")
        color = True
        root.after(1000, zahlen_gewinn_schleife)
    else:
        pass

def zahlen_gewinn_schleife_die_ersten_zwei_gleich():
    global color
    if color:
        zufallszahlen_label_1.config(foreground="red")
        zufallszahlen_label_2.config(foreground="red")
        root.after(1000, zahlen_gewinn_schleife)
        color = False
    elif not color:
        zufallszahlen_label_1.config(foreground="black")
        zufallszahlen_label_2.config(foreground="black")
        color = True
        root.after(1000, zahlen_gewinn_schleife)
    else:
        pass

#Schleifen_ende----------------------------------------->
#Variablen----------------------------------------->
def gestzt_var_text(): # Info wieviele Coins du gesetzt hast
    text_label.config(text=f"Du hast {verlierercoins} Coins gesetzt")

def start_var(): # Bring das Spiel zum laufen wenn du den Start Button Drückst blockt aber wenn das spiel 
    global clicking #schon läuft und vordert dazu auf einen einsatzt zu wählen wenn noch keiner
    if clicking: #gewählt wurde
        pass
    elif any(var_liste_status):
        #text_label.config(f"Du hast {coins} Coins im Pott")
        generate_random_number()
    else:
        text_label.config(text=wähle_einsatz_text)

#Variable für den fuck it button----------------------------------------->

def exit_game():
    root.destroy()

def start_text():
    text_label.config(text=f"Dein Guthaben: {coins} Coins")

#Tasten----------------------------------------->

def taste_10():
    if coins < 10:
        text_label.config(text=text_10)
        var_liste_status[0] = True
        verlieren()
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        if coins < (verlierercoins + 10):
            pass
        else:
            verlierercoins += 10
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[0] = True
            gesetzt[0] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_25():
    if coins < 25:
        text_label.config(text=text_25)
        var_liste_status[1] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 25):
            pass
        else:
            verlierercoins += 25
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[1] = True
            gesetzt[1] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_50():
    if coins < 50:
        text_label.config(text=text_50)
        var_liste_status[2] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 50):
            pass
        else:
            verlierercoins += 50
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[2] = True
            gesetzt[2] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_75():
    if coins < 75:
        text_label.config(text=text_75)
        var_liste_status[3] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 75):
            pass
        else:
            verlierercoins += 75
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[3] = True
            gesetzt[3] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_100():
    if coins < 100:
        text_label.config(text=text_100)
        gesetzt[4] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 100):
            pass
        else:
            verlierercoins += 100
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[4] = True
            gesetzt[4] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()
    
def taste_200():
    if coins < 200:
        text_label.config(text=text_200)
        gesetzt[5] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 200):
            pass
        else:
            verlierercoins += 200
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[5] = True
            gesetzt[5] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_500():
    if coins < 500:
        text_label.config(text=text_200)
        gesetzt[6] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 500):
            pass
        else:
            verlierercoins += 500
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[6] = True
            gesetzt[6] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()

def taste_1000():
    if coins < 1000:
        text_label.config(text=text_200)
        gesetzt[7] = True
    elif clicking:
        pass
    else:
        global gewinnercoins, gewinnercoins_doppel, verlierercoins, gewinnercoins_trippel, gewinnercoins_zwei_doppel, seiten, color
        coins_click_sound()
        if coins < (verlierercoins + 1000):
            pass
        else:
            verlierercoins += 1000
            gewinnercoins = verlierercoins * 50
            gewinnercoins_doppel = verlierercoins 
            gewinnercoins_trippel = verlierercoins * 10
            gewinnercoins_zwei_doppel = verlierercoins * 5
            var_liste_status[7] = True
            gesetzt[7] = True
            seiten = False
            color = None
            gestzt_var_text()
            start()
#Tasten Ende----------------------------------------->
#Spielerdaten----------------------------------------->

# Funktion zum Öffnen eines zweiten Fensters

def öffne_zweites_fenster():
    global aktualisiere_coins, coins, benutzer_abrufen, coins_k, Benutzername_anzeige, entry_name, entry_passwort, button_speichern, button_abrufen, label_ergebnis, Passwort_anzeige, entry_passwort, speichere_zeitstand, time_running
    
    # Ordnerpfad für die JSON-Datei festlegen
    ordner_pfad = r"Spielerdaten"
    json_datei = os.path.join(ordner_pfad, "spielerdaten.json")

    # Erstelle den Ordner, falls er nicht existiert
    if not os.path.exists(ordner_pfad):
        os.makedirs(ordner_pfad)

    # Funktion zum Laden der JSON-Daten (wenn Datei existiert)
    def lade_daten():
        if os.path.exists(json_datei):
            with open(json_datei, "r") as file:
                return json.load(file)
        else:
            return {}

    # Funktion zum Speichern der JSON-Daten
    def speichere_daten(daten):
        try:
            with open(json_datei, "w") as file:
                json.dump(daten, file, indent=4)
        except Exception as e:
            print(f"Fehler beim Speichern der Daten: {e}")

    # Funktion zum Abrufen eines Benutzers
    def benutzer_abrufen():
        global coins, clicks_angezeigt, benutzer_show, coins_k
        click_sound_buttons()
        
        benutzername = entry_name.get()
        passwort = entry_passwort.get()
        daten = lade_daten()
        
        if benutzername in daten:
            gespeichertes_passwort = daten[benutzername]["passwort"]
            if passwort == gespeichertes_passwort:
                # Passwort korrekt, Benutzer abrufen
                coins_daten = daten[benutzername]["coins"]
                clicks = daten[benutzername]["clicks"]
                highscore = daten[benutzername]["highscore"]
                coins = coins_daten
                coins_k = coins
                clicks_angezeigt = clicks
                highscore_angezeigt = highscore
                highscore_label.config(text=f"Highscore: {highscore_angezeigt}")
                clicks_label.config(text=f"Clicks: {clicks_angezeigt}")
                anzeige_coins()
                coins_label.config(text=f"{formatted_coins}")
                text_label.config(text=f"Dein Guthaben: {formatted_coins} Coins")
                label_ergebnis.config(text=f"{benutzername} hat {coins} Coins.")
                benutzername_frame.place(x=100, y=200)
                benutzername_label.config(text=f"{benutzername}")
                benutzername_frame.lift()
                lade_zeitstand()
                start_timer()
                check_for_200()
                check_for_100()
                check_for_500()
                check_for_1000()
                toggle_benutzer()
                daten[benutzername]["coins"] = coins  # Aktualisiere die gespeicherten Coins
                speichere_daten(daten)
            else:
                # Falsches Passwort
                label_ergebnis.config(text="Falsches Passwort.")
        else:
            # Benutzer existiert nicht
            label_ergebnis.config(text="Benutzer nicht gefunden. Bitte erstellen.")

    # Funktion zum Speichern eines neuen Benutzers
    def benutzer_speichern():
        click_sound_buttons()
        benutzername = entry_name.get()
        passwort = entry_passwort.get()
        clicks_start = 0 
        highscore_start = 0 
        start_zeitstand = 0
        if len(benutzername) > 6:
            label_ergebnis.config(text="Benutzername darf maximal 6 Zeichen haben.")
            return  # Beende die Funktion, wenn die Länge überschritten ist

        if len(passwort) < 4:
            label_ergebnis.config(text="Passwort muss mindestens 4 Zeichen lang sein.")
            return
        
        if len(passwort) > 12:
            label_ergebnis.config(text="Passwort darf maximal 12 Zeichen lang sein.")
            return

        daten = lade_daten()
        
        if benutzername not in daten:
            # Benutzer existiert nicht, neuen Benutzer erstellen
            aktuelle_coins = coins
            daten[benutzername] = {"coins": aktuelle_coins, "passwort": passwort, "clicks": clicks_start, "highscore": highscore_start, "zeitstand": start_zeitstand}
            speichere_daten(daten)
            label_ergebnis.config(text=f"{benutzername} wurde erstellt mit {aktuelle_coins} Coins.")
        else:
            # Benutzer existiert bereits
            label_ergebnis.config(text=f"{benutzername} existiert bereits.")

    # Funktion zum Aktualisieren der Coins (z.B. durch Spielgewinne/-verluste)
    def aktualisiere_coins(aenderung, aenderung_2, clicks_aenderung, highscore_aenderung):
        benutzername = entry_name.get()
        daten = lade_daten()
        
        if benutzername in daten:
            daten[benutzername]["coins"] += aenderung
            daten[benutzername]["coins"] -= aenderung_2
            daten[benutzername]["clicks"] += clicks_aenderung

            neue_coins = coins + highscore_aenderung

            # Überprüfung und Aktualisierung
            if neue_coins >= daten[benutzername]["highscore"]:
                #Setze den Highscore
                daten[benutzername]["highscore"] = coins

            speichere_daten(daten)
            highscore_angezeigt = daten[benutzername]["highscore"]
            highscore_label.config(text=f"Highscore: {highscore_angezeigt}")
            clicks_angezeigt = daten[benutzername]["clicks"]
            clicks_label.config(text=f"Clicks: {clicks_angezeigt}")
        else:
            label_ergebnis.config(text="Benutzer nicht gefunden. Bitte erstellen.")

    def speichere_zeitstand():
        global time_running
        if entry_name.get() == "":  # Wenn das Entry-Feld leer ist
            time_running = False
        else:
            benutzername = entry_name.get()
            daten = lade_daten()
            daten[benutzername]["zeitstand"] = time  # Speichert den aktuellen Stand der `time`-Variable
            speichere_daten(daten)

    # Funktion, um den Zeitstand aus JSON zu laden
    def lade_zeitstand():
        if entry_name.get() == "":  # Wenn das Entry-Feld leer ist
            pass
        else:
            global time
            benutzername = entry_name.get()
            daten = lade_daten()
            time = daten[benutzername]["zeitstand"]  # Lade die gespeicherte Zeit oder 0, wenn nicht vorhanden
    
    # Eingabefeld für den Benutzernamen
    Benutzername_anzeige = tk.Label(root, text="Benutzername:")
    Benutzername_anzeige.place(x=200, y=320)

    entry_name = tk.Entry(root)
    entry_name.place(x=200, y=350)

    # Eingabefeld für das Passwort
    Passwort_anzeige = tk.Label(root, text="Passwort:")
    Passwort_anzeige.place(x=200, y=380)

    entry_passwort = tk.Entry(root, show="*")  # Verstecke Eingabe mit Sternchen
    entry_passwort.place(x=200, y=410)

    # Button zum Speichern des Benutzers
    button_speichern = tk.Button(root, text="Benutzer speichern", command=benutzer_speichern)
    button_speichern.place(x=200, y=440)

    # Button zum Abrufen des Benutzers
    button_abrufen = tk.Button(root, text="Benutzer abrufen", command=benutzer_abrufen)
    button_abrufen.place(x=200, y=470)

    # Ergebnislabel für die Ausgabe
    label_ergebnis = tk.Label(root, text="")
    label_ergebnis.place(x=200, y=500)

    entry_passwort.bind("<Return>", lambda event: benutzer_abrufen())

time_running = False
time = 0  # Zeit in Sekunden

def update_timer():
    global time, time_running, speichere_zeitstand, days, hours, minutes, seconds
    if time_running:
        if menü_show:
            time += 1
            days = time // 86400
            hours = (time % 86400) // 3600
            minutes = (time % 3600) // 60
            seconds = time % 60
            time_label.config(text=f"Zeit: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")
            speichere_zeitstand()
            root.after(1000, update_timer)
        else:
            time += 1
            days = time // 86400
            hours = (time % 86400) // 3600
            minutes = (time % 3600) // 60
            seconds = time % 60
            speichere_zeitstand()
            root.after(1000, update_timer)

def start_timer():
    """Startet den Timer."""
    global time_running
    if not time_running:
        time_running = True
        update_timer()

def stop_timer():
    """Stoppt den Timer."""
    global time_running
    time_running = False

def reset_timer():
    """Setzt den Timer zurück."""
    global time, time_running
    time_running = False
    time = 0
    time_label.config(text="00:00:00:00")

#Benutzer----------------------------------------->
def benutzer_on():
    if clicking:
        pass
    else:
        click_sound_buttons()
        menü_button.place_forget()
        benutzer_button.lift()
        rollen_frame.place(x=0, y=0, width=550, height=800)
        menü_button.lift()
        benutzername_frame.place_forget()
        root.after(0, lambda: öffne_zweites_fenster())
    

def benutzer_off():
    if clicking:
        pass
    else:
        click_sound_buttons()
        menü_button.place(x=0, y=0, width=95, height=95)
        benutzer_button.place(x=455, y=0, width=95, height=95)
        Benutzername_anzeige.place_forget()
        entry_name.place_forget()
        button_speichern.place_forget()
        button_abrufen.place_forget()
        label_ergebnis.place_forget()
        rollen_frame.place_forget()
        Passwort_anzeige.place_forget()
        entry_passwort.place_forget()

benutzer_show = False

def toggle_benutzer():
    global benutzer_show, clicking
    if benutzer_show:
        if clicking:
            pass
        else:
            benutzer_off()
            benutzer_button.config(image=münzen_bild_10)
    else:
        if clicking:
            pass
        else:
            benutzer_on()
            benutzer_button.config(image=münzen_bild_25)

    benutzer_show = not benutzer_show
#Benutzer_ende----------------------------------------->
#Menüs----------------------------------------->

days = 0
hours = 0
minutes = 0
seconds = 0
def menü_on():
    if clicking:
       pass
    else:
        click_sound_buttons()
        benutzer_button.place_forget()
        rollen_frame.place(x=0, y=0, width=550, height=800)
        menü_button.lift()
        music_toggle_button.place(x=200, y=300, width=30, height=30)
        music_toggle_button.lift()
        clicks_label.place(x=200, y=340)
        clicks_label.lift()
        benutzername_frame.place_forget()
        sound_toggle_button.place(x=240, y=300, width=30, height=30)
        highscore_label.place(x=200, y=370)
        time_label.place(x=200, y=400)
        time_label.config(text=f"Zeit: {days:02}:{hours:02}:{minutes:02}:{seconds:02}")

def menü_off():
    if clicking:
        pass
    else:
        click_sound_buttons()
        benutzer_button.place(x=455, y=0, width=95, height=95)
        menü_button.place(x=0, y=0, width=95, height=95)
        music_toggle_button.place_forget()
        rollen_frame.place_forget()
        clicks_label.place_forget()
        benutzername_frame.place(x=100, y=200)
        sound_toggle_button.place_forget()
        highscore_label.place_forget()
        time_label.place_forget()

menü_show = False

def toggle_menü():
    global menü_show, clicking
    if menü_show:
        if clicking:
            pass
        else:
            menü_off()
            menü_button.config(image=münzen_bild_10)
    else:
        if clicking:
            pass
        else:
            menü_on()
            menü_button.config(image=münzen_bild_25)

    menü_show = not menü_show

#Menüs ende----------------------------------------->
#Verlieren----------------------------------------->
def verlieren():
    if coins <= 0:
        verlieren_frame.place(x=0, y=0, width=550, height=800)
        verlieren_ent()
        menü_button.place_forget()
        benutzer_button.place_forget
    else:
        pass

def verlieren_ent():
    global verlieren_button_frame
    verlieren_button_frame = tk.Frame(root, bg="#000000")
    verlieren_button_frame.place(x=150, y=670)

    verlieren_button = tk.Button(verlieren_button_frame, command=exit_game, text="Beenden", font=("Arial", 20), bg="#D3CDB8")
    verlieren_button.grid(row=0, column=0)

    nochmal_button = tk.Button(verlieren_button_frame, command=nochmal, text="Nochmal", font=("Arial", 20), bg="#D3CDB8")
    nochmal_button.grid(row=0, column=1)

def nochmal():
    global coins, verlieren_frame
    coins = 100
    coins_label.config(text=f"{coins}")
    text_label.config(text="Was willst du setzen?")
    verlieren_frame.pack_forget()
    verlieren_button_frame.place_forget()
    start()
    main()
    
#Verlieren Ende----------------------------------------->
#animation--------------------->
#1---
animation = False
def start_animation():
    global animation
    def update_label():
        if animation:
            global animation_number
            animation_number = random.randint(1, 9)
            zufallszahlen_label_1.config(text=f"{animation_number}")
            root.after(50, update_label)

    animation = True
    update_label()

def stop_animation():
    global animation
    animation = not animation
#2----
animation_2 = False
def start_animation_2():
    global animation_2
    def update_label_2():
        if animation_2:
            global animation_2_number
            animation_2_number = random.randint(1, 9)
            zufallszahlen_label_2.config(text=f"{animation_2_number}")
            root.after(50, update_label_2)

            
    animation_2 = True
    update_label_2()

def stop_animation_2():
    global animation_2
    animation_2 = not animation_2
#3----
animation_3 = False
def start_animation_3():
    global animation_3
    def update_label_3():
        if animation_3:
            global animation_3_number
            animation_3_number = random.randint(1, 9)
            zufallszahlen_label_3.config(text=f"{animation_3_number}")
            root.after(50, update_label_3)

    animation_3 = True
    update_label_3()

def stop_animation_3():
    global animation_3
    animation_3 = not animation_3
#4----
animation_4 = False
def start_animation_4():
    global animation_4
    def update_label_4():
        if animation_4:
            global animation_4_number
            animation_4_number = random.randint(1, 9)
            zufallszahlen_label_4.config(text=f"{animation_4_number}")
            root.after(50, update_label_4)

            
    animation_4 = True
    update_label_4()

def stop_animation_4():
    global animation_4
    animation_4 = not animation_4
#--------------------------------->
def format_coins(coins):
    if coins >= 1_000_000:
        return f"{str(coins / 1_000_000)[:4]}M"  # Millionenformatierung
    elif coins >= 1_000:
        return f"{str(coins / 1_000)[:4]}k"  # Tausenderformatierung
    else:
        return str(coins)

def anzeige_coins():
    global formatted_coins
    formatted_coins = format_coins(coins)
#Audio----------------------------------------->

def play_hintergrund_audio():
    pygame.mixer.music.load(r"musik\hintergrund_musik_test_neu.mp3")
    pygame.mixer.music.play(loops=100)


music_playing = False

def toggle_music():
    global music_playing
    if music_playing:
        pygame.mixer.music.stop()  # Sound stoppen
        music_toggle_button.config(text="Stop")
    else:
        pygame.mixer.music.play()  # Sound abspielen
        music_toggle_button.config(text="Play")
    music_playing = not music_playing

sounds_enabled = True

def click_sound_buttons():
    if sounds_enabled:
        click_sound = pygame.mixer.Sound(r"musik\klick_sound_1.mp3")
        click_sound.play()

def zahlen_click_sound():
    if sounds_enabled:
        zahlen_sound = pygame.mixer.Sound(r"musik\zahlen_sound.mp3")
        zahlen_sound.play()

def coins_click_sound():
    if sounds_enabled:
        coins_sound = pygame.mixer.Sound(r"musik\coins_click_sound_1.mp3")
        coins_sound.play()

def toggle_sound():
    global sounds_enabled
    sounds_enabled = not sounds_enabled
    if sounds_enabled:
        sound_toggle_button.config(text="Play")
    else:
        sound_toggle_button.config(text="Stop")
#Audio ende----------------------------------------->

random_number_1 = 0
random_number_2 = 0
random_number_3 = 0
random_number_4 = 0
#----------------------------------------->
#Coins&Benutzername
coins_frame = tk.Frame(root, bg="#D3CDB8")
coins_frame.place(x=334, y=204, width=130, height=30)

coins_label = tk.Label(coins_frame, text=f"{coins}", font=("Bodoni MT Black", 23), bg="#D3CDB8", fg="#000000")
coins_label.pack()
#---
benutzername_frame = tk.Frame(root)
benutzername_frame.place(x=100, y=200)

benutzername_label = tk.Label(benutzername_frame, text="", font=("Bodoni MT Black", 20), bg="#D3CDB8", fg="#000000")
benutzername_label.pack()
#----------------------------------------->
#Ist für allen anderen text
text_label = tk.Label(root, text=beispiel_text, font=("Berlin Sans FB Demi", 20), bg="#D3CDB8", fg="#000000")
text_label.place(x=95, y=460, width=370)
#----------------------------------------->
#Zufallszahlen Labels und Frames
number_frame_1 = tk.Frame(root)
number_frame_1.place(x=112, y=330, width=50, height=60)
#---
number_frame_2 = tk.Frame(root)
number_frame_2.place(x=205, y=330, width=50, height=60)
#---
number_frame_3 = tk.Frame(root)
number_frame_3.place(x=298, y=330, width=50, height=60)
#---
number_frame_4 = tk.Frame(root)
number_frame_4.place(x=393, y=330, width=50, height=60)
#---
zufallszahlen_label_1 = tk.Label(number_frame_1, text=f"{random_number_1}", font=("Bodoni MT Black", 60), bg="#D3CDB8", fg="#000000")
zufallszahlen_label_1.pack(pady=0)
#---
zufallszahlen_label_2 = tk.Label(number_frame_2, text=f"{random_number_2}", font=("Bodoni MT Black", 60), bg="#D3CDB8", fg="#000000")
zufallszahlen_label_2.pack(pady=0)
#---
zufallszahlen_label_3 = tk.Label(number_frame_4, text=f"{random_number_3}", font=("Bodoni MT Black", 60), bg="#D3CDB8", fg="#000000")
zufallszahlen_label_3.pack(pady=0)
#---
zufallszahlen_label_4 = tk.Label(number_frame_3, text=f"{random_number_4}", font=("Bodoni MT Black", 60), bg="#D3CDB8", fg="#000000")
zufallszahlen_label_4.pack(pady=0)
#----------------------------------------->

# Start Button
start_button = tk.Button(root, image=start__button, command=start_var, font=("Arial", 17), bg="#000000", relief="flat")
start_button.place(x=228, y=550, width=100, height=100)
#----------------------------------------->
# Zahlen Buttons
zehn_button = tk.Button(root, image=münzen_bild_10, command=taste_10, font=("Arial", 17), bg="#000000", relief="flat")
zehn_button.place(x=95, y=550, width=95, height=95)
#---
fünfundzwanzig_button = tk.Button(root, image=münzen_bild_25, command=taste_25, font=("Arial", 17), bg="#000000", relief="flat")
fünfundzwanzig_button.place(x=127, y=645, width=95, height=95)
#---
fünfzig_button = tk.Button(root, image=münzen_bild_50, command=taste_50, font=("Arial", 17), bg="#000000", relief="flat")
fünfzig_button.place(x=231, y=684, width=95, height=95)
#---
fünfundsiebzig_button = tk.Button(root, image=münzen_bild_75, command=taste_75, font=("Arial", 17), bg="#000000", relief="flat")
fünfundsiebzig_button.place(x=337, y=644, width=95, height=95)
#---
hundert_button = tk.Button(root, image=münzen_bild_100, command=taste_100, font=("Arial", 17), bg="#000000", relief="flat")
hundert_button.place(x=371, y=552, width=95, height=95)
#---
zwei_hundert_button = tk.Button(root, image=münzen_bild_100, command=taste_200, font=("Arial", 17), bg="#000000", relief="flat")
zwei_hundert_button.place(x=371, y=552, width=90, height=90)

fünf_hundert_button = tk.Button(root, image=münzen_bild_100, command=taste_500, font=("Arial", 17), bg="#000000", relief="flat")
fünf_hundert_button.place(x=371, y=552, width=90, height=90)

tausend_button = tk.Button(root, image=münzen_bild_100, command=taste_1000, font=("Arial", 17), bg="#000000", relief="flat")
tausend_button.place(x=371, y=552, width=90, height=90)

#----------------------------------------->
#Fuck it Button
#fuck_button = tk.Button(root, image=fuck_it, command=exit_game, font=("Arial", 17), bg="#000000", width=60, height=60, relief="flat")
#fuck_button.place(x=50 ,y=120)
#----------------------------------------->
#Seiten
seite_r_label = tk.Label(root, image=seite_r_rot, bg="#FFFFFF")
seite_r_label.place(x=510, y=0, width=30, height=800)

seite_l_label = tk.Label(root, image=seite_l_rot, bg="#FFFFFF")
seite_l_label.place(x=0, y=0, width=30, height=800)
#----------------------------------------->
#Menü&Benutzer
menü_button = tk.Button(root, image=münzen_bild_10, command=toggle_menü, font=("Arial", 17), bg="#000000", relief="flat")
menü_button.place(x=0, y=0, width=95, height=95)

benutzer_button = tk.Button(root, image=münzen_bild_10, command=toggle_benutzer, font=("Arial", 17), bg="#000000", width=50, height=50, relief="flat")
benutzer_button.place(x=455, y=550, width=95, height=95)
#----------------------------------------->
#Menü&Verlieren-Frames
rollen_frame = tk.Frame(root)
rollen_frame.place(x=0,y=0, width=550, height=800)

rolle_label = tk.Label(rollen_frame, image=rollen_bild)
rolle_label.pack()
#---
verlieren_frame = tk.Frame(root)
verlieren_frame.place(x=0 ,y=0, width=550, height=800)

verlieren_label = tk.Label(verlieren_frame, image=verlier_bild_kopf_oben)
verlieren_label.pack()
#----------------------------------------->
#Music&Sound_toggle_buttons
music_toggle_button = tk.Button(root, text="Play", command=toggle_music)
music_toggle_button.place(x=200, y=300, width=30, height=30)
#---
sound_toggle_button = tk.Button(root, text="Play", command=toggle_sound)
sound_toggle_button.place(x=240, y=300, width=30, height=30)
#----------------------------------------->
#Clicks Label----------------------------------------->
clicks_label = tk.Label(root, text=f"Clicks: {clicks_angezeigt}")
clicks_label.place(x=200, y=340)
#----------------------------------------->
#Highscore Label----------------------------------------->
highscore_label = tk.Label(root, text="Highscore: 0")
highscore_label.place(x=200, y=370)

# Label zur Anzeige der Zeit
time_label = tk.Label(root, text="Zeit: 00:00:00:00")
time_label.place()
#----------------------------------------->
#start variable



def start():
    global seite_l_label, seite_r_label
    zufallszahlen_label_1.config(text=" 0 ")
    zufallszahlen_label_2.config(text=" 0 ")
    zufallszahlen_label_3.config(text=" 0 ")
    zufallszahlen_label_4.config(text=" 0 ")
    seite_r_label.place_forget()
    seite_l_label.place_forget()

def main():
    öffne_zweites_fenster()
    benutzer_off()
    menü_on()
    menü_off()
    start()
    play_hintergrund_audio()
    verlieren_frame.place_forget()
    toggle_music()
    zwei_hundert_button.place_forget()
    fünf_hundert_button.place_forget()
    tausend_button.place_forget()
    check_for_500()
    
main()

root.mainloop()
