from django import forms 
from Crudapp.models import User

class StudentRegistration(forms.ModelForm):

    class Meta:
        model= User
        fields=['name' , 'email' , 'password' ]
        widgets={
            'name': forms.TextInput(),
            'email' : forms.EmailInput(),
            'password':forms.PasswordInput()
        }

        


