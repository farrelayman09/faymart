
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)


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
Cookies adalah sepotong kecil informasi yang disimpan di browser klien. Ini digunakan untuk menyimpan data pengguna dalam file secara permanent (atau untuk waktu tertentu). Cookies mempunyai tanggal dan waktu kadaluwarsa dan dihapus secara otomatis ketika kadaluarsa. Django menyediakan metode bawaan untuk meng-set dan mengambil cookie. Cara Django menggunakan cookies untuk mengelola data sesi pengguna terdiri dari beberapa tahap. Pertama, browser client mengirim request ke server. Kemudian, server mengembalikan session id yang akan disimpan sebagai cookie di sisi client. Cookie ini akan digunakan supaya browser mengingat informasi kita selama kita login (holding state). Lalu, ketika cookies tersebut expire, barulah cookies dikeluarkan dari browser.

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara default cookies memiliki kelemahan, yakni rentannya file cookie diubah/temper oleh pengguna lain karena sifatnya yang text-based file. Selain itu, tidak semua aplikasi web yang mengumpulkan informasi dari cookie itu sah/legitimate. Beberapa di antaranya mungkin berbahaya yang menggunakan cookie untuk tujuan hacking.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, kita mengaktifka virtual environment untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain
python -m venv env
atau 
python3 -m venv env

Kemudian di main/views.py, kita akan membuat fungsi dengan nama register sekaligus mengimport class UserCreationForm. Class ini adalah class bawaan Django yang berfungsi untuk meng-handle pendaftaran user baru aplikasi web kita.
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
```form = UserCreationForm(request.POST)``` digunakan untuk menginitialize UserCreationForm baru dari yang sudah di-import sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

Kemudian di main/templates kita membuat file HTML baru dengan nama register.html. Isinya sebagai berikut:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
File ini berfungsi untuk menjadi kerangka page register akun baru

Lalu di main/urls.py kita mengimpor file register tersebut serta menambahkan pathnya di list urlpatterns.
Setelah itu, di main/views.py, kita membuat fungsi login_user dengan parameter request. Kita juga mengimport authenticate dan login dari Django
Authenticate dan login berfungsi untu kmengautentikasi pengguna yang ingin login.
```
from django.contrib.auth import authenticate, login.
```
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Lalu, di main/templates kita membuat file login.html dengan isi:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

File ini akan menjadi kerangka page login aplikasi web kita. Lalu, di main/urls.py kita dapat mengimpor file login serta menambahkan pathnya di urlpatterns.
Setelah membuat fungsi login, kita dapat membuat fungsi logout untuk keluar dari sesi pemakaian web. Kita juga perlu mengimpor class dari Django.
```
from django.contrib.auth import logout
```
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Kita juga perlu menambahkan tombol logout di main.html. Saya menambahkannya setelah hyperlink Add New Product.
Kemudian, tentunya kita juga mengimport serta menambahkan path logout di urlpatterns di main/urls.py

Setelah itu, kita dapat menambahkan aspek restriksi untuk main page. di main/views.py, kita menambahkan import serta kode sebagai berikut:
```
from django.contrib.auth.decorators import login_required
```
```
...
@login_required(login_url='/login')
def show_main(request):
...
```

```@login_required(login_url='/login')``` di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

Lalu, kita dapat menerapkan cookies untuk menampilkan fitur last login
Pertama, di main/views.py kita mengimport:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Di fungsi login_user, kita mengganti kondisi if dengan statement:
```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
```response.setcookie('last_login', str(datetime.datetime.now()))``` berfungsi untuk membuat _cookie last_login dan menambahkannya ke dalam response

Lalu, di show_main kita menambahkan 'last_login': request.COOKIES['last_login'], di context untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan

Fungsi logout_user juga kita ubah menjadi sedemikian rupa:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

```
Kemudian, kita juga perlu menambahkan ```<h5>Sesi terakhir login: {{ last_login }}</h5>``` di main.html sebagai kerangka tampilan last login.

Terakhir, kita dapat menghubungkan suatu user dengan item. Hal ini dilakukan supaya data di satu akun tidak muncul di akun lain. Pertama, di main/models kita mengimport User
```
from django.contrib.auth.models import User
```

Lalu, di models.py kita menambahkan model baru yakni
```
class Item(models.Model): # Nama class Product saya ubah menjadi Item di tugas 4
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
kode diatas berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship, dimana sebuah produk pasti terasosiasikan dengan seorang user. 
Setelah itu, di main/views.py kita mengubah fungsi create_product menjadi sedemikian rupa
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
```
Parameter commit=False yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database.
Kita juga mengubah fungsi show_main menjadi berikut:
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        ...
    ...
