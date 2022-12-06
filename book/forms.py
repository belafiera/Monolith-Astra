from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddReview(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['the_user'].empty_label = "haven't chosen"
        self.fields['books_review'].empty_label = "haven't chosen"

    class Meta:
        model = Review
        fields = ['the_user', 'review_text', 'books_review']
        widgets = {
            'review_text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

#    def clean_books_review(self):
       # books_review = self.cleaned_data['books_review']
        # if len(books_review) > 3000:
         #   raise ValidationError('Too long review text - over 3000 symbols')

       # return books_review
