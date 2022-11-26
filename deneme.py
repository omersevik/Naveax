from cgi import print_arguments, print_directory
from logging.config import listen
from string import printable
from turtle import Turtle


print('Hello, World!')

print('Merhaba devamı Burası Neresi ile bağlantılı bir kod \nBurası Neresi')

print('Benim adim \tÖmer')


print('Benim adım {}'.format('Ömer'))

print('Benim adım {}, yasim {}'.format('Ömer', 15))

print('Benim adım {0}, yasim {1}'.format('Ömer', 15))

print('Benim adım {1}, yasim {0}'.format('Ömer', 15))

print('Benim adım {ad}, yasim {yaş}'.format(ad='Ömer', yaş=15))

print('Benim adım {ad}, yasim {yaş}'.format(yaş=15, ad='Ömer'))


sayi = 10
print(sayi)

sayi = 11
print(sayi)





sayi = sayi + 1
print(sayi)

sayi = sayi - 1
print(sayi)

sayi = sayi / 2
print(sayi)

sayi = sayi * 2
print(sayi)

sayi = sayi % 5
print(sayi)





#1sayi = 10 hatalı nedeni değişkene başına sayı ekleyememiz python izin vermiyor
#print(1sayi) 

sayi1 = 20 #bu nu yapa bilirsin max sayı ekleyerek
print(sayi1)



#sayi ilk = 24
#print(sayi ilk)
#hatalı

sayi_ilk = 53
print(sayi_ilk)
#doğru




print(2+2)
print(2-4)
print(26+2*5-(2*6)/3)
print(3.1*2.0)
print(3.1*5)
print(3.0*5)


strvar = "Python"
print(strvar)

#strvar [-3]
#'h'

#strvar [2:]
#'thon'

#strvar [:3]
#'Pyt'

#strvar [2:5]
#'tho'

#strvar [::2]
#'Pto'

#strvar [1:5:3]
#'yo'



strvar = "Merhaba"
print(len(strvar)) # böyle yapabildim len nasıl dışarda kunlanıcam bilmiyorum


print(strvar + " ogrenlen!")

strvar = strvar + " ogren! " # strvarı kendine eşitledim
print(strvar)

strvar = strvar * 5 # bunu yanlız çalıştıramıyorum 'strvar * 5'
print(strvar)
print(strvar)

strvar = "Naber KnK WoW"
print(strvar.upper()) #büyütür tüm harfleri
print(strvar.lower()) #küçültür tüm harfleri
print(strvar.split()) #harfleri kareli paranteze alır hemde tırnak içine
print(strvar.split("W")) #hafr berileyip ayıra biliyoruz
print(strvar.split("r")) # //      //      //      //
print(strvar.split(sep="a", maxsplit=1))  #a harfini sildi


#bundan sonra boolean , bool elemanı nasıl kuınlanıldığı gösterilir

a = True # tırnaksız bool ifadesi taşır
print(type(a)) #bir true false ifadesini yazı olarak yazmak var bide gerçek anlamıyla yazmak var gerçek anlamıyla yazarsanız bool olur 
b = False #tırnaksız bool ifadesi taşır
print(a)
print(b)
c = 'True' #bu tırnaklı olunca yazı ifadesine dünüşüyor str oluyor bool ile bir alakası yok
print(c)
print(type(c))

#         |
#karışık \/

print('oguzhan' + '5')
print('oguzhan' + str(5))

print(float(15))
print(int(15.2))
print(15 * 15.8)
print(100 * ' oğuzhan ')
#print('oguzhan ' * 'Ömer ')

sayi = 2
sayi2 = 5
print(sayi * sayi2)


isim = 'Ömer'
soyisim = ' Şevik'
print(isim + soyisim)
print(isim)

isim = 'tayfun '
soyisim = 'erbilen'
print(isim + soyisim)

isim = 1
isimSoyisim = 2
isim_soyisim = 2
_isim = 1
ISIM = 1
isim1234 = 1
#4isim = 1 error SyntaxError: invalid syntax
#$deneme = 123 error SyntaxError: invalid syntax
#'deneme' = deasd error SyntaxError: cannot assign to literal
#isim soyisim = celiskarslan error SyntaxError: invalid syntax
#isim-soyisim = 'dasd' error SyntaxError: cannot assign to operator
 
