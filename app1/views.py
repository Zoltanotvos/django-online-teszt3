from django.shortcuts import render, redirect
from . models import Adatbázismodell
# Create your views here.
def főoldal(request):
    return render(request,"főoldal.html")
def adatbekérő(request):
    if request.method == "GET":
        return render(request, "adatbekérő.html")
    elif request.method == "POST":
        szöveg1 = request.POST.get("szöveg")
        szám1 = request.POST.get("szám")
        boool1 = request.POST.get("boool")
        if boool1 == "on":
            boool1 = True
        else:
            boool1 = False
        adatbázis_elem = Adatbázismodell(szöveg = szöveg1, szám = szám1, boool = boool1)
        adatbázis_elem.save()
        return redirect("főoldal")