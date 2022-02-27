from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = 'title', 'content', 'image', 'author', 'slug', 'tags'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control fh5co_contact_text_box'}),
            'content': CKEditorUploadingWidget(attrs={'class': "form-control fh5co_contacts_message m-0"}),
            'author': forms.TextInput(attrs={'class': 'form-control fh5co_contact_text_box'}),
            'slug': forms.TextInput(attrs={'class': 'form-control fh5co_contact_text_box'}),
            'tags': forms.SelectMultiple(attrs={}),
        }
