from django import forms
from .models import Post


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'avatar1', 'avatar2', 'avatar', 'body', 'address', 'phone_number', 'city', 'pole']