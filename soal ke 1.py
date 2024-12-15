def hitung_biaya_pengiriman(panjang, lebar, tinggi, berat):
    # Tarif dasar
    biaya_minimal = 8000
    tarif_per_kg_kecil = 5000
    tarif_per_kg_besar = 7000
    tambahan_dimensi_besar = 50000
    volume_batas = 50 * 50 * 50  # Volume maksimum untuk kategori kecil (cm³)
    
    # Hitung volume paket
    volume = panjang * lebar * tinggi
    
    # Jika berat kurang dari 1 kg
    if berat < 1:
        return biaya_minimal
    
    # Jika volume paket kecil
    if volume <= volume_batas:
        return berat * tarif_per_kg_kecil
    
    # Jika volume paket besar
    return berat * tarif_per_kg_besar + tambahan_dimensi_besar


# Input dari pengguna
print("Perhitungan Biaya Ekspedisi - Kota/Kabupaten Pasuruan")
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))

# Hitung biaya
biaya = hitung_biaya_pengiriman(panjang, lebar, tinggi, berat)

# Output hasil
print(f"Total biaya pengiriman: Rp {biaya:,.0f}")