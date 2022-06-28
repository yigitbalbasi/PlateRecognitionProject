# mezuniyetPlakaTanima
Mezuniyet projemin yazılımı

Özet:


Gereksinimler:

OpenALPR kütüphanesi
Kamera  

//proje içerisinde laptop built-in kamera kullanılmıştır. 
//Harici kamera kullanımı için videoCek.py dosyası içerisindeki cv2.CaptureVideo() komudunun parametresi değiştirilmelidir.

OpenALPR kütüphanesinin kurulu olduğu dizin içerisinde 

                                          cikislar/output
                                          girisler
                                          
                                                        adlara sahip dizinleri oluşturmalıyız.

videoCek.py dosyası ubuntu konsol üzerinden "python3 videoCek.py" şeklinde çağırıldığında çalışmaya başlamaktadır. 
Kameradan çekilen görüntüler kare kare ayrıştırılıp openalpr/cikislar/output dizinine kaydedilmektedir. 
Bu dizin içerisinden işlenmesini istediğimiz kareyi seçip openalpr/girisler dizinine dosyayı kopyalayıp 
dosyanın adını "1.jpg" olarak değiştirmek gerekmektedir.
Programın son aşamasını çalıştırmak için ubuntu konsol üzerinde "python3 resimOkuma.py" kodu çalıştırıldığında plaka okuma işlemi yapmaktadır.
