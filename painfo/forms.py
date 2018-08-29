from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Painf

class RegistrationForm(UserCreationForm):

    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.frist_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields =(
            'email',
            'first_name',
            'last_name',
            'password'
            )

class painfof(forms.Form):
    uhid = forms.IntegerField()
   # name = forms.CharField()
  #  date = forms.DateField()
  #  ipno = forms.CharField()

   # types = forms.CharField()
  #  dep = forms.CharField()
   # doc = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class edit_info(forms.Form):
   # uhid = forms.IntegerField()
    name = forms.CharField()
  #  date = forms.DateField(input_formats=('%d-%m-%Y'))
  #  ipno = forms.CharField()

    #types = forms.CharField()
    #dep = forms.CharField()
class sepainfo(forms.Form):

    Search=forms.CharField()

class seipno(forms.Form):

    Enter_Ipno_to_Delete=forms.CharField()

class dephoto(forms.Form):

    Enter_Document_Name_to_Delete=forms.CharField()



class docfile(forms.Form):
    doc=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class ipn(forms.Form):
    ipno=forms.CharField()


class editipno(forms.Form):

    ipno = forms.CharField()
    types = forms.CharField()
    dep = forms.CharField()
 #   doc=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
class ipno_edit(forms.Form):
    types = forms.CharField()
    dep = forms.CharField()
    #doc=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

##    class Meta:
##        model = docs
##        fields = ('doc',)