```
Potongan kode diatas berfungsi untuk menampilkan objek Item yang terasosiasikan dengan user yang sedang login. Kode request.user.username berfungsi untuk menampilkan username pengguna yang login pada halaman main.
Dengan adanya model baru, tentunya kita perlu melakukan migrasi. Ketika kita melakukan makemigrations kita memiliki opsi satu untuk menetapkan default value untuk field user. Lalu, kita ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada. Setelah itu selesai, kita dapat melakukan migrate sehingga model berhasil ditambahkan.

# Tugas 5

Nama: Farrel Ayman Abisatyo<br>
Kelas: PBP F<br>
NPM: 2206828916<br>

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

Terdapat beberapa element selector yang dapat digunakan dari CSS
- Paragraph
    ```
    /* Style all <p> elements */
    p {
      color: blue;
    }
    ```
Selector ini untuk men-select dan mengs-style paragraph tertentu. Dalam kasus ini paragraph akan memiliki warna biru

- Headings:
  ```
  h1 {
  color: #fca205;
  font-family: "Monospace";
  font-style: italic;
  }
  ```
  Selector headings berfungsi menselect dan mengs-style headers yang dispecify. 
- Anchor
  ```
  /* Style all <a> elements */
    a {
      text-decoration: none;
      color: #0066cc;
    }
  ```
  Selector a berfungsi menselect dan mengs-style anchor element yang dispecify. anchor element ini biasanya berupa hyperlink

- Lists
  ```
      /* Style all <ul> and <ol> elements */
    ul, ol {
      list-style-type: square;
    }
  ```
  Selector list berfungsi menselect dan mengs-style list element yang dispecify, seperti ```<ul>``` (unordered lists) , ```<ol> ```(ordered lists), dan juga list items ```<li>```. 
- Tables
  ```
      /* Style all <table> elements */
    table {
      border-collapse: collapse;
      width: 100%;
    }
  ```
  Selector list berfungsi menselect dan mengs-style table element yang dispecify.

## Jelaskan HTML5 Tag yang kamu ketahui.

- ```<head> </head>```
  Berisi meta-information tentang HTML document tersebut,seperti character encoding, title, links ke stylesheets, dan scripts.
- ```<title> </title>```
  Meng-set title dari HTML document tersebut, yang nantinya akan didisplay di title bar browser.
- ```<table></table>```
  Mendefinisika dan meng-set table di dokumen html tersebut
- ```<th></th>```
  Mendefinisikan table header di table
- ```<td></td>```
  Mendefinisikan table data yang akan dimasukkan ke table

## Jelaskan perbedaan antara margin dan padding.

- Margin adalah ruang di luar elemen dan mempengaruhi jarak antara elemen tersebut dengan elemen lain.<br>
    ```
    div {
      margin: 15px;
    }
    ```
    Kode di atas akan meng-set margin yang memberi jarak antar elemen di luar sebesar 15 px.
- Padding adalah ruang di dalam elemen dan mempengaruhi jarak antara batas elemen dengan konten di dalamnya.<br>
    ```
    div {
      padding: 15px;
    }
    ```
    Kode di atas akan meng-set padding yang memberi jarak antar elemen di dalam sebesar 15 px.
## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Bootstrap:
- Efficient/hemat waktu
- kustomisasi yang lebih terbatas karena bergantung pada gaya dan desain bawaan.
- Lebih besar dalam ukuran file karena memiliki banyak fitur dan komponen<br>

Tailwind:
- Limited pre-built components. 
- Memungkinkan kustomisasi yang lebih besar
- Lebih ringan dalam ukuran file karena hanya menggunakan kelas-kelas yang diperlukan

Jadi, bisa disimpulkan bahwa misal kita ingin meng-customize web app kita dengan lebih leluasa, lebih baik menggunakan Tailwind. Sementara itu, jika kita ingin mendesain web app dengan cepat dan efisien serta menggunakan banyak komponen bawaan, sebaiknya menggunakan Bootstrap.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, saya mengaktifkan virtual environment sebelum mengerjakan tugas. 
Kemudian, saya ke main/templates/main.html dan menambahkan kode sebagai berikut.
```
{% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"     crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>

```
Kode ini berfungsi untuk menambahkan bootstrap CSS dan juga JS

Setelah itu, saya menambahkan navbar dengan menulis kode di bagian atas script. Kode tersebut mengacu pada dokumentasi mengenai NavBar.
Berikut adalah kodenya:
```
{% extends 'base.html' %}

{% block content %}
<style>
    body {
        background-color: #0DD8E9; /* Change this to the desired blue color */
        color: black; /* Set the text color to contrast with the background */
    }
</style>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">You are logged in as {{name}}</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Dropdown
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a href="{% url 'main:logout' %}"><button type="button" class="btn">Logout</button></a>
                    <a class="nav-link disabled" aria-disabled="true"></a>
                </li>
            </ul>
            <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
        </div>
    </div>
</nav>
```
Dapat dilihat bahwa saya menghapus tombol logout di bawah dan menambahkannya di NavBar dengan kode 
```
<li class="nav-item">
    <a href="{% url 'main:logout' %}"><button type="button" class="btn">Logout</button></a>
    <a class="nav-link disabled" aria-disabled="true"></a>
</li>
```
Untuk menambahkan warna background biru, saya menulis kode ini di atas kode navbar
```
<style>
    body {
        background-color: #0DD8E9; /*  light blue  */
        color: black; /* Set text color to contrast bg */
    }
</style>
```
Saya juga mengerjakan bonus dengan menambahkan kode for loop untuk mewarnai item terakhir di list
```
{% for item in items %}
    <tr {% if forloop.last %}style="background-color: #9CF5FF;"{% endif %}>
        <td>{{item.name}}</td>
        <td>{{item.price}}</td>
        <td id="amount_{{ item.id }}">{{item.amount}}</td>
        <td>{{item.description}}</td>
        <td>{{item.date_added}}</td>
...
```





