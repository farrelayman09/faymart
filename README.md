
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)


Link Adaptable: https://faymart.adaptable.app/main/

# Tugas 2
Nama: Farrel Ayman Abisatyo<br>
Kelas: PBP F<br>
NPM: 2206828916<br>

## Step by Step
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


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![image](https://github.com/farrelayman09/faymart/assets/125422538/43de6f41-e96b-4905-8adc-0e4cd3c654f3)
sumber: https://www.interviewbit.com/blog/django-architecture/

- file urls.py pada aplikasi mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi tersebut. Sementara itu, urls.py pada proyek mengarahkan rute URL tingkat proyek dan dapat mengimpor rute URL dari berkas urls.py aplikasi-aplikasi
- views.py berperan sebagai komponen yang menangani logika presentasi dalam konsep MVT. Terlihat bahwa function show_main pada dasarnya menunjukkan text dari atribut yang ingin ditunjukkan kepada user
- models.py berperan sebagai komponen yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Di sinilah kita menginitialize atribut/variabel-variabel yang ingin digunakan.
- berkas html adalal template dari implementasi MVT ini. main.html berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template ini memisahkan kode HTML dari logika aplikasi.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Dengan menggunakan virtual environment, Anda dapat memastikan bahwa proyek Anda tetap stabil dan konsisten di berbagai lingkungan. Lingkungan yang Dapat Direproduksi: Dengan virtual environment, Anda dapat membuat lingkungan yang dapat direproduksi dengan menentukan versi Python yang sesuai dan package lain yang diperlukan oleh project kita. jika kita menginstal semua package di local environment kita, package tersebut dapat collide saat kita mengerjakan banyak project. Oleh karena itu memiliki virtualenv untuk setiap project dianggap semacam failsafe.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC berarti model, view, and controller:  controller dan view component memiliki a one-to-many relationship. 
MVP berarti model, view, and presenter: ada one-to-one relationship antara presenter dan view di architecture ini.
MVVM berarti model, view, and view model: MVVM memperbolehkan mapping multiple views dengan single view mode, allowing one too many relationships

# Tugas 3
Nama: Farrel Ayman Abisatyo<br>
Kelas: PBP F<br>
NPM: 2206828916<br>

## Apa perbedaan antara form POST dan form GET dalam Django?
POST digunakan untuk meng-add/mengubah data ke server. Jika Django login form di-returned menggunakan POST method, browser bundles up data form tersebut, meng-encodes untuk transmission, mengirimkannya ke server, dan menerima kembali responsnya.

GET digunakan untuk mengambil/retrieve data dari server. GET, mem-bundle submitted data menjadi string, dan menggunakannya untuk merancang  URL. URL-nya mengandung address where ke mana data perlu dikirim sekaligus data key dan valuenya.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

**XML**<br>
XML (Extensible Markup Language) dirancang untuk membawa data, bukan untuk menampilkan data. XML adalah bahasa markup yang mendefinisikan seperangkat aturan untuk men-encode dokumen dalam format yang dapat dibaca manusia dan mesin. Berikut adalah karakteristiknya:
- XML tidak mensupport array
- lebih sulit dibaca dibandingkan JSON
- menggunakan endtag
- more secure
- mendukung comments
- any encoding

**JSON**<br>
JSON (JavaScript Object Notation) adalah format pertukaran data yang lightweight dan sepenuhnya tidak bergantung pada language. Berikut adalah karakteristiknya:
- JSON mensupport array
- lebih mudah dibaca dibandingkan XML
- tidak menggunakan endtag
- less secure
- tidak mendukung comments
- only UTF-8 encoding

**HTML**<br>
HTML adalah markup language yang lebih digunakan untuk mengatur kerangka tampilan page. Berbeda dengan XML atau JSON yang menyimpan dan men-transport data, HTML berfungsi menampilkan data (display).

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON semakin populer di API code programming dan layanan web karena membantu dalam data interchange dan hasil layanan web yang lebih cepat. JSON berbasis text, lightweight, dan memiliki data format yang easy-to-parse sehingga tak butuh code tambahan untuk parsing.

## STEP-BY-STEP
## Membuat input form untuk menambahkan objek model pada app sebelumnya.

Pertama, sayake forms.py di folder main untuk mengimport ModelForm dari django.forms dan Product dan main.models yang telah dibuat sebelumnya. 
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "amount", "description"]
```
Saya menulis``` model = Product``` untuk menunjukkan model yang digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product. Selain itu, saya juga menambahkan name, price, amount, dan description sebagai field yang akan saya pakai di page.

Lalu, saya ke views.py yang ada di folder main dan menambahkan beberapa import
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
Kemudian, saya membuat fungsi create_product yang berfungsi untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form.
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
baris ``` return HttpResponseRedirect(reverse('main:show_main')) ```digunakan untuk melakukan redirect setelah data form berhasil disimpan.

Kemudian saya menambahkan lines di fungsi show_main sedemikian sehingga akhirnya seperti ini
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Farrel Ayman Abisatyo', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
```
Setelah itu, saya ke urls.py di folder main dan mengimport fungsi-fungsi tersebut supaya dapat dipakai

