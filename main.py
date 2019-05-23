# -*- coding: utf-8 -*-

import PIL.Image, time
from tkinter import*
from tkinter.filedialog import *
from Modules import *

############################################################################################

def roleback1():
    global fenetre_EndEncode
    fenetre_EndEncode.destroy()
    commencement()

def roleback2():
    global fenetre_EndDecode
    fenetre_EndDecode.destroy()
    commencement()

############################################################################################

def EndEncode():
    global fenetre_encode, fenetre_EndEncode
    fenetre_encode.destroy()
    fenetre_EndEncode = Tk()
    reglage = Dim_fen().sized(parent= fenetre_EndEncode)    
    fenetre_EndEncode.title("Image Encoded !")
    EncodedPath = Label(fenetre_EndEncode, text="Image Encodée dans le meme dossier que le programme !").place(relx = 0.5, rely = 0.5, anchor=CENTER)
    boutton_comeback = Button(fenetre_EndEncode,text="Revenir au debut", command = roleback1).place(relx=0.15, rely=0.85,width= 120, height= 50, anchor=CENTER)
    boutton_quit = Button(fenetre_EndEncode,text="Quitter", command = fenetre_EndEncode.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_EndEncode.mainloop()

def EndDecode():
    global fenetre_encode, fenetre_EndDecode
    fenetre_decode.destroy()
    fenetre_EndDecode = Tk()
    reglage = Dim_fen().sized(parent= fenetre_EndDecode)    
    fenetre_EndDecode.title("Image Decoded !")
    EncodedPath = Label(fenetre_EndDecode, text="Image Décodée dans le meme dossier que le programme !").place(relx = 0.5, rely = 0.5, anchor=CENTER)
    boutton_comeback = Button(fenetre_EndDecode,text="Revenir au debut", command = roleback2).place(relx=0.15, rely=0.85,width= 120, height= 50, anchor=CENTER)
    boutton_quit = Button(fenetre_EndDecode,text="Quitter", command = fenetre_EndDecode.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_EndDecode.mainloop()

############################################################################################
def UnStegaProcess():
    global filepath
    ImgToRetreive = PIL.Image.open(filepath)
    width, height = ImgToRetreive.size #(x,y)
    for x in range(width):
        for y in range(height):
            try:
                value_test = ImgToRetreive.getpixel((x,y))# form RGBA ==> rouge vert bleu Alpha(= Opacity)
            except IndexError:
                pass
            RGB_pass = []
            RGB_destega = []
            for i in value_test:
                tmp = str(ToBinary(i))
                tmp2 = tmp[4:]
                RGB_pass.append(tmp2)
                tmp2 = tmp[:4]
                RGB_destega.append(tmp2)
            RGB_final = []
            RGB_final.append(RGB_pass[0] + RGB_destega[0])
            RGB_final.append(RGB_pass[1] + RGB_destega[1])
            RGB_final.append(RGB_pass[2] + RGB_destega[2])
            RGB_decimal = []
            for a in range(0,3):
                RGB_decimal.append(int(RGB_final[a],2))
            tuple_RGB = (RGB_decimal[0],RGB_decimal[1],RGB_decimal[-1])
            try:
                ImgToRetreive.putpixel((x,y),tuple_RGB)
            except IndexError:
                pass
    ImgToRetreive.save("Image Decoded.png", quality=100)
    print("Finished !")

def StegaProcess():
    global filepath, filepath2, fenetre_encode
    im_pass = PIL.Image.open(filepath)
    im_cont = PIL.Image.open(filepath2)
    width_pass, height_pass = im_pass.size #(x,y)
    width_cont, height_cont = im_cont.size #(x,y)
    for x in range(width_pass):
        for y in range(height_pass):
            try:
                value_test = im_pass.getpixel((x,y))# form RGBA ==> rouge vert bleu Alpha(= Opacity)
                value_test2 = im_cont.getpixel((x,y))
            except IndexError:
                pass
            RGB_pass = []
            RGB_cont = []
            for i in value_test:
                tmp = str(ToBinary(i))
                tmp2 = tmp[4:]
                RGB_pass.append(tmp2)
            for j in value_test2:
                tmp = str(ToBinary(j))
                tmp2 = tmp[:4]
                RGB_cont.append(tmp2)
            RGB_final = []
            RGB_final.append(RGB_cont[0] + RGB_pass[0])
            RGB_final.append(RGB_cont[1] + RGB_pass[1])
            RGB_final.append(RGB_cont[2] + RGB_pass[2])
            RGB_decimal = []
            for a in range(0,3):
                RGB_decimal.append(int(RGB_final[a],2))
            tuple_RGB = (RGB_decimal[0],RGB_decimal[1],RGB_decimal[-1])
            try:
                im_cont.putpixel((x,y),tuple_RGB)
            except IndexError:
                pass
    im_cont.save("Image Encoded.png", quality=100)
    EndEncode()
    
############################################################################################

def ImgToDecode(filepath):
    global fenetre_decode
    vi_pass = PIL.Image.open(filepath)
    canvas = Canvas(fenetre_decode ,width=100, height=200,bg="red")
    canvas.place(relx = 0.4, rely= 0.5)
    vi_pass_can = PhotoImage(file=filepath)
    canvas.create_image(300, 200, image=vi_pass_can, anchor=NW)
    time.sleep(0.3)
    UnStegaProcess()

def ImgToHide(filepath):
    global fenetre_encode, ValidStep
    vi_pass = PIL.Image.open(filepath)
    canvas = Canvas(fenetre_encode ,width=100, height=200,bg="red")
    canvas.place(relx = 0.4, rely= 0.5)
    vi_pass_can = PhotoImage(file=filepath)
    canvas.create_image(300, 200, image=vi_pass_can, anchor=CENTER)
    ValidStep += 1
    if ValidStep == 2:
        time.sleep(0.3)
        StegaProcess()

def ImgReceiver(filepath2):
    global fenetre_encode, ValidStep
    vi_pass = PIL.Image.open(filepath2)
    canvas = Canvas(fenetre_encode ,width=100, height=200,bg="red")
    canvas.place(relx = 0.4, rely= 0.5)
    vi_pass_can = PhotoImage(file=filepath2)
    canvas.create_image(300, 200, image=vi_pass_can, anchor=CENTER)
    ValidStep += 1
    if ValidStep == 2:
        time.sleep(0.3)
        StegaProcess()

############################################################################################

def img_decode():
    global Select_img, filepath
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.JPG')])
    if len(filepath) <= 1:
        pass
    else:
        Select_img.destroy()
        ImgToDecode(filepath)

def img_pass():
    global Select_img, filepath
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.JPG')])
    if len(filepath) <= 1:
        pass
    else:
        Select_img.destroy()
        ImgToHide(filepath)

def img_cont():
    global Select_img2, filepath2
    filepath2 = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.jpg')])
    if len(filepath2) <= 1:
        pass
    else:
        Select_img2.destroy()
        ImgReceiver(filepath2)
############################################################################################  

def Decode():
    global fenetre1, fenetre_decode, Select_img
    fenetre_1.destroy()
    fenetre_decode = Tk()
    reglage = Dim_fen()
    reglage.sized(parent= fenetre_decode)
    fenetre_decode.title("Decode by Rida and Yasin")
    #afficher l'image pour décripter
    Select_img = Button(fenetre_decode,text="Image a decoder",command = img_decode)
    Select_img.place(relx=0.5, rely=0.45,height= 50,width= 300, anchor=CENTER)
    #Bouton quitter
    boutton_quit = Button(fenetre_decode,text="Quitter", command = fenetre_decode.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_decode.mainloop()
       
def Encode():
    global fenetre1, fenetre_encode, Select_img, Select_img2, ValidStep
    ValidStep = 0
    fenetre_1.destroy()
    fenetre_encode = Tk()
    reglage = Dim_fen()
    reglage.sized(parent= fenetre_encode)
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
    reglage = Dim_fen()
    reglage.sized(parent= fenetre_1)
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
