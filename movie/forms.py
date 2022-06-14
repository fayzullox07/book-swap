from django import forms
from .models import Book




class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__" #['title','author','genre','desc','src']
        exclude = ["slug","user"]



        widgets = {
            
            "title": forms.TextInput(
                attrs={
                    "class": "value-input",
                    "placeholder": "Kitob nomi",
                }
            ),
            "author":forms.TextInput(
                attrs={
                    "class":"value-input",
                    "placeholder":"Kitob aftori",
                }
            ),
            "genre":forms.TextInput(
                attrs={
                    "class":"value-input",
                    "placeholder":"Kitob janri",
                    "max-length":50,
                }
            ),
            "desc":forms.TextInput(
                attrs={
                    "class":"bigger-input",
                    "placeholder":"Kitob haqida",
                }
            )
        }