from parsel import Selector
from openpyxl import load_workbook
import re , requests ,time


while True:
    try:

        saniye = int(input("Kaç Saniyede bir Gösterim Yapılsın ? : "))

        break

    except ValueError:

        print("Tam Sayı Girin !!")

        continue

ac=load_workbook(filename='trendurunler.xlsx')

oku=ac['urunler']

altSira=0

hucreNo=1

while True:

    hucreKontrol = oku['A{}'.format(hucreNo)].value

    if hucreKontrol == None:

        print("Kontrol Bitti")
        print("BuyBox Yüksek Fiyatlı ürün Sayısı :",altSira)

        break

    else :

        hucreIcı=oku['A{}'.format(hucreNo)].value

        urunAdresi=hucreIcı

        baslik = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        toplama = requests.get(urunAdresi, headers=baslik)

        if toplama.status_code == 200:

                    secici = Selector(toplama.text)

                    duzenle = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

                    urun = secici.css('#product-detail-app > div > div.pr-cn > div.pr-cn-in > div.pr-in-w > div:nth-child(1) > div.pr-in-cn > h1').get()

                    satici = secici.css('#product-detail-app > div > div.pr-cn > div.pr-cn-in > div.pr-in-w > div.pr-in-sl-ar.sl-ar-en > div.pr-in-sl-bx > div.sl-nm').get()

                    pfiyat = secici.xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/span[1]').get()

                    sfiyat = secici.xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/span[2]').get()
                    
                    #print(satici) #Alttaki if için satıcı dönüş verisi 1 kez çalıştırılıp Alınması yeterli


                    if satici== "<div title=\"Kadir Corut Deha Pazarlama\" class=\"sl-nm\"><a href=\"/magaza/kadir-corut-deha-pazarlama-m-110677\">Kadir Corut Deha Pazarlama</a></div>":

                        hucreNo += 1

                        continue
                    else:
                        print("Kontrol Edilen Ürün  : ", hucreNo)

                        print("Ürün Adı             : ", duzenle.sub('', urun).strip())
                        try:
                            print("Ürün Satıcısı        : ",duzenle.sub('',satici).strip())
                        except:
                            print("Satışta Değil")
                        try:

                            print("Ürün Piyasa Fiyatı   : ", duzenle.sub('', pfiyat).strip())

                        except:
                            print("Ürün Piyasa Fiyatı   : Ürün Satışa KAPALI!")

                        try :

                            print("Ürün Satış  Fiyatı   : ", duzenle.sub('', sfiyat).strip())

                        except:

                            print("Ürün Satış  Fiyatı   : Ürüne İndirim Uygulanmamış")

                            pass

                        print("Ürün Adresi          :", urunAdresi)

                        print("*" * 25)
                        altSira+=1


        else:

            print('Bağlantı kurulamadı! HTTP Kodu: ', toplama.status_code)

        hucreNo+=1

        time.sleep(saniye)
