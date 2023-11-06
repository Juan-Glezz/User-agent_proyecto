from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse

def indexed(req):
    return render(req,"proyecto/index.html")


def info_agent(req):
    user_agent = get_user_agent(req)
    return render(req,"proyecto/infoUser.html" , {"info":user_agent})


def get_agent(req):
    user_agent = get_user_agent(req)
    IpDelCliente = req.META.get('REMOTE_ADDR')
    NombreHost = req.META.get('HTTP_HOST')
    if user_agent.is_pc:
        info_txt = f'Su pc tiene el host: {NombreHost} y la ip: {IpDelCliente}'
        if user_agent.is_touch_capable:
            info_txt += "Su dispositivo es tactil"
        else:
            
            info_txt += "Su dispositivo no es tactil"

    if user_agent.is_mobile:
        info_txt = "Su dispositivo es un telefono movil"
        if user_agent.is_touch_capable:
            info_txt += " Su dispositivo es tactil"
        else:
            info_txt += " El dispositivo no es tactil"
        
    if user_agent.is_tablet:
        info_txt = f'Su dispositivo es una Tablet con el host: {NombreHost} y la ip: {IpDelCliente}'
        if user_agent.is_touch_capable:
            info_txt += " Su dispositivo es tactil"
        else:
            info_txt += " Su dispositivo no es tactil"
       
        
    if user_agent.is_bot:
        info_txt = f'Es un Bot con el host: {NombreHost} y la ip: {IpDelCliente}'
        if user_agent.is_touch_capable:
            info_txt += " Su dispositivo es tactil"
        else:
            info_txt += " Su dispositivo no es tactil"

    return render(req, "proyecto/informacion.html" , {"info_txt": info_txt})
# Create your views here.
