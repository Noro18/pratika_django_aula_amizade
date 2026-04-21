from django  import forms
from .models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = "__all__"
        
        widgets = {
            "nre" : forms.TextInput(attrs={"class" : "form-control"}),
            "naran_estudante" : forms.TextInput(attrs={"class" : "form-control"}),
            "sexu" : forms.Select(attrs={"class" : "form-control"}),
            "idade" : forms.NumberInput(attrs={"class" : "form-control"}),
            "email" : forms.EmailInput(attrs={"class" : "form-control"}),
            "departamento" : forms.Select(attrs={"class" : "form-control"}),
            "hela_fatin" : forms.TextInput(attrs={"class" : "form-control"}),
            "nu_telefone" : forms.TextInput(attrs={"class" : "form-control"}),
            "imajen" : forms.FileInput(attrs={"class" : "form-control"}),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Prense Username"
        })
    )
    
    password = forms.CharField(
        label ="Password",
        widget=forms.PasswordInput(attrs={
            "class" : "form-control",
            "placeholder" : "Prense Password"
        })
    )