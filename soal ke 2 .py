def hitung_tarif_parkir(jenis_kendaraan, lama_parkir):
    # Tarif dasar
    tarif_awal = 3000
    tarif_motor_per_jam = 1000
    tarif_mobil_per_jam = 1500
    denda_lebih_24_jam = 10000

    #rumus dan percabangan
    if lama_parkir <= 2:
        total_tarif = tarif_awal
    else:
        if jenis_kendaraan.lower() == "motor":
            tambahan = (lama_parkir - 2) * tarif_motor_per_jam + tarif_awal
        elif jenis_kendaraan.lower() == "mobil":
            tambahan = (lama_parkir - 2) * tarif_mobil_per_jam + tarif_awal
        else:
            return "Jenis kendaraan tidak valid"
        
        total_tarif = tarif_awal + tambahan
        if lama_parkir > 24:
            total_tarif += denda_lebih_24_jam
    
    return total_tarif


# Input dari pengguna
jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ").strip()
lama_parkir = float(input("Masukkan lama parkir (jam): "))

# Hitung tarif dan tampilkan hasil
tarif = hitung_tarif_parkir(jenis_kendaraan, lama_parkir)
if isinstance(tarif, float):
    print(f"Total tarif parkir: Rp {tarif}")
else:
    print(tarif)