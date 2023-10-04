import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse




@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP F', # Kelas PBP
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def remove_product(request, product_id):  # to remove item/product
    if request.method == "DELETE":
        item = get_object_or_404(Item, pk=product_id)

        # Ensure the user has the necessary permissions to delete the product
        if item.user == request.user:
            item.delete()
            return JsonResponse({'message': 'Product deleted successfully.'}, status=204)
        else:
            return JsonResponse({'error': 'You do not have permission to delete this product.'}, status=403)
    else:
        return JsonResponse({'error': 'Invalid request method. Use DELETE to remove a product.'}, status=400)

@login_required(login_url='/login')
def increment_amount(request, product_id): # to increment amount
    try:
        item = get_object_or_404(Item, pk=product_id)

        # Ensure the user has the necessary permissions to increment the amount
        if item.user == request.user:
            item.amount += 1
            item.save()
            return JsonResponse({'new_amount': item.amount})
        else:
            return JsonResponse({'error': 'You do not have permission to increment the amount.'}, status=403)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@login_required(login_url='/login')
def decrement_amount(request, product_id):  # to decrement amount
    try:
        item = get_object_or_404(Item, pk=product_id)

        # Ensure the user has the necessary permissions to decrement the amount
        if item.user == request.user:
            item.amount = max(0, item.amount - 1)
            item.save()
            return JsonResponse({'new_amount': item.amount})
        else:
            return JsonResponse({'error': 'You do not have permission to decrement the amount.'}, status=403)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get data berdasarkan ID
    item = Item.objects.get(pk = id)
    # Hapus data
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))