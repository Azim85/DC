from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CustomerRequestModel
from django.contrib import messages

obj = CustomerRequestModel

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'DC NAPA', 'flag':'all'}
        return render(request, 'dev_com/napaDc.html', context)

    def post(self, request, *args, **kwargs):
        this = request.POST
        user = request.POST['name']
        created = obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        if created:
            messages.success(request, f'{user} your application is received soon we will contact you thanks!')
        return render(request, 'dev_com/napaDc.html', {'message_done':'ms'})

class BeepView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'BEEP', 'flag':request.path.strip('/')}
        return render(request, 'dev_com/3bep.html', context)

    def post(self, request, *args, **kwargs):
        this = request.POST
        obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        return render(request, 'dev_com/3bep.html')


class RFIDView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'RFID', 'flag':request.path.strip('/')}
        return render(request, 'dev_com/rfid.html', context)

    def post(self, request, *args, **kwargs):
        this = request.POST
        obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        return render(request, 'dev_com/rfid.html')


class EMKView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'EMK', 'flag':request.path.strip('/')}
        return render(request, 'dev_com/emk.html', context)


    def post(self, request, *args, **kwargs):
        this = request.POST
        obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        return render(request, 'dev_com/emk.html')

class DLPView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'DLP', 'flag':request.path.strip('/')}
        return render(request, 'dev_com/dlp.html', context)

    def post(self, request, *args, **kwargs):
        this = request.POST
        obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        return render(request, 'dev_com/dlp.html')

class SmartDocsView(View):
    def get(self, request, *args, **kwargs):
        context = {'title':'Smart_Docs', 'flag':request.path.strip('/')}
        return render(request, 'dev_com/smartDocs.html', context)

    def post(self, request, *args, **kwargs):
        this = request.POST
        obj.objects.create(name=this['name'], last_name=this['last_name'], phone=this['phone'], category=this['category'])
        return render(request, 'dev_com/smartDocs.html')