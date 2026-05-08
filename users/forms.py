from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
GENDER =(
      ('Male', 'Male'),
      ('Female', 'Female')
   )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, initial='@gmail.com')
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=20, required=True, initial='+996')
    gender = forms.ChoiceField(choices=GENDER, required=True, initial='Male')

    class Meta:
        model = models.CustomUser
        fields = ('username',
                  'password1',
                  'password2', 
                 'photo',
                 'first_name',
                 'email',
                 'phone_number',
                    'gender')
    def save(self, commit = True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    