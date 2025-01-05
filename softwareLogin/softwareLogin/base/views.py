from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

import speech_recognition as sr
import pygame 
import pandas as pd
import speech_recognition as sr
from django.http import JsonResponse

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "voice_record.html",{})
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Burada her durumda search-and-play sayfasına yönlendiriyoruz
            return redirect('/voice_record/')  # Buraya sabit olarak yönlendiriyoruz
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def logout(request):
        logout(request)
        return redirect('accounts/login')  
# Create your views here.
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:login")
        else:
            # Hataları konsola yazdır
            print("Form geçersiz:", form.errors)
            print("Gelen veri:", request.POST)
            return render(request, "registration/signup.html", {"form": form})

    # Handle GET requests:
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# Çıkıştan sonra ana sayfaya yönlendirir Eğer GET isteği yapılırsa sayfa yüklenir


 # pygame'i başlat
pygame.mixer.init()

# Dosyanın bulunduğu dizini dinamik olarak al


# Dosyanın var olup olmadığını kontrol et
file_path =  "C:\\Users\\ibrah\\OneDrive\\Desktop\\softwareLogin\\softwareLogin\\SesDosyalari_TamYolu.tsv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path, sep='\t')
else:
    print(f"Hata: '{file_path}' dosyası bulunamadı.")
# Ses tanıma için recognizer oluşturun

recognizer = sr.Recognizer()


# Ses kaydını almak
def get_audio_input_turkish():
    with sr.Microphone() as source:
        print("Konuşmaya başlayın... (Maksimum 10 saniye)")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            print("Ses kaydı tamamlandı.")
        except sr.WaitTimeoutError:
            print("Mikrofondan ses alınamadı. Zaman aşımı.")
            return ""

    # First try Turkish, then try English if Turkish recognition fails
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print(f"Algılanan metin (Türkçe): {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition Türkçe sesi anlayamadı")
    except sr.RequestError as e:
        print(f"Google Speech Recognition servisi erişilemiyor; hata: {e}")
        return ""

    

def get_audio_input_english():
    with sr.Microphone() as source:
        print("Konuşmaya başlayın... (Maksimum 10 saniye)")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            print("Ses kaydı tamamlandı.")
        except sr.WaitTimeoutError:
            print("Mikrofondan ses alınamadı. Zaman aşımı.")
            return ""

    # First try Turkish, then try English if Turkish recognition fails
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"Recognized text (English): {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition English speech could not be understood.")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech Recognition service is unreachable; error: {e}")
        return ""

@csrf_exempt
def search_and_play_turkish(request):
    message = ""
    result_message = ""
    filtered_file_paths = []  # Eşleşen dosyaları saklamak için
    file_path =  "C:\\Users\\ibrah\\OneDrive\\Desktop\\softwareLogin\\softwareLogin\\SesDosyalari_TamYolu.tsv"
    df = pd.read_csv(file_path, sep='\t')
    if request.method == "POST":
        message = "Konuşmaya başlayın... (Maksimum 10 saniye)"
        search_word_turkish = get_audio_input_turkish() 

        if search_word_turkish:
            file_paths = df['File Path'].tolist()  # Tüm dosya yollarını al

            for file_path in file_paths:
                if search_word_turkish in os.path.basename(file_path).lower():  # Dosya adında arama yap
                    filtered_file_paths.append(file_path)  # Eşleşen dosyayı ekle

            if filtered_file_paths:
                result_message = f"'{search_word_turkish}' kelimesiyle eşleşen dosyalar bulundu."
            else:
                result_message = f"'{search_word_turkish}' kelimesiyle eşleşen bir dosya bulunamadı."
        else:
            result_message = "Bir kelime tanımlanamadı."

    return render(request, "search_and_play_turkish.html", {
        "message": message,
        "result_message": result_message,
        "file_paths": filtered_file_paths  # Sadece eşleşen dosyaları gönder
    })
def search_and_play_english(request):
    message = ""
    result_message = ""
    filtered_file_paths = []  # Eşleşen dosyaları saklamak için
    file_path =  "C:\\Users\\ibrah\\OneDrive\\Desktop\\softwareLogin\\softwareLogin\\SesDosyalari_TamYolu.tsv"
    df = pd.read_csv(file_path, sep='\t')
    if request.method == "POST":
        message = "Konuşmaya başlayın... (Maksimum 10 saniye)"
        search_word_english = get_audio_input_english() 

        if search_word_english:
            file_paths = df['File Path'].tolist()  # Tüm dosya yollarını al

            for file_path in file_paths:
                if search_word_english in os.path.basename(file_path).lower():  # Dosya adında arama yap
                    filtered_file_paths.append(file_path)  # Eşleşen dosyayı ekle

            if filtered_file_paths:
                result_message = f"'{search_word_english}' kelimesiyle eşleşen dosyalar bulundu."
            else:
                result_message = f"'{search_word_english}' kelimesiyle eşleşen bir dosya bulunamadı."
        else:
            result_message = "Bir kelime tanımlanamadı."

    return render(request, "search_and_play_english.html", {
        "message": message,
        "result_message": result_message,
        "file_paths": filtered_file_paths  # Sadece eşleşen dosyaları gönder
    })


