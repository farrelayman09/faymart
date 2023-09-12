from django.shortcuts import render

def show_main(request):
    context = {
        'product': 'Cookie',
        'amount': '10'
    }

    return render(request, "main.html", context)