#Membuat Data Panen
data_panen={
    'lokasi1':{
        'nama_lokasi':'Kebun A',
        'hasil_panen':{
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama_lokasi':'Kebun B',
        'hasil_panen':{
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama_lokasi':'Kebun C',
        'hasil_panen':{
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi':'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi':'Kebun E',
        'hasil_panen':{
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

#nomor 1
#Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing
print(data_panen)
#nomor 2
#Tampilkan jumlah hasil panen jagung dari lokasi2
print(data_panen['lokasi2']['hasil_panen']['jagung'])
#nomor 3
#Tampilkan nama lokasi dari lokasi3
print(data_panen['lokasi3']['nama_lokasi'])

#nomor 4
#Memasukkan jumlah hasil panen padi dan kedelai dari setiap lokasi kedalam variabel yang berbeda
hasil_panen_padi=[]
hasil_panen_kedelai=[]
for lokasi,data in data_panen.items():
    hasil_panen_padi.append(data['hasil_panen']['padi'])
    hasil_panen_kedelai.append(data['hasil_panen']['kedelai'])

print(f"Hasil panen padi dari masing-masing lokasi adalah {hasil_panen_padi}")
print(f"Hasil panen kedelai dari masing-masing lokasi adalah {hasil_panen_kedelai}")

#nomor 5
#Membuat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi
hasil_padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
hasil_kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

hasil_padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
hasil_kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

hasil_padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
hasil_kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

hasil_padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
hasil_kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

hasil_padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
hasil_kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print(f"Hasil Panen Padi di lokasi 1 yaitu di Kebun A adalah {hasil_padi_lokasi1}")
print(f"Hasil Panen Kedelai di lokasi 1 yaitu di Kebun A adalah {hasil_kedelai_lokasi1}")

print(f"Hasil Panen Padi di lokasi 2 yaitu di Kebun B adalah {hasil_padi_lokasi2}")
print(f"Hasil Panen Kedelai di lokasi 2 yaitu di Kebun B adalah {hasil_kedelai_lokasi2}")

print(f"Hasil Panen Padi di lokasi 3 yaitu di Kebun C adalah {hasil_padi_lokasi3}")
print(f"Hasil Panen Kedelai di lokasi 3 yaitu di Kebun C adalah {hasil_kedelai_lokasi3}")

print(f"Hasil Panen Padi di lokasi 4 yaitu di Kebun D adalah {hasil_padi_lokasi4}")
print(f"Hasil Panen Kedelai di lokasi 4 yaitu di Kebun D adalah {hasil_kedelai_lokasi4}")

print(f"Hasil Panen Padi di lokasi 5 yaitu di Kebun E adalah {hasil_padi_lokasi5}")
print(f"Hasil Panen Kedelai di lokasi 5 yaitu di Kebun E adalah {hasil_kedelai_lokasi5}")

#nomor 6
#membuat percabangan if else
def cek_kondisi_lokasi(lokasi, padi, jagung):
    if padi > 1300 or jagung > 800:
        print(f"berdasarkan data yang ada, maka {lokasi} memerlukan perhatian khusus.")
    else:
        print(f"berdasarkan data yang ada, maka {lokasi} dalam kondisi baik.")

for lokasi,data in data_panen.items():
    padi=data['hasil_panen']['padi']
    jagung=data['hasil_panen']['jagung']
    cek_kondisi_lokasi(data['nama_lokasi'],padi,jagung)