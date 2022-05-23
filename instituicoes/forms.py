from instituicoes.models import Instituicoes
from django import forms

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Instituicoes
        fields = ('inst_name', 'inst_cnpj', 'logo', 'description', 'cat', 'alt_logo', 'is_active', 'image_data',)
        labels = { 'image_data': "Upload Image" }
        widgets = {
            'image_data' : forms.FileInput(attrs={'multiple': False})
        }