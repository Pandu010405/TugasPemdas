data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1
print("Seluruh Data Panen:")
for lokasi, data in data_panen.items():
    print(f"{data['nama_lokasi']}: {data['hasil_panen']}")

# 2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")

# 3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi3: {nama_lokasi3}")

# 4
padi_panen = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
kedelai_panen = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("\nJumlah hasil panen padi tiap lokasi:", padi_panen)
print("Jumlah hasil panen kedelai tiap lokasi:", kedelai_panen)

# 5
print("\nStatus lokasi berdasarkan hasil panen:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']

# 6
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
