class participant:
    qrup = ['Nurlan', 'Ömər', 'Aysel', 'Vüsal', 'Rəşid', 'Xədicə', 'Selcan']
    istirakcilar = set()
    dict = {}
    def __init__(self):
        self.secim()

    def siyahi_goster(self):
        if len(self.istirakcilar)==0:
            print("Istirakci yoxdur")
        else:
            for i in self.istirakcilar:
                print(str(i))
    def istirak_etmeyen(self):
        print("Istirak etmeyenler:")
        for i in self.qrup:
            if i in self.istirakcilar:
                continue
            else:
                print(i)
    def elave_et(self):
            while True:
                elave_ad = input("Elave edeceyiniz istirakcinin adi:")
                if elave_ad == 'done':
                    self.siyahi_goster()
                    self.secim()
                self.istirakcilar.add(elave_ad.lower().capitalize())
    def sil(self):
        if len(self.istirakcilar) == 0:
            print("Istirakci yoxdur")
        else:
            silinen = input('Silmek istediyiniz telebe:')
            if silinen.lower().capitalize() in self.istirakcilar:
                self.istirakcilar.remove(silinen)
                print("'{}' siyahidan silindi! ".format(silinen))
            else:
                print('Istirakci tapilmadi')
            self.siyahi_goster()
    def secim(self):
        while True:
            print("""----------Xidmetler------------
1> Istirakci siyahisi
2> Istirakci elave et
3> Istirakci sil
4> İstirak etmeyenler""")
            print("*Her hansi emeliyyati dayandirmaq ucun \"done\" yazmaginiz kifayetdir")
            secim = input("Seciminiz:")
            if secim == '1':
                self.siyahi_goster()
            elif secim == '2':
                self.elave_et()
            elif secim == '3':
                self.sil()
            elif secim == '4':
                self.istirak_etmeyen()
            elif secim == 'done':
                break
            else:
                print('!!Kecerli reqem daxil edilmeli!!')
participant()
