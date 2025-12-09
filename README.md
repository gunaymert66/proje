🎤 Voice Command Database (Django + AJAX)

Bu proje, web tarayıcısı üzerinden alınan ses kayıtlarını AJAX ile Django backend’ine gönderen, kayıtları hem dosya sistemine hem de veritabanına kaydeden bir web uygulamasıdır. Uygulama Türkçe ve İngilizce komut kayıtlarını destekler ve kullanıcı giriş sistemi içerir.

🚀 Özellikler

Tarayıcıdan ses kaydı alma (MediaRecorder API)

AJAX ile asenkron kayıt gönderme

Kaydedilen ses dosyalarını klasörde saklama

Ses komutu bilgilerini SQLite veritabanında tutma

TR / EN kayıt sayfaları

Login / Register kullanıcı sistemi (Django Auth)

Dinamik klasör oluşturma (tarihe veya dile göre)

Admin panelinde kayıtları görüntüleme

🛠️ Teknolojiler
Alan	Teknoloji
Backend	Django, Python
Frontend	HTML, CSS, JavaScript
API	AJAX, Fetch API
Database	SQLite
Audio	MediaRecorder API
📁 Proje Yapısı (Örnek)
project/
│── manage.py
│── README.md
│── requirements.txt
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
└── media/
    └── recordings/
        ├── tr/
        └── en/

🔧 Kurulum Adımları
1. Depoyu klonlayın
git clone https://github.com/<username>/<repo>.git
cd <repo>

2. Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate       # Linux / Mac
venv\Scripts\activate          # Windows

3. Gereksinimleri yükleyin
pip install -r requirements.txt

4. Migrasyonları uygulayın
python manage.py migrate

5. Sunucuyu başlatın
python manage.py runserver
