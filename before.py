#!/bin/bash

# -*- coding: utf-8 -*-
import PIL.Image, os, time
from tkinter import*
from tkinter.filedialog import *



def progress_destega(currentValue):
    maxValue=100
    progressbar["value"]=currentValue

def de_stega():
    global filepath,filepath2, fenetre_2
    im_pass = PIL.Image.open(filepath)
    im_destega = PIL.Image.open(filepath3)
    width_pass, height_pass = im_pass.size #(x,y)
    width_cont, height_cont = im_destega.size #(x,y)
    if width_pass >= width_cont or height_pass >= height_cont:
        resize_pass = width_cont, height_cont
        resize_cont = width_cont*2, height_cont*2
        im_pass.thumbnail(resize_pass)
        im_destega.thumbnail(resize_cont)
    for x in range(width_pass):
        for y in range(height_pass):
            progress = (x/width_pass)*100
            try:
                value_test = im_pass.getpixel((x,y))# form RGBA ==> rouge vert bleu Alpha(= Opacity)
                value_test2 = im_destega.getpixel((x,y))
            except IndexError:
                pass
            RGB_pass = []
            RGB_cont = []
            for i in value_test:
                tmp = str(format(i, "08b"))
                tmp2 = tmp[4:]
                RGB_pass.append(tmp2)
            for j in value_test2:
                tmp = str(format(j, "08b"))
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
            print("Progression -> {}/{}".format(int(progress), 100))
            try:
                im_destega.putpixel((x,y),tuple_RGB)
            except IndexError:
                pass
    fenetre_3.destroy()
    im_cont.save("image destega.png", quality=100)
    im_destega.show()
    
def Threading():
    if de_stega_cond.get() == True:
        var1 = thread(pre_destega, de_stega)
    elif de_stega_cond.get() == False:
        var2 = thread(pre_stega, Stega)
    else: 
        print("Nique ta mere")
def Stega():
    global filepath,filepath3, fenetre_2
    im_pass = PIL.Image.open(filepath)
    im_cont = PIL.Image.open(filepath2)
    width_pass, height_pass = im_pass.size #(x,y)
    width_cont, height_cont = im_cont.size #(x,y)
    if width_pass >= width_cont or height_pass >= height_cont:
        resize_pass = width_cont, height_cont
        resize_cont = width_cont*2, height_cont*2
        im_pass.thumbnail(resize_pass)
        im_cont.thumbnail(resize_cont)
    for x in range(width_pass):
        for y in range(height_pass):
            progress = (x/width_pass)*100
            try:
                value_test = im_pass.getpixel((x,y))# form RGBA ==> rouge vert bleu Alpha(= Opacity)
                value_test2 = im_cont.getpixel((x,y))
            except IndexError:
                pass
            RGB_pass = []
            RGB_cont = []
            for i in value_test:
                tmp = str(format(i, "08b"))
                tmp2 = tmp[4:]
                RGB_pass.append(tmp2)
            for j in value_test2:
                tmp = str(format(j, "08b"))
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
            print("Progression -> {}/100".format(int(progress)))
            try:
                im_cont.putpixel((x,y),tuple_RGB)
            except IndexError:
                pass
    fenetre_2.destroy()
    im_cont.save("image contenaire.png", quality=100)
    im_cont.show()
    
def pre_stega():
    global fenetre_1, geo2, fenetre_2
    fenetre_2 = Toplevel(fenetre_1)
    fenetre_2.title("Loading...")
    fenetre_2.geometry(geo2)
    Label_waiting = Label(fenetre_2, text="Patientez pendant que le programme Cache l'image....").pack()
    fenetre_2.mainloop()
    
def pre_destega():
    global fenetre_1, geo2, fenetre_3
    fenetre_3 = Toplevel(fenetre_1)
    fenetre_3.title("Loading...")
    fenetre_3.geometry(geo2)
    Label_waiting = Label(fenetre_3, text="Patientez pendant que le programme retrouve l'image....").pack()
    fenetre_3.mainloop()
def valid_imgpass():
    global filepath,check_selected,Select_img, fenetre_1, de_stega_cond
    print(de_stega_cond.get())
    name, ext = os.path.splitext(filepath)
    vi_pass = PIL.Image.open(filepath)
    vi_pass.thumbnail((100, 100))
    canvas1 = Canvas(fenetre_1,width=150, height=150,bg="red")
    canvas1.place(relx = 3, rely= 0.05)
    vi_pass_can = PhotoImage(file=filepath)
    canvas1.create_image(100, 100, image=vi_pass_can, anchor=NW)

    selected_img_pass_label = Label(fenetre_1,text="Img pass selected").place(relx= 0.5, rely= 0.25,anchor=CENTER)
    Select_img.destroy()
    check_selected += 1
    if check_selected == 2:
        if de_stega_cond.get() == True:
            time.sleep(0.3)
            Select_img3 = Button(fenetre_1,text="selectionnez une image steganographié",command = img_de_stega)
            Select_img3.place(rely= 0.4, relx= 0.5, height= 50, width= 300, anchor=CENTER)
        elif de_stega_cond() == False:
            time.sleep(0.3)
            Threading()
    else:
        pass
        
