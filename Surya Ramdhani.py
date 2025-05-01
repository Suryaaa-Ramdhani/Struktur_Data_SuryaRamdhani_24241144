# Nama: Surya Ramdhani
# NIM : 24241144

# NIM sebagai identitas
nim = "24241144"

# Input bilangan dari pengguna
bilangan = input("Masukkan bilangan: ")

# Fungsi untuk mengecek syarat bilangan
def cek_bilangan(bil):
    return bil[:2] == "24" and bil[-2:] == "44"

# Output informasi
print(f"NIM: {nim}")
print(f"Bilangan yang dimasukkan: {bilangan}")

# Pemeriksaan dan hasil
if cek_bilangan(bilangan):
    print(f"Hasil: {bilangan} memenuhi syarat (2 digit awal = 24, 2 digit akhir = 44)")
else:
    print(f"Hasil: {bilangan} TIDAK memenuhi syarat")