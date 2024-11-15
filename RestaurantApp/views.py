from django.shortcuts import render,redirect
from RestaurantApp.models import BookTable,contact


# Create your views here.
def index(request):
    return render(request,'index.html')
def starter(request):
    return render(request,'starter-page.html')
def About(request):
    return render(request,'About.html')
def Menu(request):
    return render(request,'Menu.html')
def Special(request):
    return render(request,'Special.html')
def Events(request):
    return render(request,'Events.html')
def chef(request):
    return render(request,'chef.html')
def contact(request):
    if request.method == "POST":
        Mycontact = contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        Mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def booking(request):
    if request.method == "POST":
        Mybooking = BookTable(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            people=request.POST['people'],
            message=request.POST['message'],
        )
        Mybooking.save()
        return redirect('/booking')
    else:
        return render(request, 'Book.html')