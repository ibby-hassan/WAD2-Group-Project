from django import forms
from django.contrib.auth.models import User
from insQuire.models import UserProfile, Question, Answer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'category']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
