#!/bin/bash

# Veritabanı migrasyonlarını çalıştır
echo "Running database migrations..."
python manage.py migrate --noinput

# Statik dosyaları topla
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Diğer işlemler (örn: önbellek temizleme veya dosya izinlerini ayarlama)
echo "Clearing cache..."
python manage.py clear_cache  # Örneğin cache temizleme

echo "Release process complete."
