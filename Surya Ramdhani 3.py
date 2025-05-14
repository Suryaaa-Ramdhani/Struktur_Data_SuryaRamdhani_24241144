# Menginput nilai integer
nilai = int(input("Masukkan nilai: "))

# Menghitung nilai
if nilai >= 85:
    grade = "A"
elif nilai >= 80:
    grade = "-A"
elif nilai >= 75:
    grade = "B+"
elif nilai >= 70:
    grade = "B"
elif nilai >= 65:
    grade = "B-"
elif nilai >= 60:
    grede = "C+"
elif nilai >= 55:
    grede = "C"
elif nilai >= 50:
    grade = "-C"
elif nilai >= 40:
    grade = "D"
elif nilai <= 40:
    grade = "E"
# Menampilkan hasil
print(f"Nilai Anda: {nilai}")
print(f"Grade: {grade}")