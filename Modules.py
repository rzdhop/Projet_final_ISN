from tkinter import*

def ToBinary(nombre):
    var2 = nombre
    var1 = ""
    while var2 > 0:
        var1 = str(var2 % 2) + str(var1)
        var2 = var2 // 2
    if len(var1) != 8:
        for i in range(8 - len(var1)):
            var1 = "0" + str(var1)
    return var1
    
class Dim_fen:
    def __init__(self):
        pass
    def sized(self, parent):
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
