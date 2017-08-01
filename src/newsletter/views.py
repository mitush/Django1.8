from django.shortcuts import render
from .forms import SignUpForm,ContactForm

def home(request):
	title="My title"
	
	# if request.method=="POST":
	# 	print request.POST
	form=SignUpForm(request.POST or None)
	context={
		"title": title,
		"form":form,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		#or use form.save() to save 
		instance.save()
		context ={
			"title":"Thankyou"
		}
		print instance
	

	return render(request,"home.html",context)

def contact(request):
	form =ContactForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data
	contact ={
	"form":form,

	}
	return render(request,"forms.html",contact)