def play_audio_function(file_path):
    pygame.mixer.music.load(file_path)  # Dosya yolunu al
    pygame.mixer.music.play()  # Müziği çal

@csrf_exempt  # CSRF korumasını geçici olarak devre dışı bırakmak için
def play_audio(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')  # AJAX ile gönderilen dosya yolunu al
        if file_path:
            play_audio_function(file_path)  # Ses dosyasını çal
            return JsonResponse({"message": "Ses başarıyla çaldı!"})
        else:
            return JsonResponse({"message": "Dosya yolu bulunamadı."}, status=400)

    return JsonResponse({"message": "Geçersiz istek."}, status=400)

import sounddevice as sd
from scipy.io.wavfile import write
import os
import time
from django.conf import settings
from django.http import FileResponse
# Parametreleri ayarla
ORNEKLEME_HIZI = 44100  # Hz (CD kalitesi)
SURE = 5               # Kayıt süresi (saniye)
from django.db import models

# Kaydı başlatan fonksiyon
from django.http import JsonResponse
from django.shortcuts import render
import pyaudio
import wave
import speech_recognition as sr
import os
from datetime import datetime
import re
import time

# Ses kaydeden fonksiyon
def record_audio(output_filename="recorded_audio.wav", record_seconds=3, channels=1, rate=44100, chunk=1024):
    """
    Ses kaydeden ve kaydı bir dosyaya kaydeden fonksiyon.
    """
    output_dir = os.path.dirname(output_filename)
    if not os.path.exists(output_dir) and output_dir != "":
        os.makedirs(output_dir)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []
    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def recognize_speech_from_audio(audio_filename="recorded_audio.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_filename) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="tr")
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""



import os
import csv
from datetime import datetime

def audio_files_to_csv_recursive(folder_path, csv_file_name):
    headers = ["File Name", "File Extension", "File Size (KB)", "Creation Date", "File Path"]

    # Open the CSV file for writing
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(headers)

        # Traverse through folders and files
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_name, file_extension = os.path.splitext(file)
                file_size = os.path.getsize(file_path) / 1024  # KB size
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

                # Write file information to CSV
                writer.writerow([file_name, file_extension, round(file_size, 2), creation_time, file_path])

        print(f"Audio files information (including subfolders) has been written to {csv_file_name}")
import csv
import sqlite3

# CSV dosyasını veritabanına aktar
def import_csv_to_db(csv_file_path):
    # Bağlantıyı her işlem için oluştur
    conn = sqlite3.connect('files_database.db')
    cursor = conn.cursor()

    # Mevcut tabloyu sil (varsa)
    cursor.execute('DROP TABLE IF EXISTS files')

    # Tabloyu yeniden oluştur
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT UNIQUE,
        file_extension TEXT,
        file_size REAL,
        creation_date TEXT,
        file_path TEXT
    )
    ''')

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')  # TSV dosyası için delimiter '\t' kullanılıyor
        
        # İlk 6 satırı atlamak
        for _ in range(6):
            next(reader)  # İlk 6 satırı atla
        
        # CSV dosyasındaki her bir satırı veritabanına ekle
        for row in reader:
            # Eğer satırda eksik veri varsa geç
            if len(row) < 5:
                print(f"Geçersiz satır (Eksik veri): {row}")
                continue
            
            try:
                # Dosya adı zaten var mı kontrol et
                cursor.execute('''
                INSERT OR IGNORE INTO files (file_name, file_extension, file_size, creation_date, file_path)
                VALUES (?, ?, ?, ?, ?)
                ''', (row[0], row[1], float(row[2]), row[3], row[4]))
                
            except sqlite3.Error as e:
                print(f"Hata oluştu: {e}")
        
        conn.commit()
        conn.close()

# CSV dosyasını veritabanına aktar
import_csv_to_db('C:\\Users\\ibrah\\OneDrive\\Desktop\\softwareLogin\\softwareLogin\\SesDosyalari_TamYolu.tsv')

def record_and_recognize(request):
    if request.method == 'POST':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_directory = f"C:/Users/ibrah/OneDrive/Desktop/Software/{request.user.username}"  # User's folder
        output_path = os.path.join(output_directory, f"recorded_audio_{timestamp}.wav")
        
        # Check if directory exists, create if not
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Record audio
        record_audio(output_filename=output_path, record_seconds=5)

        # Recognize speech from audio
        text = recognize_speech_from_audio(audio_filename=output_path)

        if text:
            new_output_path = os.path.join(output_directory, f"{request.user.username}.{text}.wav")

            # Rename the recorded file based on speech recognition
            os.rename(output_path, new_output_path)

            # Update CSV file with audio file information
            folder_path = "C:\\Users\\ibrah\\OneDrive\\Desktop\\Software"
            csv_file_name = "C:\\Users\\ibrah\\OneDrive\\Desktop\\softwareLogin\\softwareLogin\\SesDosyalari_TamYolu.tsv"
            audio_files_to_csv_recursive(folder_path, csv_file_name)
            import_csv_to_db(csv_file_name)
            return JsonResponse({'status': 'success', 'text': text})
        else:
            return JsonResponse({'status': 'error', 'text': ''})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def voice_record(request):
    return render(request, 'voice_record.html')