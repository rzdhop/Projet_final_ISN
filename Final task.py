#!/bin/bash
# -*- coding: utf-8 -*-

import PIL.Image, os, time
from tkinter import*
from tkinter.filedialog import *

class Dim_fen:
    def __init__(self, parent):
        global ecran_x, ecran_y
        parent.geometry("800x600+0+0")
        ecran_x = parent.winfo_screenwidth()
        ecran_y = parent.winfo_screenheight()
        fenetre_x = 800
        fenetre_y = 600
        posX = (ecran_x // 2) - (fenetre_x // 2)
        posY = (ecran_y // 2) - (fenetre_y // 2)
        geo =("{}x{}+{}+{}".format(fenetre_x,fenetre_y,posX,posY))
        parent.geometry(geo)
        parent.minsize(650,400)#taille min en x*y
        
    def ligne_sepa(self, parent):
        x1= ecran_x * 0.005
        x2= ecran_x * 0.9
        y1= 3
        y2= 2
        ligne_sepa = Canvas(parent,height = 10, width = 750)
        ligne_sepa.create_line(x1,y1,x2,y2,width=5,fill='grey')
        ligne_sepa.place(relx=0.5, rely=0.4, anchor=CENTER)

############################################################################################
def ImgToDecode(filepath):
    global fenetre_decode
    vi_pass = PIL.Image.open(filepath)
    vi_pass.thumbnail((100, 200))
    canvas = Canvas(fenetre_decode ,width=100, height=200,bg="red")
    canvas.place(relx = 0.4, rely= 0.5)
    vi_pass_can = PhotoImage(file=filepath)
    canvas.create_image(300, 200, image=vi_pass_can, anchor=NW)

def ImgToHide(filepath):
    global fenetre_encode
    vi_pass = PIL.Image.open(filepath)
    vi_pass.thumbnail((100, 200))
    canvas = Canvas(fenetre_encode ,width=100, height=200,bg="red")
    canvas.place(relx = 0.4, rely= 0.5)
    vi_pass_can = PhotoImage(file=filepath)
    canvas.create_image(300, 200, image=vi_pass_can, anchor=NW)

############################################################################################
def img_decode():
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.JPG')])
    if len(filepath) <= 1:
        pass
    else:
        ImgToDecode(filepath3)

def img_pass():
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.JPG')])
    if len(filepath) <= 1:
        pass
    else:
        ImgToHide(filepath)

def img_cont():
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.jpg')])
    if len(filepath) <= 1:
        pass
    else:
        pass
############################################################################################        
def Decode():
    global fenetre1, fenetre_decode
    fenetre_1.destroy()
    fenetre_decode = Tk()
    reglage = Dim_fen(parent = fenetre_decode)
    fenetre_decode.title("Decode by Rida and Yasin")
    #afficher l'image pour décripter
    Select_img = Button(fenetre_decode,text="Image a decoder",command = img_decode)
    Select_img.place(relx=0.5, rely=0.45,height= 50,width= 300, anchor=CENTER)
    #Bouton quitter
    boutton_quit = Button(fenetre_decode,text="Quitter", command = fenetre_decode.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_decode.mainloop()
       
def Encode():
    global fenetre1, fenetre_encode
    fenetre_1.destroy()
    fenetre_encode = Tk()
    reglage = Dim_fen(parent = fenetre_encode)
    fenetre_encode.title("Encode by Rida and Yasin")
    #afficher l'image pour décripter
    Select_img = Button(fenetre_encode,text="Image a cacher",command = img_pass)
    Select_img.place(relx=0.5, rely=0.3,height= 50,width= 300, anchor=CENTER)
    #afficher l'image conteneur
    Select_img2 = Button(fenetre_encode,text="image contenaire",command = img_cont)
    Select_img2.place(relx=0.5, rely=0.5,height= 50,width= 300, anchor=CENTER)
    #afficher une ligne de séparation
    reglage.ligne_sepa(parent = fenetre_encode)
    #Bouton quitter
    boutton_quit = Button(fenetre_encode,text="Quitter", command = fenetre_encode.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_encode.mainloop()
    
############################################################################################
def commencement():
    global fenetre_1
    fenetre_1 = Tk()
    fenetre_1.title("Stéganoraphie by Rida and Yasin")
    reglage = Dim_fen(parent = fenetre_1)
    #afficher l'image pour décripter
    Select_img = Button(fenetre_1,text="Encode",command = Encode)
    Select_img.place(relx=0.5, rely=0.3,height= 50,width= 300, anchor=CENTER)
    #afficher l'image conteneur
    Select_img2 = Button(fenetre_1,text="Decode",command = Decode)
    Select_img2.place(relx=0.5, rely=0.5,height= 50,width= 300, anchor=CENTER)
    #afficher une ligne de séparation
    reglage.ligne_sepa(parent = fenetre_1)
    #Bouton quitter
    boutton_quit = Button(fenetre_1,text="Quitter", command = fenetre_1.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_1.mainloop()


if __name__ == "__main__":
    commencement()
############################################################################################
