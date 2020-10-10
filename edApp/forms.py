from django import forms
from django.contrib.auth.models import User
from .models import edsystango,ClassesForm,InstituteForm,rulesForm,feesForm

class ClassesForm(forms.ModelForm):
    class Meta:
        model=ClassesForm
        fields='__all__' # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}

class InstituteForm(forms.ModelForm):
    class Meta:
        model=InstituteForm
        fields='__all__' # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}


class rulesForm(forms.ModelForm):
    class Meta:
        model=rulesForm
        fields='__all__' # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}


class feesForm(forms.ModelForm):
    class Meta:
        model=feesForm
        fields='__all__' # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}
