from rest_framework import serializers
from product.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id',
                  'title',
                  'price',
                  'short_description',
                  'description',
                  'is_active',
                  'is_delete',
                  ]
