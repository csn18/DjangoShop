from django.forms import ModelForm

from Shop.models import ProductColor


class ProductColorForm(ModelForm):
    class Meta:
        model = ProductColor
        fields = '__all__'
