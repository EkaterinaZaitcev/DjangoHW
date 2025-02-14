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
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name:
            for word in ban_words:
                if word in name.lower():
                    raise ValidationError(f'Слово "{word}" недопустимо в имени товара')
        return name

    def clean_description(self):
        ban_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        description = self.cleaned_data.get('description')
        if description:
            for word in ban_words:
                if word in description.lower():
                    raise ValidationError(f'Слово "{word}" недопустимо в описании товара')
        return description


    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price and price < 0:
           raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        valid_extensions = ('jpg', 'png', 'jpeg')
        _, ext = image.name.rsplit('.', maxsplit=1)
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер файла не должен превышать 5 МБ.")
            if ext not in valid_extensions:
                raise ValidationError("Недопустимый формат файла. Загрузите JPEG или PNG.")
        return image
