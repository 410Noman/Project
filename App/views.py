from django.shortcuts import render
from .models import Post
from django.views import generic 
from datetime import datetime
#from App.models import Contact
# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'

def Contactt(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        Contact = Contactt(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        Contact.Save()

    # return HttpResponse("this is contact page")
    return render(request, 'contactus.html')