from django import forms
from .models import Post, Profile

class CreatePostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        
        model = Profile

        fields = ['display_name', 'profile_image_url', 'bio_text']