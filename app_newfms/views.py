from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alarma
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
import json
import socket
import datetime
import environ
env = environ.Env()

syslog_use = env('J_SYSLOG_USE')
syslog_ip = env('J_SYSLOG_IP')
syslog_port = env('J_SYSLOG_PORT')

@login_required
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Done!")

@login_required
def all_alm(request):
    p = Alarma.objects.all()
    return render(request, 'alarmas.html', {'alms': p})

def es_admin(user):
    return user.groups.filter(name='nocadmin').exists() or user.is_staff

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("all_alm")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def done(request):
    return render(request, "done.html")

@user_passes_test(es_admin)
def ack(request,id):
    alm=Alarma.objects.get(pk=id)
    alm.USER = request.user.username
    alm.ACK = 1
    alm.save()
    return redirect('all_alm')

@user_passes_test(es_admin)
def delete(request,id):
    alm=Alarma.objects.get(pk=id)
    alm.USER = request.user.username
    alm.SEVERIDAD = "CL"
    alm_dict = model_to_dict(alm)
    alm_json = json.dumps(alm_dict)
    send_syslog_rfc3164(alm_json)
    alm.delete()
    return redirect('all_alm')


def send_syslog_rfc3164(message):
    if syslog_use.upper()=='TRUE':
        syslog_server_ip = syslog_ip
        syslog_server_port = int(syslog_port)
        timestamp = datetime.datetime.now().strftime('%b %d %H:%M:%S')
        syslog_message = f"<133>{timestamp} NEWFMS NEWFMS: {message}"
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(syslog_message.encode('utf-8'), (syslog_server_ip, syslog_server_port))
            