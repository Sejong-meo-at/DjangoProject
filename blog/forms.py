from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import WordPost,Comment, WordBook

class WordPostForm(forms.ModelForm):

     class Meta:
         model = WordPost
         # fields = ('title', 'text',)
         fields = ('change_word', 'word_mean', 'change_word_reason', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'text',)

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
