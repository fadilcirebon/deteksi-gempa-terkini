"""
Aplikasi Deteksi Gempa Terkini
Modularisasi dengan function
Modularisasi dengan package
"""

from gempa_terkini import ektraksi_data, tampilkan_data

if __name__ =='__main__':
    print("Aplikasi Utama")
    result = ektraksi_data()
    tampilkan_data(result)

#done

    