def valid_imgcont():
    global filepath2,check_selected,Select_img2, de_stega_cond
    print(de_stega_cond.get())
    selected_img_cont_label = Label(fenetre_1,text="Img cont selected").place(relx= 0.5, rely= 0.55,anchor=CENTER)
    Select_img2.destroy()
    check_selected += 1
    if check_selected == 2:
        if de_stega_cond.get() == True:
            time.sleep(0.3)
            Select_img3 = Button(fenetre_1,text="selectionnez une image steganographié",command = img_de_stega)
            Select_img3.place(rely= 0.4, relx= 0.5, height= 50, width= 300, anchor=CENTER)
        elif de_stega_cond.get() == False:
            time.sleep(0.3)
            Threading()
    else:
        pass
def valid_img_destega():
    global de_stega_cond
    if check_selected == 2:
        if de_stega_cond == True:
            time.sleep(0.3)
            Select_img3 = Button(fenetre_1,text="selectionnez une image steganographié",command = img_de_stega)
            Select_img3.place(rely= 0.4, relx= 0.5, height= 50, width= 300, anchor=CENTER)
        elif de_stega_cond == False:
            time.sleep(0.3)
            Threading()
    else:
        pass
def img_de_stega():
    global filepath3, de_stega_bout
    filepath3 = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.jpg')])
    if len(filepath2) <= 1:
        pass
    else:
        de_stega_bout.destroy()
        Threading()
def img_cont():
    global filepath2
    filepath2 = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.jpg')])
    if len(filepath2) <= 1:
        pass
    else:
        valid_imgcont()
def img_pass():
    global filepath
    filepath = askopenfilename(title="Choisissez l'image",filetypes=[('png files','*.png'),('jpg files','*.JPG')])
    if len(filepath) <= 1:
        pass
    else:
        valid_imgpass()
def dimention_fen():
    global ecran_x, geo2, fenetre_1
    #dimension et emplacement de la fentre au lancement du programme
    fenetre_1.geometry("800x600+0+0")
    ecran_x = fenetre_1.winfo_screenwidth()
    ecran_y = fenetre_1.winfo_screenheight()
    fenetre_x = 800
    fenetre_y = 600
    posX = (ecran_x // 2) - (fenetre_x // 2)
    posY = (ecran_y // 2) - (fenetre_y // 2)
    geo =("{}x{}+{}+{}".format(fenetre_x,fenetre_y,posX,posY))
    fenetre_1.geometry(geo)
    fenetre_1.minsize(650,400)#taille min en x*y
    fenetre_x = 300
    fenetre_y = 150
    geo2 =("{}x{}+{}+{}".format(fenetre_x,fenetre_y,int(posX+posX/2),int(posY+posY/2)))
    
def commencement():
    global ecran_x,check_selected, fenetre_1, Select_img, Select_img2, de_stega_cond, de_stega_bout
    check_selected = 0
    fenetre_1 = Tk()
    fenetre_1.title("Stéganoraphie by Rida and Yasin")
    dimention_fen()
    de_stega_cond = BooleanVar()
    de_stega_bout = Checkbutton(fenetre_1, onvalue=True, offvalue=False, text="Retrouver votre image", variable=de_stega_cond)
    de_stega_bout.place(rely= 0.1, relx= 0.5, height= 50, width= 300, anchor=CENTER)
    #afficher l'image pour décripter
    Select_img = Button(fenetre_1,text="selectionnez une image pass",command = img_pass)
    Select_img.place(relx=0.5, rely=0.3,height= 50,width= 300, anchor=CENTER)
    #afficher l'image conteneur
    Select_img2 = Button(fenetre_1,text="selectionnez une image cont",command = img_cont)
    Select_img2.place(relx=0.5, rely=0.5,height= 50,width= 300, anchor=CENTER)
    #afficher une ligne de séparation
    x1= ecran_x * 0.005
    x2= ecran_x * 0.9
    y1= 3
    y2= 2
    ligne_sepa = Canvas(fenetre_1,height = 10, width = 750)
    ligne_sepa.create_line(x1,y1,x2,y2,width=5,fill='grey')
    ligne_sepa.place(relx=0.5, rely=0.4, anchor=CENTER)
    #Bouton quitter
    boutton_quit = Button(fenetre_1,text="Quitter", command = fenetre_1.destroy).place(relx=0.85, rely=0.85,width= 100, height= 50, anchor=CENTER)
    fenetre_1.mainloop()
if __name__ == "__main__":
    commencement()
