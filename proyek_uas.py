import os
import time
import sys

ideal_anak = [9, 11]
ideal_remaja = [8, 10]
ideal_dewasa = [7, 9]
ideal_lansia = [7,8]



def klasifikasi_durasi(usia, durasi):
  if usia == "anak anak" :
    durasi_minimal = min(ideal_anak)
    durasi_maksimal = max(ideal_anak)
    if durasi_minimal <= durasi <= durasi_maksimal:
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nBagus! Pola tidur sudah sesuai untuk tumbuh kembang.")
    elif durasi < durasi_minimal :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nAnak butuh tidur cukup untuk pertumbuhan. Cobalah tidur lebih awal dan kurangi aktivitas malam.")
    else  :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nTerlalu banyak tidur bisa membuat anak kurang aktif. Coba atur waktu bermain di siang hari.")

  elif usia == "remaja":
    durasi_minimal = min(ideal_remaja)
    durasi_maksimal = max(ideal_remaja)
    if durasi_minimal <= durasi <= durasi_maksimal:
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nPola tidur sudah baik, pertahankan!")
    elif durasi < durasi_minimal :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nKurangi penggunaan gadget sebelum tidur dan buat jadwal tidur teratur.")
    else  :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nCobalah lebih produktif di siang hari agar waktu tidur tidak berlebihan.")

  elif usia == "dewasa" :
    durasi_minimal = min(ideal_dewasa)
    durasi_maksimal = max(ideal_dewasa)
    if durasi_minimal <= durasi <= durasi_maksimal:
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nTidur sudah ideal untuk menjaga energi dan produktivitas.")
    elif durasi < durasi_minimal :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nCoba kelola stres, kurangi kafein, dan buat jam tidur konsisten.")
    else  :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nTerlalu banyak tidur bisa menjadi tanda kelelahan. Cobalah rutinitas olahraga ringan.")

  elif usia == "lansia" :
    durasi_minimal = min(ideal_lansia)
    durasi_maksimal = max(ideal_lansia)
    if durasi_minimal <= durasi <= durasi_maksimal:
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nBagus, pola tidur sesuai dengan kebutuhan lansia.")
    elif durasi < durasi_minimal :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nTidur singkat siang hari boleh, tapi hindari tidur sore terlalu lama.")
    else  :
      return print(f"Durasi tidur \t: {durasi} Jam\nUsia \t\t: {usia}\nTerlalu banyak tidur bisa mempengaruhi mobilitas. Coba perbanyak aktivitas ringan.")

  else:
    print(f"Input usia tidak sesuai")


def menu():
  print("""
  ==============================================
      💤 SISTEM MANAJEMEN KESEHATAN TIDUR 💤
  ==============================================
  Masukan data sesuai format berikut:

  👉 Usia: anak anak | remaja | dewasa | lansia
  👉 Durasi Tidur (jam): contoh 6.5
  ==============================================
  """)

def clear_screen():
    if os.name == 'nt' :
      _ = os.system('cls')
    else:
      _ = os.system('clear')

while True :
  menu()
  try:
    durasi = float(input("Durasi tidur anda (dalam jam): "))
    usia = input("Usia anda : ").lower()
  except:
    clear_screen()
    print("Input tidak sesuai")
    input("Tekan ENTER untuk kembali ke menu utama...")
    clear_screen()
    continue

  clear_screen()
  print("""
  ---------------------------------------------------
  📊 Hasil analisis berdasarkan durasi dan usia anda
  ---------------------------------------------------
  """)
  klasifikasi_durasi(usia, durasi)

  analisa_lagi = input("\nAnalisis lagi (y/n)? ").lower()
  clear_screen()
  if analisa_lagi != "y":
    print("""
    ================================================
    🙏 Terima kasih telah menggunakan program ini!
        Semoga pola tidur Anda semakin sehat 😴✨
    ================================================
    """)
    break


