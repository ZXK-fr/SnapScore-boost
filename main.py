try:
    from colorama import Fore, init
    import ctypes, pyautogui, keyboard, os, time, platform
    from datetime import datetime
    from pystyle import Colors, Colorate
except ImportError:
    input("Erreur : installe les modules du fichier requirements.txt")

init(autoreset=True)

ascii_text = Fore.YELLOW + """
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⡀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀    
⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⠀⠀⠀
⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠀⠀
⠀⠀⠀⠀⠈⠛⠛⠋⠙⠿⣿⣿⣿⣿⣿⣿⠿⠋⠙⠛⠛⠁⠀⠀⠀
"""

dedi = (Colorate.Horizontal(Colors.green_to_black, "SnapScore boost by Zxk"))
def sur_linux():
    return platform.system() == "Linux"

class snapchat:

    def __init__(self):
        self.snaps_envoyes = 0
        self.delai = 0.3
        self.debut = None

    def choper_positions(self):
        self.log("mets ta souris sur *caméra* et appuie sur G")
        self.bouton_camera = self.attendre_f()

        self.log("mets ta souris sur *prendre photo* et appuie sur G")
        self.bouton_photo = self.attendre_f()

        self.log("mets ta souris sur *envoyer à* et appuie sur G")
        self.bouton_envoyer_a = self.attendre_f()

        self.log("mets ta souris sur ton *raccourci* et appuie sur G")
        self.raccourci = self.attendre_f()

        self.log("mets ta souris sur *tout sélectionner* et appuie sur G")
        self.selectionner_tout = self.attendre_f()

        self.log("mets ta souris sur *envoyer snap* et appuie sur G")
        self.bouton_envoyer_snap = self.attendre_f()

    def attendre_f(self):
        while True:
            if keyboard.is_pressed("G"):
                pos = pyautogui.position()
                time.sleep(0.5)
                return pos

    def envoyer_snap(self, nb_personnes):
        self.mettre_titre(nb_personnes)
        pyautogui.moveTo(self.bouton_camera)
        pyautogui.click()
        time.sleep(self.delai)

        pyautogui.moveTo(self.bouton_photo)
        pyautogui.click()
        time.sleep(self.delai)

        pyautogui.moveTo(self.bouton_envoyer_a)
        pyautogui.click()
        time.sleep(self.delai)

        pyautogui.moveTo(self.raccourci)
        pyautogui.click()
        time.sleep(self.delai)

        pyautogui.moveTo(self.selectionner_tout)
        pyautogui.click()
        time.sleep(self.delai)

        pyautogui.moveTo(self.bouton_envoyer_snap)
        pyautogui.click()

        self.snaps_envoyes += 1
        self.mettre_titre(nb_personnes)

    def mettre_titre(self, nb_personnes):
        maintenant = time.time()
        passe = str(maintenant - self.debut).split(".")[0]
        total = self.snaps_envoyes * nb_personnes
        if not sur_linux():
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"SnapScore boost | Snaps envoyés : {total} | Temps : {passe}s | Dev : Zxk"
            )

    def log(self, txt):
        print(f"{Fore.BLUE}\n[{Fore.MAGENTA}Console{Fore.BLUE}] {txt}")

    def lancer(self):
        os.system("cls" if not sur_linux() else "clear")
        print(ascii_text)
        print(dedi)
        self.choper_positions()

        while True:
            try:
                nb_personnes = int(input(f"\n       {Fore.CYAN}[{Fore.MAGENTA}Console{Fore.CYAN}] combien de gens dans le raccourci ? "))
                break
            except ValueError:
                self.log("erreur, entre un vrai chiffre")

        self.log("PC lent = tape 1")
        self.log("PC rapide = tape 2")
        choix = input(f"\n       {Fore.CYAN}[{Fore.MAGENTA}Console{Fore.CYAN}] ton choix : ")
        if choix == "1":
            self.delai = 2

        self.log("va dans les chats et appuie sur G quand t’es prêt")
        while not keyboard.is_pressed("G"):
            pass

        os.system("cls" if not sur_linux() else "clear")
        print(ascii_text)
        self.log("ça envoie...")
        self.debut = time.time()

        while not keyboard.is_pressed("F4"):
            self.envoyer_snap(nb_personnes)
            time.sleep(4)

        self.log(f"fini d’envoyer {self.snaps_envoyes} snaps")

bot = snapchat()
bot.lancer()
