import pytz
from django import forms
from .models import Task, StudentList


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']
class SearchForm(forms.Form):
    query = forms.CharField(label='Search Contacts', max_length=100)

class UploadFileForm(forms.Form):
    file = forms.FileField()