```
from main.views import show_main, create_product
```

Kemudian, di templates di folder main saya membuat folder html baru dengan nama create_product.html yang berisi kode
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Kode ini berfungsi untuk "menambahkan" produk baru di page. Bisa dilihat bahwa ```{{ form.as_table }}``` digunakan untuk menampilkan fields form yang sudah dibuat pada forms.py sedalam bentuk  table. Sementara itu,``` <input type="submit" value="Add Product"/> ```digunakan sebagai tombol submit untuk mengirimkan request ke view ```create_product(request)```.

Setelah itu, saya menambahkan kode di block content sebagai berikut
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.amount}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```
Saya menambahkan kode di atas untuk menampilkan data produk seperti Name, Price, Amount, Description, dan Date added. Saya juga menambahkan tombol "Add New Product" yang akan redirect ke halaman form.

## Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Berikut adalah 5 fungsi views untuk melihat objek yang terdapat di dalam views.py

- HTML
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Farrel Ayman Abisatyo', # Nama
        'class': 'PBP F', # Kelas PBP
        'products': products,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan. Sementara itu, Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.

- XML
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type dengan value "application/xml" (untuk format XML) 
- JSON
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type dengan value "application/json" (untuk format JSON).

- XML BY ID
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
konsepnya sama seperti sebelumnya hanya saja terdapat parameter tambahan, yakni id.
- JSON BY ID
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
konsepnya sama juga seperti sebelumnya dengan tambahan parameter id.

##  Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Untuk membuat routing URL untuk setiap views yang ada, saya ke urls.py di main dan mengimport fungsi yang telah dibuat sebelumnya 
```
main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```
Kemudian, saya menambahkan list of urlpatterns sedemikian sehingga pada akhirnya, list tersebut akan terlihat seperti ini
```
urlpatterns = [
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
]
```
List of urlpatterns tersebut perlu ditambahkan dengan path yang berisi jenis view yang telah dibuat supaya kita dapat mengakses fungsi views tersebut.

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- HTML
<img width="1070" alt="Screen Shot 2023-09-20 at 11 33 52" src="https://github.com/farrelayman09/faymart/assets/125422538/cd1f359f-af09-4082-ac5f-d64e4ccf8e7d">

- XML
<img width="1440" alt="Screen Shot 2023-09-20 at 05 11 11" src="https://github.com/farrelayman09/faymart/assets/125422538/a09de55e-2936-43cc-842e-6d79c85d90d6"><br>

- XML by ID
<img width="1440" alt="Screen Shot 2023-09-20 at 05 26 00" src="https://github.com/farrelayman09/faymart/assets/125422538/2906978c-56a6-4201-b54a-6c8aeda19014"><br>

- JSON
<img width="1440" alt="Screen Shot 2023-09-20 at 05 25 50" src="https://github.com/farrelayman09/faymart/assets/125422538/5ec096c3-ba93-4a8e-a9d7-8dc76ab225b8"><br>

- JSON by ID
<img width="1440" alt="Screen Shot 2023-09-20 at 05 24 34" src="https://github.com/farrelayman09/faymart/assets/125422538/890348b0-7276-4428-9627-72b9a483f084"><br>



# Tugas 4
Nama: Farrel Ayman Abisatyo<br>
Kelas: PBP F<br>
NPM: 2206828916<br>

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah sebuak class yang dapat digunakan untuk membuat new user yang bisa menggunakan aplikasi web kita.<br>
Kelebihan: cara yang praktis dan efisien untuk membuat form pembuatan user baru<br>
Kekurangan: form ini hanya menyediakan 3 field secara default, yakni username, password1, dan password2 (konfirmasi password)<br>

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Dalam konteks Django, autentikasi adalah proses verifikasi siapa pengguna (login), sedangkan otorisasi adalah proses verifikasi bahwa pengguna tersebut mempunyai akses terhadap sesuatu. Autentikasi penting karena proses ini memverifikasi siapa yang me-login ke aplikasi web kita sehingga hanya user dengan credentials yang tepat dapat masuk. Authorization penting karena proses ini memverifikasi hak akses pengguna terhadap data di web sehingga melindungi informasi dan sistem dari _unauthorized access_

##  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?



