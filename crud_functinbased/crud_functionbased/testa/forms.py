from django import forms
from .models import Student


class StudentRegistration(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

    def clean_email(self):
        # this is step for debuging
        # import pdb; pdb.set_trace()
        # breakpoint()
        if Student.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise forms.ValidationError("A minimum of 5 characters is required")
        elif len(password) < 8:
            raise forms.ValidationError("Password length should not be less than 8 characters")
        elif not password.capitalize():
            raise forms.ValidationError("Make sure your password has a capital letter in it")
        elif not password.isdigit():
            raise forms.ValidationError("Make sure your password has a number in it")
        return password