print('Hello World!')
print('Oğuzhan')

#isim = input('Lütfen isim giriniz.')
#print(isim)


#cevap bekleniyor

#isim2 = input('isim giriniz:')
#soyisim = input('Soyisim giriniz:')
#yas = int(input('Yaş:'))

#print(isim + " " + soyisim + " " + yas) yanlış yas int oyüzden hata verir yası str yapıyoruz
#print(isim + " " + soyisim + " " + str(yas))
print('____________________________________________________')
print('____________________________________________________')
print('____________________________________________________')
print('____________________________________________________')
print('____________________________________________________')
# == ifadesi eşitliği temsil eder
# != eşit değilse demektir
# < küçüktür.
# <= küçük eşittir.
# >= büyük eşittir.


print(4 == 4)
print(4 != 4)
print(4 == 5)
print(4 != 5)
print(4 < 5)
print(5 > 4)
print(5 <= 4)
print(4 <= 5)
print(5 <= 5)
print(5 >= 4)
print(4 >= 5)
print(5 >= 5)

#True ve/and True = Doğrudur
#True ve/and False = Yanlıştır
#False ve/and True = Yanlıştır
#False ve/and False = Yanlıştır

#Ture or Ture = Doğrudur
#Ture or False = Doğrudur
#False or Ture = Doğrudur
#False or False = Yanlıştır
#not operatörü



#and ifadesi 2 tane değişken var ise 1 tanesi bile yanlış ise
#diyerkside doğru ise o yanlıştır bitanesinin yanlış olması 
#demek kompile bunu false yapar ve bu yanlış olur


#kullanici_adi = input('Kullanici Adi:')
#password = input('Password:')
#print(kullanici_adi == "Ömer" and password == "123456")



#or ifadesi 2tane değişken var ise 1tanesi doğru ise 
# diyerkiside yanlış ise o doğrudur bitanesinin doğru 
# olması yeterlidir.


#kullanici_adi2 = input('Kullanici Adi:')
#password2 = input('Password:')
#print(kullanici_adi2 == "Naber" or password2 == "1234")


#bu not ibaresi tamamen tam tersi çalışır and'tan yani not 
# burda sen istediğin kadar doğru gir o falsetır ama sen 
# yanlış gir o truedur

#kullanici_adi = input('Kullanici Adi:')
#print(not (kullanici_adi == "ömer"))



#if elif else kunlanımı

print('________________________________________')
print('________________________________________')
print('________________________________________')
print('________________________________________')

#basit bir fi elif else kodu

#isim = "ömer"

#alinan_isim = input('isim:')

#if isim == alinan_isim:
#    print('Doğru bildiniz')

#elif alinan_isim =='oguz':
#    print('Doğru yaklaştınız')

#elif alinan_isim == "ogu":
#    print('dahada yaklaştınız')

#else:
#    print('Yanlış bildiniz.')



#while döngüsü while else kodu

#sayi = 0

#while sayi <= 5:
#    print(sayi)
#    sayi = sayi + 1
#else:
#    print(sayi)


#baslangic = 0
#baslangic1 = 0
#baslangic2 = 0


#while baslangic < 10:
#    if baslangic % 2 != 0:
#        print(baslangic)
#    baslangic = baslangic + 1

#print('___\n')

#while baslangic2 < 10:
#    if baslangic2 % 2 == 0:
#        print(baslangic2)
#    baslangic2 = baslangic2 + 1

#while baslangic1 < 10:
#    baslangic1 = baslangic1 + 1
#    if baslangic1 % 2 != 0:
#        continue #döngüyü sıfırlayıor
#    print(baslangic1)

#while True:
#    alinan = input('isim giriniz')
#    if alinan == 'cikis':
#        break # döngü kırıcı
#    print(alinan)

# listeler bölümüne geçtik

pazar_listesi = ['elma', 'ekmek', 'kayısı', 'zeytin', 'elma', 'elma']
esya_listesi = ['hırka', 'terlik']

print(pazar_listesi[0])
print(pazar_listesi[1])
print(pazar_listesi[2])
print(pazar_listesi[3])
print(pazar_listesi[-1])
print(pazar_listesi[-2])
print(pazar_listesi[-3])
print(pazar_listesi[-4])
print(pazar_listesi)

