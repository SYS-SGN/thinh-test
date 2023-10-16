from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import inforLogin
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def login(request):
    usg_id = request.GET.get('UI', '')
    usg_network_ip = request.GET.get('UIP', '')
    subscriber_mac = request.GET.get('MA', '')
    port_mapping = request.GET.get('RN', '')
    origin_server_url = request.GET.get('OS', '')

    context = {
        'usg_id': usg_id,
        'usg_network_ip': usg_network_ip,
        'subscriber_mac': subscriber_mac,
        'port_mapping': port_mapping,
        'origin_server_url': origin_server_url,
    }
    return render(request,"login.html",context)
    #return HttpResponse(f'usg_id : {usg_id}, usg_network_ip: {usg_network_ip},subscriber_mac : {subscriber_mac}, port_mapping: {port_mapping}, origin_server_url: {origin_server_url}')


def check_data(request):
    infor=inforLogin.objects.all().values() 
    return HttpResponse(infor)

def login_submit(request):
    if request.method == "POST":
        infor=[]
        infor.append(request.POST.get('usg_id'))
        infor.append(request.POST.get('usg_network_ip'))
        infor.append(request.POST.get('subscriber_mac'))
        infor.append(request.POST.get('port_mapping'))
        infor.append(request.POST.get('origin_server_url'))
        if any(value == '' for value in infor):
            return render(request,"login.html")
        else: 
            logger = logging.getLogger(__name__)
            logger.info(infor)
            return redirect("https://www.google.com")


def login_account_submit(request):
    if request.method == "POST":
        inforuser=[]
        inforuser.append(request.POST.get('username'))
        inforuser.append(request.POST.get('passwork'))
        print(inforuser)
        if any(value == '' for value in inforuser):
            return render(request,"login.html")
        else: 
            #test account mẫu
            if inforuser[0]=="abcde" and inforuser[1]=="12345":
                logger = logging.getLogger(__name__)
                logger.info(inforuser)
                return redirect("https://www.google.com")
            else:
                logger = logging.getLogger(__name__)
                logger.warning("Sai tai khoan/mat khau")
                return render(request,"login.html")