from tkinter import *
from PIL import ImageTk, Image

class App:  #Création de la classe servant principalement à utiliser des variables golobales
    def __init__(self):
        self.config_parking = Tk()                          #Création de la 1ère fenêtre
        self.config_parking.geometry("300x120")
        self.config_parking.bind("<Return>", self.valider)
        self.config_parking.focus_force()
        self.entry = Entry(self.config_parking)             #Création de la barre de saisie
        self.entry.place(x = 25, y = 80)
        self.entry.focus()
        Label(self.config_parking, text = "OU").place(x = 155, y = 50)
        self.config_groupe = Button(self.config_parking, text = "Config du groupe", command = self.config_gr)
        self.config_groupe.place(x = 180, y = 50)

        #Initialisation des variables
        self.park_config = []
        self.n = 0
        self.n_bis = 0
        self.n_ter = 0

        #Lancement de fonction pour le demande de disposition
        self.start()


        self.config_parking.mainloop()

    def start(self): #Fonction servant à afficher le bon message en fonction du niveau de la disposition
        if self.n == 0: #Question du niveau
            self.ask = Label(self.config_parking, text = "Veuillez saisir le nombre \n de niveaux du parking")
            self.ask.place(x = 20, y = 30)
        elif self.n == 1:#Question de l'alléee
            self.ask['text'] = "Veuillez saisir le nombre d'allées par niveau"
            self.ask_bis = Label(self.config_parking, text = "niveau {}".format(self.n_bis))
            self.ask_bis.place(x = 20, y = 45)
        elif self.n == 2:#Question des places
            self.ask['text'] = "Veuillez saisir le nombre de places par allée et par niveau"
            self.ask_bis = Label(self.config_parking, text =  "niveau {} allée N° {}".format(self.n_bis, self.n_ter))
            self.ask_bis.place(x = 20, y = 45)
        elif self.n ==3:#A la fin on appelle la fonction parking afin de lancer la fonction principale
            self.parking()

    def valider(self,event = None): #Fonction appellée à chaque appuis sur la touche entrée
                                    #Elle permet de vérifier l'entrée de la saisie et de l'enregistrer
        if int(self.entry.get()) < 0:
            return False
        else:
            if self.n == 0:
                for i in range(int(self.entry.get())):
                    self.park_config.append(list())    #On ajoute le nombre de niveaux

            elif self.n == 1:
                if self.n_bis != len(self.park_config):
                    for i in range(int(self.entry.get())):
                        self.park_config[self.n_bis].append(list()) #On ajoute le nombre d'allée par niveau
                    self.allee_par_niveau()
                    self.ask_bis.destroy()
                    self.n-=1

            elif self.n == 2:
                for i in range(int(self.entry.get())):
                    self.park_config[self.n_bis][self.n_ter].append(0) #On ajoute le nombre de places par allée et par niveau
                self.place_par_allee()
                self.ask_bis.destroy()
                self.n-=1

        self.n+=1
        self.start()

    def allee_par_niveau(self): #Définit à quel niveau on est
        if self.n_bis == len(self.park_config)-1:
            self.n+=1
            self.n_bis = 0
        elif self.park_config[self.n_bis] != []:
            self.n_bis +=1

    def place_par_allee(self): #Définit danq quelle allée on est
        if self.n_ter == len(self.park_config[self.n_bis])-1:
            if self.n_bis == len(self.park_config)-1:
                self.n+=1
            else:
                self.n_bis+=1
                self.n_ter = 0
        elif self.park_config[self.n_bis][self.n_ter] != []:
            self.n_ter+=1

    def config_gr(self): #Fonction appellée si on lance la config par défault, on saute alors les 1eres fonctions
        self.park_config = [[[0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0]],[[0,0,0,0,0,0]],[[0,0,0,0,0]]]
        self.parking()

    def parking(self):
        self.config_parking.destroy()
        self.parking_visu = Tk()    #Création de la fenêtre principale (parking)
        self.parking_visu.geometry("1020x600")
        image_de_fond_right = ImageTk.PhotoImage(Image.open("image_de_fond_right.jpg"))
        image_de_fond_left = ImageTk.PhotoImage(Image.open("image_de_fond_left.jpg"))
        image_de_fond_bottom = ImageTk.PhotoImage(Image.open("image_de_fond_bottom.jpg"))

        self.parking_visu.focus_force()

        ########------------Frames Pricipaux-------------########################################
        self.Frame_Top  = Frame(self.parking_visu, width = 520, height = 80)
        self.Frame_center = Frame(self.parking_visu, width = 520, height = 460, bg = 'lightgrey')
        self.Frame_right = Canvas(self.parking_visu, width = 250, height = 600, bg = 'red')
        self.Frame_left = Canvas(self.parking_visu, width = 250, height = 600, bg = 'green')
        self.Frame_bottom = Canvas(self.parking_visu, width = 520, height = 80, bg = 'yellow')

        self.canvas_dessin = Canvas(self.Frame_center, width = 520, height = 460)

        #######-----------Package des Frames-------------##################################
        self.Frame_right.pack(side = RIGHT)
        self.Frame_left.pack(side = LEFT)
        self.Frame_bottom.pack(side = BOTTOM)
        self.Frame_center.pack(side = BOTTOM)
        self.Frame_Top.pack(side = TOP)
        self.canvas_dessin.pack()

        #########------------Labels et autres-----------##################################

        self.Frame_right.create_image(75, 300, image = image_de_fond_left)
        self.Frame_left.create_image(180, 300, image = image_de_fond_right)
        self.Frame_bottom.create_image(260, 75, image = image_de_fond_bottom)

        self.Button_come = Button(self.Frame_left,relief = GROOVE, text = "Choisir une place", font = ("Helvetica", 10), cursor ='hand2',command = lambda: self.choice_level(0))
        self.Button_come.place(x = 70, y = 20)

        self.Button_leave = Button(self.Frame_right, relief = GROOVE, text = 'Quitter une place',font = ("Helvetica", 10), cursor ='hand2',command = lambda:self.choice_level(1))
        self.Button_leave.place(x = 70, y = 20)

        self.Button_valider = Button(self.Frame_bottom, relief = GROOVE, text = 'Valider',font = ("Helvetica", 10), cursor ='hand2',command = self.execution)
        self.Button_valider['state'] = DISABLED
        self.Button_valider.place(x = 30, y = 20)

        self.affichage_resume =  Label(self.Frame_bottom, text = "Niveau   Allée n°   Place n°")
        self.affichage_resume.place(x = 185, y = 20)

        self.Button_annuler = Button(self.Frame_bottom, relief = GROOVE, text = 'Annuler',font = ("Helvetica", 10), cursor ='hand2',command = self.annuler)
        self.Button_annuler.place(x = 430, y = 20)

        ############################-----Valeurs par défault----####################################
        self.selected_mode = 0
        self.selected_mode_2 = 0
        self.selected_mode_3 = 0
        self.nb_places = 0
        self.text_error = ["Aucune place n'est libre,\n veuillez en libérer une.","Aucune place n'a encore été prise,\n veuillez en choisir une."]
        self.Frame_mod = [self.Frame_left,self.Frame_right]
        for i in self.park_config:
            for j in i:
                self.nb_places += len(j) #Nombre de places

        self.place_free = Label(self.Frame_Top, text = 'Places restantes: {}'.format(self.nb_places))
        self.place_free.pack()
        self.dessin()

        self.parking_visu.mainloop()


    #Les 4 fonctions servent à afficher les listbox et ainsi proposer les choix des places disponibles ou non

    def choice_level(self,mod): #Listbox pour le niveau
        try:
            self.affichage_error.destroy()
        except: pass
        self.annuler()

        self.mod = mod

        self.listbox_1 = Listbox(self.Frame_mod[self.mod], width = 10, height = 5)
        self.listbox_1.place(x = 60, y = 200)
        self.listbox_1.bind("<ButtonRelease-1>", self.choice_allee)
        self.info_niv = Label(self.Frame_mod[self.mod], text = 'Niveau:')
        self.info_niv.place(x = 125, y = 200)

        choix = list(set(self.valid_choice(0)[self.mod]))
        if choix != []:
            for elt in choix:
                self.listbox_1.insert(END, elt)
        else:
            self.listbox_1.destroy()
            self.info_niv.destroy()
            self.affichage_error =  Label(self.Frame_mod[self.mod], text = self.text_error[self.mod], font = ("Helvetica", 10), fg = "red")
            self.affichage_error.place(x = 10, y = 50)

    def choice_allee(self,event = None): #Listbox pour l'allée
        try:       #On essaye de détruire les listbox d'après au cas où elles soient déjà apparentes
            self.listbox_2.destroy()
            self.info_allee.destroy()
            self.listbox_3.destroy()
            self.info_place.destroy()
        except: pass

        self.Button_valider['state'] = DISABLED
        a  = self.listbox_1.curselection() #On récupère la sélection de la listbox
        self.selected_mode = self.listbox_1.get(a)
        self.canvas_dessin.delete("all") #On efface tous le canvas
        self.dessin(self.selected_mode) #On redessine le canvas
        self.listbox_2 = Listbox(self.Frame_mod[self.mod], width = 10, height = 5)
        self.listbox_2.place(x = 60, y = 300)
        self.listbox_2.bind("<ButtonRelease-1>", self.choice_place)
        #####-----Actualisation des labels et autres-----######
        self.info_niv['text'] = 'Niveau: {}'.format(self.selected_mode)
        self.affichage_resume['text'] = "Niveau {}  Allée n°  Place n°".format(self.selected_mode)
        self.info_allee = Label(self.Frame_mod[self.mod], text = 'Allée:')
        self.info_allee.place(x = 125, y = 300)
        for elt in  list(set(self.valid_choice(1)[self.mod])):
            self.listbox_2.insert(END, elt) #Création des éléments de la listbox

    def choice_place(self, event = None): #Listbox pour la place
        try:  #On essaye de détruire les listbox d'après au cas où elles soient déjà apparentes
            self.listbox_3.destroy()
            self.info_place.destroy()
        except:pass
        self.Button_valider['state'] = DISABLED #On désactive le bouton
        a  = self.listbox_2.curselection() #On récupère la sélection de la listbox
        self.selected_mode_2 = self.listbox_2.get(a)
        self.listbox_3 = Listbox(self.Frame_mod[self.mod], width = 10, height = 5)
        self.listbox_3.place(x = 60, y = 400)
        self.listbox_3.bind("<ButtonRelease-1>", self.choice_end)
        #####-----Actualisation des labels et autres-----######
        self.info_allee['text'] = 'Allée n°{}'.format(self.selected_mode_2)
        self.affichage_resume['text'] = "Niveau {}  Allée n°{}  Place n°".format(self.selected_mode,self.selected_mode_2)
        self.info_place = Label(self.Frame_mod[self.mod], text = 'Place:')
        self.info_place.place(x = 125, y = 400)

        for elt in list(set(self.valid_choice(2)[self.mod])):
            self.listbox_3.insert(END, elt) #Création des éléments de la listbox

    def choice_end(self, event = None):
        a  = self.listbox_3.curselection() #On récupère la sélection de la listbox
        self.selected_mode_3 = self.listbox_3.get(a)
        #####-----Actualisation des labels et autres-----######
        self.info_place['text'] = 'Place n°{}'.format(self.selected_mode_3)
        self.affichage_resume['text'] = "Niveau {}  Allée n°{}  Place n°{}".format(self.selected_mode,self.selected_mode_2,self.selected_mode_3)
        self.Button_valider['state'] = NORMAL
        self.listbox_3.bind("<ButtonRelease-1>", self.affiche_info_place)

    def affiche_info_place(self, event = None):
        a  = self.listbox_3.curselection() #On récupère la sélection de la listbox
        self.selected_mode_3 = self.listbox_3.get(a)
        #####-----Actualisation des labels et autres-----######
        self.info_place['text'] = 'Place n°{}'.format(self.selected_mode_3)
        self.affichage_resume['text'] = "Niveau {}  Allée n°{}  Place n°{}".format(self.selected_mode,self.selected_mode_2,self.selected_mode_3)

    def valid_choice(self,n):  #Fonction qui permet de retourner la liste qu'il faut pour la listbox
                               #n sert à déterminer quel partie nous devons retourner
                               #Si la place = 0, elle est libre. Si la place = 1, elle est occupée.
        self.liste_niveau =[[],[]]
        self.liste_allee = [[],[]]
        self.liste_place = [[],[]]

        if n == 0:
            for niveau in range(len(self.park_config)):
                for allee in range(len(self.park_config[niveau])):
                    for place in range(len(self.park_config[niveau][allee])):
                        if self.park_config[niveau][allee][place] == 0:
                            self.liste_niveau[0].append(niveau)
                        elif self.park_config[niveau][allee][place] == 1:
                            self.liste_niveau[1].append(niveau)
            return self.liste_niveau #On retourne la liste des niveaux
        if n == 1:
            for allee in range(len(self.park_config[self.selected_mode])):
                for place in range(len(self.park_config[self.selected_mode][allee])):
                    if self.park_config[self.selected_mode][allee][place] == 0:
                        self.liste_allee[0].append(allee)
                    elif self.park_config[self.selected_mode][allee][place] == 1:
                        self.liste_allee[1].append(allee)
            return self.liste_allee #On retourne la liste des allées en fonction du niveau
        if n == 2:
            for place in range(len(self.park_config[self.selected_mode][self.selected_mode_2])):
                if self.park_config[self.selected_mode][self.selected_mode_2][place] == 0:
                    self.liste_place[0].append(place)
                elif self.park_config[self.selected_mode][self.selected_mode_2][place] == 1:
                    self.liste_place[1].append(place)
            return self.liste_place #On retourne la liste des places en fonction de l'allée et du niveau

    def execution(self): #Fonction appellée à chaque fois que l'on valide le changement d'état du parking

        #######--------Actualisation du nombre de places-------#########
        if self.mod == 0:
            self.park_config[self.selected_mode][self.selected_mode_2][self.selected_mode_3] = 1
            self.nb_places-=1

        elif self.mod == 1:
            self.park_config[self.selected_mode][self.selected_mode_2][self.selected_mode_3] = 0
            self.nb_places +=1

        self.place_free['text'] = 'Places restantes: {}'.format(self.nb_places)
        self.annuler()
        self.canvas_dessin.delete("all")
        self.dessin(self.selected_mode)

    def annuler(self): #Sert à revenir à zéro (Au niveau des listbox)
        try:  #On essaye de détruire les listbox d'après au cas où elles soient déjà apparentes
            self.listbox_1.destroy()
            self.info_niv.destroy()
            self.listbox_2.destroy()
            self.info_allee.destroy()
            self.listbox_3.destroy()
            self.info_place.destroy()
        except: pass
        self.Button_valider['state'] = DISABLED
        self.affichage_resume['text'] = "Niveau   Allée n°   Place n°"

    def dessin(self,niv = 0): #Fonction qui gère tout le dessin du parking
        max_places = 0
        nb_allee = len(self.park_config[niv])
        for allee in range(len(self.park_config[niv])):
            if len(self.park_config[niv][allee]) > max_places:
                max_places = len(self.park_config[niv][allee])
        r = 7 #Rayon du cercle

        self.canvas_dessin.create_text(260,10,text="Niveau: {}".format(niv),font = ("Helvetica", 15, "bold")) #Affichage de l'étage en cours

        #Dessin des traits droits verticaux
        for i in range(len(self.park_config[niv])+1):
            self.canvas_dessin.create_line(20+i*480/nb_allee, 20, 20+i*480/nb_allee, 420)

        #Dessin des traits droits horizontaux
        for i in range(len(self.park_config[niv])):
            for j in range(len(self.park_config[niv][i])+2):
                if j % 2 == 0:
                    self.canvas_dessin.create_line(20+i*480/nb_allee, 420 - (j//2)*2*400/(((max_places+1)//2)*2), 20+i*480/nb_allee+(480/nb_allee/3), 420 - (j//2)*2*400/(((max_places+1)//2)*2))

                else:
                    self.canvas_dessin.create_line(20+(i+1)*480/nb_allee, 420 - (j//2)*2*400/(((max_places+1)//2)*2), 20+(i+1)*480/nb_allee-(480/nb_allee/3),420 - (j//2)*2*400/(((max_places+1)//2)*2))

        #Dessin des cerlces (verts ou rouges) ainsi que le numéro de la place
        list_state = ['green','red']
        for i in range(len(self.park_config[niv])):
            for j in range(len(self.park_config[niv][i])):
                y0_trait =420 -  (j//2)*2*400/(((max_places+1)//2)*2)
                x1_trait_gauche = 20+i*480/nb_allee+(480/nb_allee/3)
                if j % 2 == 0:
                    self.canvas_dessin.create_oval(x1_trait_gauche - r, y0_trait - (2*400/(((max_places+1)//2)*2))/2- r, x1_trait_gauche + r, y0_trait - (2*400/(((max_places+1)//2)*2))/2+ r, fill = list_state[self.park_config[niv][i][j]])
                    self.canvas_dessin.create_text(20+i*480/nb_allee+(480/nb_allee/3)/2,y0_trait - (2*400/(((max_places+1)//2)*2))/2- r,text=j)
                else:

                    self.canvas_dessin.create_text(20+(i+1)*480/nb_allee-(480/nb_allee/3)/2,y0_trait - (2*400/(((max_places+1)//2)*2))/2- r,text=j)
                    self.canvas_dessin.create_oval(20+(i+1)*480/nb_allee-(480/nb_allee/3) - r, y0_trait - (2*400/(((max_places+1)//2)*2))/2- r, 20+(i+1)*480/nb_allee-(480/nb_allee/3) + r, y0_trait - (2*400/(((max_places+1)//2)*2))/2+ r, fill = list_state[self.park_config[niv][i][j]])
            self.canvas_dessin.create_text(20+(i+1/2)*480/nb_allee,440,text="Allée: {}".format(i))


a = App() #Appel de la classe
