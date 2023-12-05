from django.core.mail import send_mail
from django.shortcuts import render,redirect
from home.utils import *
from home.models import *
from django.contrib import messages
def inserting(name, mail, cono, comment):
    a = Insert(name, mail, cono, comment)
    if a != None:
        return True


def contact(request):
    context = {
        "page": "Om Chaudhari",
    }
    if request.method == "POST":
        data = request.POST
        name = data.get("data[name]")
        mail = data.get("data[mail]")
        cono = data.get("data[Contact Number]")
        comment = data.get("data[comment]")
        if len(cono)<10 or len(cono)>10:
            messages.error(request, "Invalid Contact detail(Must be 10 characters)")
            context.update({"color": "danger"})
            return render(request, "contact.html", context)
        s = inserting(name, mail, cono, comment)
        if s == True:
            messages.success(request, "Data Submitted")
            context.update({"color": "success"})
        else:
            messages.error(request, "Error occured")
            context.update({"color": "danger"})
        subject = "About Connecting"
        message = "I will contact you soon🥹,Follow me on\n\n\nGithub🥰 - https://github.com/omchaudhari1107\n\nLinkein😹 - https://www.linkedin.com/in/om-chaudhari-38960721b"
        sender = "omchaudhari1107@gmail.com"
        recipients = [mail]

        send_mail(subject, message, sender, recipients)
        
    return render(request, "contact.html", context)


def index(request):
    shlok = Random_shlok()
    shlok = shlok.split('split')
    num1 = shlok[len(shlok)-1].split(".")
    context = {"page": "Om Chaudhari", "shlok":shlok,"num":shlok[len(shlok)-1],"num1":num1[len(num1)-1].replace(" ",""),"ch":num1[0].replace(" ","")}
    shlok.pop(len(shlok)-1)
    return render(request, "index.html", context)


def Project(request):
    context = {"page": "Om Chaudhari"}
    return render(request, "project.html", context)


def db(request):
    data_set = Read()
    context = {'data_set' : data_set}
    return render(request, "DataBase.html",context)


