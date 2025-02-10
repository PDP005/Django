from django import forms

class FrmAlumno(forms.Form):
    nombre=forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control','placeholder':"Tu nombre"}))
    contra=forms.CharField(min_length=6,widget=forms.TextInput({'class':'form-control','placeholder':"Contra"}))
