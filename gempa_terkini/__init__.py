import requests
from bs4 import BeautifulSoup

def ektraksi_data():
    """
    Tanggal: 08 Desember 2021
    Waktu: 05:18:33 WIB
    Magnitudo: 3.4
    Kedalaman : 7 km
    Lokasi: 6.71 LS - 107.35 BT
    Pusat Gempa : Pusat gempa berada di darat 18 km Barat Daya Purwakarta
    Dirasakan: Dirasakan (Skala MMI): III Cipeundeuy, III Cirata, III Maniis, II Purwakarta
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code ==200:
        print (content.text)
        #soup = BeautifulSoup(content)
        #print(soup.prettify())

        hasil = dict()
        hasil['tanggal']= "08 Desember 2021"
        hasil['waktu']= " 05:18:33 WIB"
        hasil['magnitudo']= "3.4"
        hasil['lokasi']= {'ls':6.71,'bt':107.35}
        hasil['pusat gempa']= 'Pusat gempa berada di darat 18 km Barat Daya Purwakarta'
        hasil['dirasakan']= ' Dirasakan (Skala MMI): III Cipeundeuy, III Cirata, III Maniis, II Purwakarta'
        return hasil
    else:
        return None



def tampilkan_data(result):
    print(f'Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal{result['tanggal']}")
    print(f"Waktu{result['waktu']}")
    print(f"Magnitudo{result['magnitudo']}")
    print(f"Lokasi: 'LS'={result['lokasi']['ls']}, 'BT'={result['lokasi']['bt']}")
    print(f"Pusat{result['pusat gempa']}")
    print(f"Dirasakan{result['dirasakan']}")