pazar_listesi.append('domates') # append listeye ekleme yapmaya sağlar
print(pazar_listesi)

yeni_list = pazar_listesi[1:4]
print(yeni_list)

yeni_list = pazar_listesi[1:]
print(yeni_list)

yeni_list = pazar_listesi[:2]
print(yeni_list)


print(pazar_listesi + esya_listesi) # lsiteye liste kelmek

#pazar_listesi.clear() #liste içindeki herşeyi isler
#print(pazar_listesi)

print((pazar_listesi.count('elma')))
print((pazar_listesi.index('ekmek')))

pazar_listesi.remove('ekmek') #ekmek öldürüldü
pazar_listesi.pop() # listenin son karakteri silndi
pazar_listesi.reverse() # liste ters döndürüldü
pazar_listesi.sort() # alfabeye göre sıralar

print(pazar_listesi)

#print(dir(esya_listesi))



# for döngüsü kodu

liste = ['elma', 'armut', 'kiraz']
rakam_listesi = [1,3,7,8,9]
rakam2_listesi2 = [1,2,3,4,5,6,7,8,9,10]

total = 0

#print(liste[0])
#print(liste[1])
#print(liste[2])

#for item in liste:
#    print(item)
#    print(item)

for rakam in rakam_listesi:
    total = total + rakam

print(total)




for rakam2 in rakam2_listesi2:
    print(rakam2)


print(list(range(10)))



for item in range(10):
    print(item)



for item in range(100):
    print(item)


for item in range(100): #çift sayılar yazdırır
    if sayi % 2 == 0:
        print(sayi)



for item in range(100): #tek sayılar yazdırır ama sadece 2 yazdırıyor :(
    if sayi % 2 == 1:
        print(sayi)


isim = "oguzhan"

print(isim[0])
print(isim[1])
print(isim[2])
print(isim[3])
print(isim[4])
print(isim[5])
print(isim[6])

for harf in isim:
    print(harf)




#sözlükler ders 14
#               |
#Doğru olmayan \/

#name = "Ömer"
#surname = "Şevik"

#name_2 = "Enes"
#surname = "Şahin"


#            |
#Doğru olan \/

person = {
    'isim': 'Oğuzhan',
    'soy_isim': 'bilmemne',
    'yas': 23
}

person_2 = {
    'isim': 'enes',
    'soy_isim': 'Şahin',
    'yas': 32
}

person_3 = dict(isim= 'hasan', soy_isim = 'tuncel', yas = 34)


# ekleme yapmayı sağlıyor

person['color'] = 'blue'

print(type(person))
print(type(person_2))
print(type(person_3))
print(person)
print(person_2)
print(person_3)

# sadece [bunu içindekileri consola veya terminal yazdırı]
print(person['soy_isim'])

#hatalı KeyError: 'yemek'
#print(person['yemek'])

if "yemek" in person:
    print(person['yemek'])
else:
    print('bu keye karşılık bir value bulunamadı.')

print(dir(person))
print(help(person.get))
print(person.get('yemek', False))
print(person.get('isim', False))
print(person.get('color', False))

print(person.items())

for element in person.items():
    print(element)
    print(element[0])
    print(element[1])

print("_____________________________________")


#             |
#abimin kodu \/

persons = [
    {
    'isim': "Yakup",
    'soy_isim': "Sevik",
    'yas': 20
    },
    {
    'isim': "Omer",
    'soy_isim': "Sevik",
    'yas': 15
}];

# Persons Array'i içerisinde bulunan 2 adet objeyi birlikte gösterir.
print(persons)

# Persons Array'inin içerisinde olan objeleri tek tek gösterir.
for person in persons:
    print(person)
    
# Persons Array'inin içerisinde olan objelerin içerisinden isim değerini gösterir.
for person in persons:
     print(person['isim'])

  

# abimin kodu /\
#             |






 #tuple örnek

for anahtar, deger in person.items():
         print(anahtar, "=", deger)



 #print(person.keys())
print("______________________________")


# direk cevabı verir
#çok mantıklı değil

#for key in person.keys():
#     print(person[key])

#aynı şeyi yapıyor forla
print(person.values())

