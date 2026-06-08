def analisis_teks(teks):
    jumlah_karakter = len(teks)
    jumlah_kata = len(teks.split())
    return jumlah_karakter, jumlah_kata

teks_uji = "Untuk kode R, format tabelnya sama. Contoh baris kode R seperti teks <- readline. hati_hati hai"
karakter, kata = analisis_teks(teks_uji)
print(f"Jumlah Karakter: {karakter}")
print(f"Jumlah Kata: {kata}")
