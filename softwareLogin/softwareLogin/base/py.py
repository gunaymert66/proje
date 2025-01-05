import os

file_path = r'softwareLogin\\media'

if os.path.exists(file_path):
    print("Dosya bulundu!")
else:
    print("Dosya veya klasör eksik. Lütfen yolu kontrol edin.")
