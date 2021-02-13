from django.http import HttpResponse
from django.shortcuts import render, redirect
#
# Create your views here.
import amsmain
from amsmain.models import Register, InsertImage


def show_singlePorto(request):
    return render(request, "indexMain.html")


def show_index(request):
    return render(request, "index.html")


def show_about(request):
    return render(request, "about.html")


def show_portfolio(request):
    images = InsertImage.objects.all().order_by('-id')
    return render(request, "portfolio.html", {'images': images})


def show_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        event = request.POST['event']
        date = request.POST['date']
        description = request.POST['description']

        reg = Register(name=name, phone=phone, email=email, event=event, date=date, description=description)
        reg.save()
        print('saved')
        return redirect("../contact/dashboard/")
    return render(request, 'contact.html')


def show_dash(request):
    bookings = Register.objects.all().order_by('-id')
    return render(request, 'dashboard.html', {'bookings': bookings})


def delete(request, did):
    var = Register.objects.get(id=did)
    var.delete()
    return redirect('../')

# def update(request, bid):
#     b = Register.objects.get(id=bid)
#     if request.method == 'POST':
#         b.name = request.POST['name']
#         b.phone = request.POST['number']
#         b.email = request.POST['email']
#         b.event = request.POST['event']
#         b.date = request.POST['date']
#         b.description = request.POST['description']
#         b.save()
#         # return HttpResponse('<script>alert("Booking Updated")</script>')
#         return redirect('../contact/dashboard/')
#
#     return render(request, 'dashboard.html', {'bookings': b})
