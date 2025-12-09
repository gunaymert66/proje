🎤 Voice Command Collector (Django + AJAX)

Bu proje, web tarayıcısından ses kaydı alıp AJAX ile Django sunucusuna gönderen, alınan kaydı hem dosya olarak klasöre hem de veritabanına kaydeden bir web uygulamasıdır.
Sistem aynı zamanda Türkçe ve İngilizce komut kayıt desteği sunar.

🚀 Özellikler

🎙️ Web tarayıcısı üzerinden ses kaydı

🔄 AJAX ile asenkron kayıt gönderme

💾 Django backend’de:

Ses dosyasını klasöre kaydetme

SQLite veritabanında kayıt oluşturma

🌍 Türkçe / İngilizce komut kayıt bölümleri

🔐 Login ve Register (İngilizce arayüz)

📁 Otomatik klasör oluşturma

🗂️ Admin panelinde kayıtları görüntüleme

🛠️ Kullanılan Teknolojiler
Backend

Django

SQLite

Python 3.x

Frontend

HTML / CSS

JavaScript

AJAX (fetch / XMLHttpRequest)

Web Audio API (MediaRecorder)

📂 Proje Dizini (Örnek)
project_root/
│── manage.py
│── requirements.txt
│── README.md
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── record_tr.html
│   │   └── record_en.html
│   └── static/
│       └── js/
│           └── recorder.js
│
├── media/
│   └── recordings/
│       ├── en/
│       └── tr/

🔧 Kurulum
1. Depoyu klonla
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

2. Sanal ortam oluştur
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

3. Bağımlılıkları yükle
pip install -r requirements.txt

4. Migrasyonları çalıştır
python manage.py migrate

5. Sunucuyu başlat
python manage.py runserver
