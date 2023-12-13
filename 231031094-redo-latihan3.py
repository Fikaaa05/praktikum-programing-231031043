Nama_karyawan =  input("Masukkan Nama: ")
Pendapatan = int(input("Masukkan Pendapatan: "))

print(f"""\nNama: {Nama_karyawan}
pendapatan: {Pendapatan}""")

if Pendapatan >= 1000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")