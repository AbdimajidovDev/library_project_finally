from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ('title', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        price = data.get('price', None)


        if not title.isalpha():
           raise ValidationError(
               {  'status': False,
                   'message': "Sarlavha harflardan tashkil topgan bo'lishi kerak!"})

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {   'status': False,
                    'message': "Bunday kitob allaqachon mavjud!!!"})

        if price <= 0:
            raise ValidationError(
                {'status': False,
                 'message': 'Narx 0dan kichik bo\'lishi mumkin emas!'})

        return data
