from tkinter import *  
from PIL import ImageTk, Image

  
root = Tk()      
#pencere oluştur
canvas = Canvas(root, width = 700, height = 550)      
canvas.pack()      



#baslık
root.title('Sonuçlar')
l = Label(root, text="Plaka Sonuçları")
l.config(font=("Verdana", 20, "bold"))  

#sonuc ekranı
T = Text(root, height=10, width=50)
T.config(font=("Verdana", 14))
sonuc="konsol sonucları"

#text'ten veri çekme kodu
f = open("console.txt", "r")
data = f.read()
sonuc=data

#widgetleri gosterir
#resimleri gösterir
#	------------------------------------------
#	------------------------------------------
#	------------------------------------------
img = ImageTk.PhotoImage(Image.open("cikislar/standartBoyResim.jpg"))
#	------------------------------------------
#	------------------------------------------
#	------------------------------------------
canvas.create_image(30,5, anchor=NW, image=img)  
#plakaSonuclari- başlıgı gösterir
l.pack()
#sonucları gösterir
T.pack()

#text ekleme kodu
T.insert(END, sonuc)
root.mai
