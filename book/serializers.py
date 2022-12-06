from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"