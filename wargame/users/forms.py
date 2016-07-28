from django import forms


class UserForm (forms.ModelForm):

  class Meta:
    model = Users
    widgets = {
      'password': forms.PasswordInput (),
    }

