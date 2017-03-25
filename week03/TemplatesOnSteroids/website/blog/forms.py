from django import forms
from .models import BlogPost, Tag


class BlogPostCreateModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['tags'].required = False

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'tags')


class TagCreateModelForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)


class CommentForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

