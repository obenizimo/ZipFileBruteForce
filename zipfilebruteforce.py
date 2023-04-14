import zipfile
import itertools
import os

# Belirtilen konumdaki ZIP dosyasına erişin
zip_folder = "C:/Users/obeno/OneDrive/Desktop/Yeni klasör (2)"  # ZIP dosyasının bulunduğu konumu buraya yazın
zip_file_name = "example.zip"  # Kırılacak zip dosyasının adını buraya yazın
zip_file_path = os.path.join(zip_folder, zip_file_name)

zip_file = zipfile.ZipFile(zip_file_path)

chars = "1234567890" #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"  # kullanılacak karakterler

for password_length in range(1, 7):  # şifre uzunluğunu burada ayarlayabilirsiniz
    attempts = 0
    total_passwords = len(chars) ** password_length
    for password in itertools.product(chars, repeat=password_length):
        password = "".join(password)
        attempts += 1
       # print(f"Şifre denendi: {password} ({attempts}/{total_passwords})")
        try:
            zip_file.extractall(pwd=password.encode("utf-8"))
            print(f"Şifre kırıldı: {password}")
            break
        except Exception as e:
            pass
