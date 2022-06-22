from datetime import datetime

kullanicilar = {                #önceden tanımladığımız kullanıcı bilgileri
    'ahmet': 'İstinye123',
    'meryem': '4444',
    'osman': '155',
    'eren': '111'
}

sepet = {}

Envanter = {                          #envanterimizdeki mallar
    'kuşkonmaz': [6,3],               #soldaki değerler stok miktarını sağdaki değerler ise birim fiyatını göstermektedir.
    'brokoli': [20,7],
    'havuç': [15,5],
    'elmalar': [25,15],
    'muz': [19, 18],
    'meyve': [23,5],
    'yumurta': [44,4],
    'karışık meyve suyu': [1,19],
    'balık çubuk-ları': [27,10],
    'dondurma': [0,4],
    'elma suyu': [33,8],
    'portakal suyu': [32,4],
    'üzüm suyu': [21,16]
}


cikisYapilmadi = True
aktifKullanici = None

while cikisYapilmadi:
    while not aktifKullanici:           #kullanıcıyı karşılama ekranı
        print('**** İstinye Online Market’e Hoşgeldiniz ****')
        print('Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:')
        kullaniciAdi = input('Kullanıcı adı: ')  #kullanıcı adı isteme
        sifre = input('Şifre: ')            #şifre isteme

        if kullaniciAdi not in kullanicilar or kullanicilar[kullaniciAdi] != sifre:  #kullanıcı adı ve şifreyi kontrol ediyoruz yalnış ise giriş yapmıyor
            print('Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!')
        else:     
            aktifKullanici = kullaniciAdi    #kullanıcı adı ve şifre eşleşiyor giriş başrılı

    print('Hoşgeldiniz ' + aktifKullanici + '! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.') 

    oturumAcik = True
    sepettenSecildi = False

    while oturumAcik:          #oturum açıldığı zaman bu seçenekleri sunacak
        print('Lütfen aşağıdaki hizmetlerden birini seçin:')
        print('1. Ürün ara')
        print('2. Sepete git')
        print('3. Satın al')
        print('4. Oturumu kapat')
        print('5. Çıkış yap')

        if sepettenSecildi:  #3 numara sepete gitme kısmı
            secim = '3'
        else:
            secim = input('Seçiminiz: ')

        if secim == '1':
            islemDevam = True
            ilkArama = True

            while islemDevam:
                arama = None
                eslesenUrunler = []

                while len(eslesenUrunler) == 0:   #ürüm arama kısmı
                    if ilkArama:
                        ilkArama = False
                        arama = input('Ne arıyorsunuz? ')
                    else:
                        arama = input('Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin): ')

                        if arama == '0':
                            islemDevam = False

                    if not islemDevam:
                        break

                    for urun in Envanter:
                        if arama.lower() in urun.lower() and Envanter[urun][0] > 0:
                            eslesenUrunler.append(urun)

                if not islemDevam:
                    break

                i = 1

                for urun in eslesenUrunler:     #eşleşen ürünler
                    print(str(i) + '. ' + urun + " " + str(Envanter[urun][1]) + "$")
                    i += 1

                secim1 = ' '

                while secim1 != '0':         #sepete kaç ürün ekleme fonksiyosu 
                    secim1 = input('Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): ')

                    if secim1 == '0':
                        islemDevam = False
                    elif secim1.isdigit() and int(secim1) < i: 
                        secilenUrun = eslesenUrunler[int(secim1) - 1]
                        tutar = input(secilenUrun + " ekleniyor. Tutari girin: ")
                        tutar = int(tutar)

                        while tutar > Envanter[secilenUrun][0]:    #eğer girdiğimiz tutar envanterden fazlaysa kabul etmiyor
                            print('Üzgünüm! Miktar sınırı aşıyor. Lütfen daha küçük bir miktarla tekrar deneyin')
                            tutar = int(input('Miktar (Ana menü için 0 girin): ')) #tekrar miktarı girmesini istiyoruz

                            if tutar == 0:
                                break

                        if tutar != 0:      # girilen tutar sıfırdan farklıysa kabul eder
                            if aktifKullanici not in sepet:
                                sepet[aktifKullanici] = {}

                            if secilenUrun not in sepet[aktifKullanici]:
                                sepet[aktifKullanici][secilenUrun] = int(tutar)
                            else:
                                sepet[aktifKullanici][secilenUrun] += int(tutar)

                            print('Sepetinize ' + secilenUrun + ' eklendi.')
                            print('Ana menüye geri dönülüyor...')
                            
                        islemDevam = False
                        secim1 = '0'
                    else:
                        print('Geçersiz bir ürün seçtiniz.')

            
        elif secim == '2':       #sepete gitme
            islemDevam = True
            sepetIslemiYapildi = False
            
            while islemDevam:
                if sepetIslemiYapildi:
                    print('Sepetiniz artık şunları içeriyor')
                    sepetIslemiYapildi = False
                else:
                    print('Sepetiniz şunları içerir:')

                urunler = []
                i = 1

                if aktifKullanici not in sepet:
                    sepet[aktifKullanici] = {}

                kullaniciSepeti = sepet[aktifKullanici]
                toplam = 0

                for urun in kullaniciSepeti:           #sepetteki öğeleri gösterme
                    urunler.append(urun)
                    fiyat = Envanter[urun][1]
                    miktar = kullaniciSepeti[urun]
                    toplam += fiyat * miktar
                    print(str(i) + '. ' + urun + ' fiyatı = ' + str(fiyat) + ' miktar = ' + str(miktar) + ' toplam = ' + str(fiyat * miktar))
                    i += 1

                print('Toplam: ' + str(toplam) + '$')

                secim2 = ' '
                while secim2 != '4':
                    print('Bir seçeneği seçiniz:')
                    print('1. Tutarı güncelleyin')
                    print('2. Bir öğeyi kaldırın')
                    print('3. Satın al')
                    print('4. Ana menüye dön')

                    secim2 = input('Seçiminiz: ')

                    if secim2 == '1' or secim2 == '2':
                        secim21 = ' '

                        while secim21 != '0':
                            if secim2 == '1':      #miktarı değiştirilecek öğeyi seçme
                                secim21 = input('Lütfen miktarını değiştireceğiniz öğeyi seçin: ')
                            else:
                                secim21 = input('Lütfen sepetten kaldırılacak öğeyi seçin: ')

                            if secim21 == '0':
                                print('Sepet menüsüne dönülüyor.')
                            elif secim21.isdigit() and int(secim21) < i:
                                if secim2 == '1':  
                                    secilenUrun = urunler[int(secim21) - 1] 
                                    miktar = int(input('Lütfen yeni miktarı yazın: ')) #yeni miktarı istiyoruz
                                    
                                    while miktar > Envanter[secilenUrun][0]: #kullanıcının girdiği miktar envanterdekinden büyükmü kontrol
                                        print('Üzgünüm! Miktar sınırı aşıyor. Lütfen daha küçük bir miktarla tekrar deneyin')
                                        miktar = int(input('Miktar (Sepet menüsü için 0 girin): '))

                                        if miktar == '0':
                                            break

                                    if miktar != 0:
                                        sepet[aktifKullanici][secilenUrun] = miktar
                                        sepetIslemiYapildi = True
                                        break
                                else:
                                    secilenUrun = urunler[int(secim21) - 1]
                                    print(secilenUrun + ' sepetten kaldırılıyor.')
                                    sepetIslemiYapildi = True
                                    del sepet[aktifKullanici][secilenUrun]
                                    break
                            else:
                                print('Geçersiz bir ürün seçtiniz. (Sepet menüsü için 0 girin)')

                        

                    elif secim2 == '3':  #satın alma kısmı
                        sepettenSecildi = True
                        secim = '3'
                        print('Satın alınacak')
                        islemDevam = False
                        break
                    elif secim2 == '4':   #ana menüye dönme
                        islemDevam = False
                        break
                    else:     #yanlış bir numara girerse uyarıyor
                        print('Geçersiz bir seçim yaptınız.')

                    if sepetIslemiYapildi:
                        print('Sepet alt menüsüne gidiliyor.')
                        break

        elif secim == '3':   #satın alma fonksiyonu 
            sepettenSecildi = False
            kullaniciSepeti = sepet[aktifKullanici]
            stokYeterli = True
            
            for urun in kullaniciSepeti:
                if kullaniciSepeti[urun] > Envanter[urun][0]:
                    print('Yeterli miktarda ' + urun + ' bulunmamaktadır. Satın alma başarısız!')
                    stokYeterli = False
                    break

            if not stokYeterli:
                continue                
                                                #satın alma seçildiğinde makbuz kısmı devreye giriyor
            print('Makbuzunuz işleniyor...')
            print('******* İstinye Online Market ********')
            print('*************************************')
            print('0850 283 6000')
            print('istinye.edu.tr')
            print('————————————')

            toplam = 0 #toplam ilk başta 0 

            for urun in kullaniciSepeti: 
                fiyat = Envanter[urun][1]
                miktar = kullaniciSepeti[urun]
                toplam += fiyat * miktar #ürünün fiyatını ve miktarını çarpım toplam fiyat bulma
                print(urun + ' ' + str(fiyat) + '$ miktar = ' + str(miktar) + ' toplam = ' + str(fiyat * miktar))
                Envanter[urun][0] -= miktar

            sepet[aktifKullanici] = {}

            print('————————————')
            print('Toplam ' + str(toplam) + '$')
            print('————————————')
            print(datetime.now().strftime('%Y/%m/%d %H:%M'))
            print('Online Market’imizi kullandığınız için teşekkür ederiz!')

        elif secim == '4':         # kullanıcı oturum kapatma fonksiyonu
            oturumAcik = False
            aktifKullanici = None
            print('Oturum kapatılıyor.')
        elif secim == '5':         #programı sonlandırma fonksiyonu
            oturumAcik = False
            cikisYapilmadi = False
            print('Program sonlandırılıyor.')
        else:                           #yanış rakam girilise tekrar deneneme
            print('Geçersiz bir hizmet seçtiniz. Lütfen geçerli bir hizmet seçin.') 