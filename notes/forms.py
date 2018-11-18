from django import forms
from django.contrib.auth.models import User

from notes.models import UserProfileInfo,notes
from .models import comments


#form for registering user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label = 'Your Password')

    class Meta():
        model = User
        fields = ('username','email','password')
#form for posting notes
class notes_form(forms.ModelForm):

    class Meta():
        model = notes
        fields = ('author','tag','title','content','published_date','image')

class CommentForm(forms.ModelForm):


    class Meta():
        model = comments
        fields = ('name','comment_tag','post_comment')
