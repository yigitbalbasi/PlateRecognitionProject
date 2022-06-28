import sys
import cv2
import pytesseract
import os
import numpy as np
import contextlib 


#	okunacak  resmin adı
#	-----------------
#	-----------------
#	-----------------
resimAdi='girisler/1.jpg'
#	-----------------
#	-----------------
#	-----------------
resim=cv2.imread('{}'.format(resimAdi))

#okunacak resmi gösteriyor
cv2.imshow('resim',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

#boyutu düzenliyor
genislik= 650
yukseklik  = 500 
dim = (genislik, yukseklik)
resizedResim = cv2.resize(resim,dim, interpolation = cv2.INTER_AREA)

#yeni halini gösteriyor
cv2.imshow('resizedFoto',resizedResim)
cv2.waitKey(0)
cv2.destroyAllWindows()
#yeni hali kaydediyor
cv2.imwrite('cikislar/standartBoyResim.jpg', resizedResim)

def yazdir():
	os.system("alpr -c eu '{}' >> console.txt".format(resimAdi))



with open('console.txt','w') as f:
    with contextlib.redirect_stdout(f):
        yazdir()
 
import arayuz

exit()

