from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

'''
	Here I am using a class SignUpAdmin inherirting admin.ModelAdmin
	to add some extra info to the rows created
'''
class SignUpAdmin(admin.ModelAdmin):
	list_display =["__unicode__","timestamp","updated"]
	form 		 =SignUpForm
	# class Meta:
	# 	model    = SignUp


admin.site.register(SignUp,SignUpAdmin)