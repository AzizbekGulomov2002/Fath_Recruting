from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import ListView
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings


from apps.company.models import *


def index(request):
    company = Company.objects.all()
    statistic = Statistic.objects.all()
    contact = Contact.objects.all()
    service = Service.objects.all()
    about = About.objects.all()
    team = Team.objects.all()
    contex = {
        'Company':company,
        'Statistic':statistic,
        'Contact':contact,
        'Service':service,
        'About':about,
        'Team':team,
    }
    return render(request, ['index.html'], contex)



class AboutViews(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'About'



class ContactViews(ListView):
    model = Contact
    template_name = 'base.html'
    context_object_name = 'Contact'


class ServiceViews(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'Service'


class TeamViews(ListView):
    model = Team
    template_name = 'team.html'
    context_object_name = 'Team'


class BlogViews(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'Blog'


def blog_detail(request,id):    
    blogs=Blog.objects.get(id=id)
    blogs.viewed=blogs.viewed+1
    blogs.save()
    print(blogs)
    return render(request,'blog_detail.html',{"blogs":blogs})



def email_send(request):
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['email']
        subject = request.POST['message']
        message = "The person who message : "+ name + '\n' +"Message: " + subject + "Email: "+ mail
        send_mail(name,message,mail,['azizgulomov1529@gmail.com'],
                   fail_silently=False)
        luck = "Message sended"
        return render(request, 'index.html', {'luck':luck})
    return render(request, 'index.html')