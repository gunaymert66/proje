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
    return render(request, "search_and_play_turkish.html",{})
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Burada her durumda search-and-play sayfasına yönlendiriyoruz
            return redirect('/search-and-play/')  # Buraya sabit olarak yönlendiriyoruz
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
file_path = r'C:\Users\ibrah\OneDrive\Desktop\Software\SesDosyalari_TamYolu.tsv'

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