from django.shortcuts import render
from django.http import HttpResponse
from .models import newcases, recovery, deaths, vaccine

# Create your views here.

def home(response):
    return render(response, "covid_db/index.html", {})

def new_cases(response):
    if response.method == "POST":
        name = response.POST.get('name', '')
        patient_id = response.POST.get('patient_id', '')
        age = response.POST.get('age', '')
        gender = response.POST.get('gender', '')
        address = response.POST.get('address', '')
        phone_no = response.POST.get('phone_no', '')
        date = response.POST.get('date', '')
        
        if name and patient_id and age and gender and address and phone_no and date:
            newcase = newcases(name=name, patient_id=patient_id, age=age, gender=gender, address=address, phone_no=phone_no, date=date)
            newcase.save()
        else:
            return HttpResponse("Enter all the response")
    return render(response, "covid_db/new_cases.html", {})

def recovered(response):
    if response.method == "POST":
        name = response.POST.get('name', '')
        id = response.POST.get('patient_id', '')
        age = response.POST.get('age', '')
        gender = response.POST.get('gender', '')
        address = response.POST.get('address', '')
        phone_no = response.POST.get('phone_no', '')
        date = response.POST.get('date', '')
        
        if name and id and age and gender and address and phone_no and date:
            recovered = recovery(name=name, patient_id=newcases.objects.get(patient_id=id), age=age, gender=gender, address=address, phone_no=phone_no, date=date)
            recovered.save()
        else:
            return HttpResponse("Enter all the response")
    return render(response, "covid_db/recovered.html", {})

def death(response):
    if response.method == "POST":
        name = response.POST.get('name', '')
        id = response.POST.get('patient_id', '')
        age = response.POST.get('age', '')
        gender = response.POST.get('gender', '')
        address = response.POST.get('address', '')
        phone_no = response.POST.get('phone_no', '')
        date = response.POST.get('date', '')
        
        if name and id and age and gender and address and phone_no and date:
            death = deaths(name=name, patient_id=newcases.objects.get(patient_id=id), age=age, gender=gender, address=address, phone_no=phone_no, date=date)
            death.save()
        else:
            return HttpResponse("Enter all the response")
    return render(response, "covid_db/deaths.html", {})

def vaccines(response):
    if response.method =="POST":
        id = response.POST.get('patient_id', '')
        vaccine_name = response.POST.get('vaccine_name', '')
        dose = response.POST.get('dose', '')

        if id and vaccine_name and dose:
            vaccines = vaccine(patient_id=newcases.objects.get(patient_id=id), vaccine_name = vaccine_name, dose = dose)
            vaccines.save()
        else:
            return HttpResponse("Enter all the response")
    return render(response, "covid_db/vaccine.html", {})