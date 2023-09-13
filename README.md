# Step by Step
**1. Membuat Project Django**

<p align="justify">Sebelum kita membuat project Django baru, tentunya kita perlu menyiapkan repository lokal dan remote, menginsiasi repo lokal, menghubungkan kedua repository tersebut dengan perintah 'git branch -M main', dan 'git remote add origin <URL_REPO>'. setelah itu selesai, kita bisa mulai membuat project Django yang baru. Pertama kita membuat virtual environment baru dengan 'python3 -m venv env' (di terminal lain bisa saja python saja), kemudian menulis command 'source env/bin/activate' (macOS).
Selanjutnya kita dapat menyiapkan dependencies yakni komponen atau modul yang diperlukan oleh suatu perangkat lunak untuk berfungsi, termasuk library, framework, atau package. Dependencies tersebut adalah django, gunicorn, whitenoise, psycopg2-binary, requests, dan urllib3. Dependencies tersebut bisa kita letakkan di dalam txt file bernama requirements. Kemudian, kita menjalankan pip3 install -r requirements.txt untuk menginstall segala dependencies yang ada. Setelah itu, kita dapat menjalankan 'django-admin startproject <NAMA PROJECT> .' untuk membuat project baru. Supaya kita dapat mem-visit project kita di web kita perlu menulis 'ALLOWED_HOSTS = ["*"]' di settings.py. Akhirnya kita menjalankan './manage.py runserver' untuk melihat apakah project kita berhasil dibuat apa tidak dengan indikator animasi roket. </p>

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**

<p align="justify">Sebelum kita membuat aplikasi baru, kita perlu menambahkan suatu berkas .gitignore yakni sebuah berkas konfigurasi yang digunakan dalam repositori Git untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git. Berkas ini berfungsi karena ada beberapa berkas yang tidak perlu dilacak oleh Git, seperti berkas-berkas yang dihasilkan oleh proses kompilasi, berkas sementara, atau berkas konfigurasi pribadi. Setelah itu, kita lakukan add, commit, push.
Setelah itu selesai, kita menjalankan 'python manage.py startapp main' untuk membuat app baru dengan nama main. Lalu kita perlu ke direktori settings.py di dalam direktori projek dan menambahkan 'main' di dalam list INSTALLED_APPS. Hal ini akan memastikan bahwa ada app bernama main yang direcognize. Selanjutnya, kita membuat direktori baru bernama templates di dalam direktori main. Di dalam templates kita perlu membuat file main.html yang akan mengatur tampilan dasar HTML.</p>
Kemudian, kita akan membuka file models.py dan mendefinisikan model baru untuk app kita. Contoh nya:

```

from django.db import models

class Product(models.Model): 
    product = models.CharField(max_length=255) 
    date_added = models.DateField(auto_now_add=True) 
    amount = models.IntegerField() 
    description = models.TextField()
```

<p align="justify">nama, tanggal_tambah, harga, dan deskripsi adalah atribut atau field pada model. Setiap field memiliki tipe data yang sesuai seperti CharField, DateField, IntegerField, dan TextField.</p>

<p align="justify">Setelah itu selesai, kita dapat melakukan migrasi model yakni suatu cara Django melacak perubahan pada model basis data kita.
Kita dapat menjalankan perintah 'python manage.py makemigrations' untuk membuat file migrasi dan 'python manage.py migrate' untuk menerapkan migrasi.


**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**


Kita mengonfigurasi routing projek yakni dengan menmbuka urls.py di direktori faymart (project) dan menjalankan perintah
```
from django.urls import path, include
```
 dan menambahkan
```
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
Berkas urls.py pada proyek bertanggung jawab untuk mengatur rute URL tingkat proyek dan path URL 'main/' akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main.

**4.  Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.**

Kita dapat menginitialize name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField dengan menulis kode sebagai berikut di models.py pada main.

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

**5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
Kita dapat melakukan suatu integrasi komponen MVT dengan membuat suatu fungsi show_main. Pertama, kita buka file views.py yang terletak di main. Lalu, kita menambahkan perintah sebagai berikut</p>

```
from django.shortcuts import render

def show_main(request):
    context = {
        'product': 'Cookie',
        'amount': '10'
    }

    return render(request, "main.html", context)
```

Perhatikan bahwa fungsi ini menerima parameter request dan mereturn render dengan parameter request, main.html, dan context. Dapat dilihat bahwa salah satu paramete render adalah main.html yang menuju pada nama berkas template yang akan digunakan untuk me-render tampilan. Hal ini mengimplikasi bahwa ada suatu keselarasan yang diperlukan antara nama variabel/atribut yang terdapat pada show_main dan pada main.html, dalaam kasus ini adalah product dan amount. Dengan itu tampilan html yang sesuai supaya tersinkron adalah

```
<h1>Welcome to Faymart!</h1> // judul

<h3>Product: </h3> 
<p>{{ product }}<p> // product: 'cookie'
<h3>Amount: </h3>
<p>{{ amount }}<p> // amount: '10'
```

**6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**

Kita dapat mengonfigrasi routing appdengan membuat file urls.py di main dan mengisinya dengan kode

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Berkas urls.py pada aplikasi main inilah yang bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.

**7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

Kita dapat melakukan deployment melalui Adaptable. Kita perlu memilih repository yang kita pakai, dalam konteks ini saya akan memakai faymart. Lalu, kita perlu memilih spesifikasi app template dan basis data yang sesuai (dalam kasus ini saya memakai Python App Template dan PostgreSQL). Setelah itu, kita dapat mencentang HTTP listener on Port dan mendepoy. Perlu diperhatikan bahwa untuk menjalankan projek django kita di web kita perlu mengetik ```python3 manage.py runserver``` di terminal.


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![image](https://github.com/farrelayman09/faymart/assets/125422538/43de6f41-e96b-4905-8adc-0e4cd3c654f3)
sumber: https://www.interviewbit.com/blog/django-architecture/

- file urls.py pada aplikasi mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi tersebut. Sementara itu, urls.py pada proyek mengarahkan rute URL tingkat proyek dan dapat mengimpor rute URL dari berkas urls.py aplikasi-aplikasi
- views.py berperan sebagai komponen yang menangani logika presentasi dalam konsep MVT. Terlihat bahwa function show_main pada dasarnya menunjukkan text dari atribut yang ingin ditunjukkan kepada user
- models.py berperan sebagai komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Di sinilah kita menginitialize atribut/variabel-variabel yang ingin digunakan.
- berkas html adalal template dari implementasi MVT ini. main.html berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template ini memisahkan kode HTML dari logika aplikasi.

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Dengan menggunakan virtual environment, Anda dapat memastikan bahwa proyek Anda tetap stabil dan konsisten di berbagai lingkungan. Lingkungan yang Dapat Direproduksi: Dengan virtual environment, Anda dapat membuat lingkungan yang dapat direproduksi dengan menentukan versi Python yang sesuai dan package lain yang diperlukan oleh project kita. jika kita menginstal semua package di local environment kita, package tersebut dapat collide saat kita mengerjakan banyak project. Oleh karena itu memiliki virtualenv untuk setiap project dianggap semacam failsafe.

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC berarti model, view, and controller:  controller dan view component memiliki a one-to-many relationship. 
MVP berarti model, view, and presenter: ada one-to-one relationship antara presenter dan view di architecture ini.
MVVM berarti model, view, and view model: MVVM memperbolehkan mapping multiple views dengan single view mode, allowing one too many relationships
