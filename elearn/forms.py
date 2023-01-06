from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Courses,Exam,Marks,Teachprofile,Stuprofile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
            'email', 'password1', 'password2']

class CourseeditForm(forms.ModelForm):  
    class Meta:  
        model = Courses 
        fields = "__all__" 

class ExameditForm(forms.ModelForm):  
    class Meta:  
        model = Exam 
        fields = "__all__" 

class MarkeditForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"

class Teachprofeditform(forms.ModelForm):  
    class Meta:  
        model = Teachprofile 
        exclude = ['owner'] 

class Stuprofeditform(forms.ModelForm):  
    class Meta:  
        model = Stuprofile 
        exclude = ['owner']  