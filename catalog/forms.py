from django.forms import ModelForm, BooleanField
from .models import Product, Category
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        ban_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        name = self.cleaned_data.get('name')
        for word in ban_words:
            if word in name.lower():
                raise ValidationError(f'Слово "{word}" недопустимо в имени товара')
        return name

    def clean_description(self):
        ban_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        description = self.cleaned_data.get('description')
        for word in ban_words:
            if word in description.lower():
                raise ValidationError(f'Слово "{word}" недопустимо в описании товара')
        return description


    def clean_price(self):

        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 0:
           raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_photo(self):
        image = self.cleaned_data.get('image')


        if image:
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError('Только JPEG или PNG.')


            if image.size > 5 * 1024 * 1024:  # 5 МБ
                raise ValidationError('Размер файла не выше 5 МБ.')

        return image
