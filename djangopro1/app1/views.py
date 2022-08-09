from django.shortcuts import render,redirect
from app1.models import Contact
from app1.forms import ContactForm
# Create your views here.
def home_view(request):
	return render(request,'app1/index.html')

def about_view(request):
	return render(request,'app1/about.html')

def services_view(request):
	return render(request,'app1/services.html')

def gallary_view(request):
	return render(request,'app1/gallary.html')

def register_view(request):
	contact=Contact.objects.all()
	return render(request,'app1/register.html',{'c':contact})

def contact_view(request):
	form=ContactForm()
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/register')
	return render(request,'app1/contact.html',{'form':form})
