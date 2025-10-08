def is_leap_year(year):
  """Menentukan apakah suatu tahun adalah tahun kabisat."""
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month():
  """Menentukan jumlah hari dalam bulan dengan perulangan while untuk validasi input."""
  bulan_valid = False
  tahun_valid = False
  
  while not bulan_valid:
    try:
      bulan = int(input("Masukkan bulan (1-12): "))
      if 1 <= bulan <= 12:
        bulan_valid = True
      else:
        print("Input bulan tidak valid. Masukkan angka antara 1 sampai 12.")
    except ValueError:
      print("Input bulan tidak valid. Masukkan angka.")
      
  while not tahun_valid:
    try:
      tahun = int(input("Masukkan tahun: "))
      if tahun > 0:
        tahun_valid = True
      else:
        print("Input tahun tidak valid. Masukkan angka yang lebih besar dari 0.")
    except ValueError:
      print("Input tahun tidak valid. Masukkan angka.")
  
  if bulan in (1, 3, 5, 7, 8, 10, 12):
    print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah 31 hari.")
  elif bulan in (4, 6, 9, 11):
    print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah 30 hari.")
  elif bulan == 2:
    if is_leap_year(tahun):
      print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah 29 hari.")
    else:
      print(f"Jumlah hari di bulan {bulan} tahun {tahun} adalah 28 hari.")

get_days_in_month()