#dağada temizi
for value in person.values():
     print()

person[123] = ["deneme", "prototurk", "OMG"]
print(person[123])

for value in person.keys():
    print(value)

#sözlük veri yapsını yukarda anlatılkıyor




#tuple

sayilar = (1, 2, 45, 67, 89, 8)
#sayilar = tuple(1, 2, 45, 67, 89, 8)

#print(type(sayilar))
print(sayilar)
print(sayilar[3])
print(sayilar[3])

for i in sayilar:
    print(i)


#burda bir int oluyor tuple olması için yanına virgül koyman gerekiyor
sayilar = (3)
print(type(sayilar))

sayilar = (3,)
print(type(sayilar))

sayilar = 1, 2, 3, 4

print(type(sayilar))
print(sayilar)
print(sayilar[2])

isim, soyisim, yas = ('oguzhan', 'çelikarslan', 23)

#print(isim, soyisim, yas)
#print(isim[0])
print(isim)
print(yas)
print(soyisim)

#tuple değiştirme = Error
#new_tuple = ('hii', 'wow', 'nE')

#tuple olduğu için değiştirme olmuyor hata veriyor
#new_tuple[0] = 'hasan'



#sys ile ne yapabildiklerimize bakalım
import sys

#print(dir(sys))
#print(help(sys.getsizeof))

#tuple listesi ile list listesi farkı
isim_listesi = ['hasan', 'selam', 'naber', True, False, 123.123]
tuple_listesi = ('hasan', 'selam', 'naber', True, False, 123.123)

print("____________________")
#burda list listesi 104 byte iken tuple listesi 88 byte 
#burda az olsada fark büyük dosyalarda çok fazla oluyor bu fark
print("byte:")
print(sys.getsizeof(isim_listesi))
#arasındaki fark birisi 104 byte iken ddiyerkisi 88 byte
print("byte:")
print(sys.getsizeof(tuple_listesi))

#burda dir elemanını kulanıyoruz her iki liste için
# print(dir(tuple_listesi))
# print("_____________________________________________________")
# print(dir(isim_listesi))

#burda len kunlanıyoruz eleman sayısın söylüyor list içindeki
print(len(tuple_listesi))
print(len(isim_listesi))




#sets (kümeler)


alacaklar = set(['elma', 'armut', 'kiraz'])
#print(dir(alacaklar))
#print(help(alacaklar.add)),

alacaklar.add('araba')
alacaklar.add('ev')
alacaklar.add('kitap')
alacaklar.add('kitap') # bir yazı veya sayıyı 1 kere yazdığınız zaman sadece bitabne varmış gibi görüyor

alacaklar.remove('araba')

alacaklar.clear()

#alacaklar.remove('armut') böylebir kelime olmadığı için keyerror: 'armıt diyecektir

alacaklar.discard('armut') # bunda hata vermez yoksa silmez varsa siler 

print(type(alacaklar))
print(alacaklar)




tek_sayılar = set([1,3,5,7,9])
cift_sayılar = set([2,4,6,8])
asal_sayılar = set([2,3,5,7])

print(tek_sayılar.union(cift_sayılar))
print(cift_sayılar.union(tek_sayılar))
print(tek_sayılar.intersection(asal_sayılar))
print(cift_sayılar.intersection(asal_sayılar))

print("__________________________________" * 100)





#foksiyonlar

def toplama(a, b=3):
    """
    verilen a ve parametrsei için toplama işlemi gerçekleitirir
    """
    #print('toplama')
    #return 'ömer'
    return a + b

#x = toplama(2) #5
help(toplama)
x = toplama(2, 5) # 7

#print(toplama)
print(x)



#*args vs **kwargs

def toplama_2 (*deneme, **deneme2):
    
    # print(args) # bir adet tuple verdi
    # print(type(args))
    # print(kwargs) # bir adet sözlük verdi dick verdi
    # print(type(kwargs))


    print(deneme) # bir adet tuple verdi
    print(type(deneme))
    print(deneme2) # bir adet sözlük verdi dick verdi
    print(type(deneme2))



toplama_2 = toplama_2(1 , 2, 3, 4, y=2, x=4)

#toplama_2 = toplama_2(y=2,x=4)

#print(toplama_2)