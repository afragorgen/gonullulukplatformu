# Gönüllülük Platformu

Bu proje, gönüllülerin çeşitli etkinlikleri görüntüleyebildiği ve etkinliklere katılabildiği basit bir web platformudur.  
Proje, Flask framework’ü kullanılarak geliştirilmiştir ve eğitim amaçlıdır.

---

## 🎯 Projenin Amacı

- Kullanıcıların sisteme kayıt olup giriş yapabilmesini sağlamak
- Mevcut gönüllülük etkinliklerini listelemek
- Etkinlik detaylarını görüntülemek
- Kullanıcıların etkinliklere gönüllü olarak katılmasını sağlamak
- Temel testler yazarak projenin doğruluğunu kontrol etmek

---

## 🚀 Özellikler

- Kullanıcı kayıt olma
- Kullanıcı giriş / çıkış işlemleri
- Etkinlikleri listeleme
- Etkinlik detaylarını görüntüleme
- Etkinliklere gönüllü olarak katılma
- Giriş yapılmadan katılımın engellenmesi
- Flash mesajlar ile kullanıcıya geri bildirim
- Basit ve sade kullanıcı arayüzü

---

## 🛠️ Kullanılan Teknolojiler

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- HTML / CSS
- Pytest

---

## 📁 Proje Yapısı

Gönüllülük Platformu/
│
├── app.py
├── extensions.py
│
├── models/
│ ├── user.py
│ ├── event.py
│ └── participation.py
│
├── routes/
│ ├── auth.py
│ ├── events.py
│ └── main_routes.py
│
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── events.html
│ ├── event_detail.html
│ ├── login.html
│ └── register.html
│
├── scripts/
│ └── seed_events.py
│
├── tests/
│ └── test_basic.py
│
└── README.md

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
pytest



