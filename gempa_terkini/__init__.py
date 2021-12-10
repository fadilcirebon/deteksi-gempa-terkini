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
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(',')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class', 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i=0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None

        for res in result:
             if i == 1:
                 magnitudo= res.text
             elif i == 2:
                 kedalaman= res.text
             elif i == 3:
                 koordinat = res.text.split(' - ')
                 ls = koordinat[0]
                 bt = koordinat[1]
             elif i == 4:
                 lokasi= res.text
             elif i == 5:
                 tsunami = res.text

             i = i + 1

        hasil = dict()
        hasil['tanggal']=  tanggal
        hasil['waktu']= waktu
        hasil['magnitudo']= magnitudo
        hasil['kedalaman']= kedalaman
        hasil['koordinat']= {'ls':ls,'bt':bt}
        hasil['lokasi']= lokasi
        hasil['tsunami']= tsunami
        return hasil
    else:
        return None



def tampilkan_data(result):
    print(f'Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu{result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: 'LS'= {result['koordinat']['ls']}, 'BT'={result['koordinat']['bt']}")
    print(f"Lokasi :  {result['lokasi']}")
    print(f"Apakah Berpotensi Tsunami :  {result['tsunami']}")
