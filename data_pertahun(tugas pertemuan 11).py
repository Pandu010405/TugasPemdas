import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 239, 240, 241, 242, 243],
    "kode_provinsi": [32] * 10,
    "nama_provinsi": ["JAWA BARAT"] * 10,
    "kode_kabupaten_kota": [3201, 3202, 3203, 3204, 3205, 3275, 3276, 3277, 3278, 3279],
    "nama_kabupaten_kota": [
        "KABUPATEN BOGOR", "KABUPATEN SUKABUMI", "KABUPATEN CIANJUR", 
        "KABUPATEN BANDUNG", "KABUPATEN GARUT", "KOTA BEKASI", 
        "KOTA DEPOK", "KOTA CIMAHI", "KOTA TASIKMALAYA", "KOTA BANJAR"
    ],
    "jumlah_produksi_sampah": [1511.15, 419.01, 981.41, 1895.94, 464.74, 0, 0, 0, 0, 0],
    "satuan": ["TON PER HARI"] * 10,
    "tahun": [2015, 2015, 2015, 2015, 2015, 2023, 2023, 2023, 2023, 2023]
}

data_pertahun = pd.DataFrame(data)
total_produksi_sampah_per_tahun = {}

for index, row in data_pertahun.iterrows():
    tahun = row["tahun"]
    jumlah_sampah = row["jumlah_produksi_sampah"]
    if jumlah_sampah is not None:  
        if tahun not in total_produksi_sampah_per_tahun:
            total_produksi_sampah_per_tahun[tahun] = 0
        total_produksi_sampah_per_tahun[tahun] += jumlah_sampah
print("Total produksi sampah per tahun di Jawa Barat:")
for tahun, total in total_produksi_sampah_per_tahun.items():
    print(f"Tahun {tahun}: {total} ton/hari")

df_total_per_tahun = pd.DataFrame(list(total_produksi_sampah_per_tahun.items()), columns=["Tahun", "Total Produksi Sampah (ton/hari)"])

df_total_per_tahun.to_csv("data_pertahun.csv", index=False)
df_total_per_tahun.to_excel("data_pertahun.xlsx", index=False)

