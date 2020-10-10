from django.shortcuts import render
from edApp.models import edsystango,ClassesForm,InstituteForm,rulesForm,feesForm
from edApp.forms import ClassesForm,SignUpForm,InstituteForm,rulesForm,feesForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/profile/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form,})

def home(request):
    return render(request,'edApp/home.html')

def dashboard(request):
    return render(request,'edApp/dashboard.html')

def classes(request):
    return render(request,'edapp/class.html')

@login_required
def Allclasses(request):
    ClassesForm.objects.all();
    return render(request,'edApp/allclasses.html')

@login_required
def Newclasses(request):
    ClassForm=ClassesForm();
    mydict={'ClassForm':ClassForm}
    if request.method=='POST':
        #DB insert code goes here
        ClassForm=ClassesForm(request.POST);
        ClassForm.save();#insert query
        print("Data inserted")
        mydict.update({'msg':'New class Registered Successfully'})
    return render(request,'edApp/newclasses.html',context=mydict)


def Editdeleteclasses(request):
    #select * from product where id='1'
    #images=Upload.objects.get(id=pid)
    #images.delete();  delete records
    return render(request,'edApp/editdeleteclasses.html')

def Subjecttoclasses(request):
    return render(request,'edApp/subjecttoclasses.html')

def Addsubject(request):
    return render(request,'edApp/addsubject.html')

def SignUpPage(request):
    signupform=SignUpForm()
    mydict={'signupform':signupform}
    if request.method=='POST':
        #DB insert code goes here
        signupform=SignUpForm(request.POST);
        if signupform.is_valid():
            user=signupform.save();#insert query
            user.set_password(user.password)
            user.save()# this object save finally
            subject="EMS Welcome Mail"
            message="Welcome "+user.email+", You are register"
            recipient_list=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Registered Successfully'})
    return render(request,'edApp/signup.html',context=mydict)

def institute(request):
    instForm=InstituteForm();
    mydict={'instForm':instForm}
    if request.method=='POST':
        #DB insert code goes here
        instForm=InstituteForm(request.POST);
        instForm.save();#insert query
        print("Data inserted")
        mydict.update({'msg':'New class Registered Successfully'})
    return render(request,'edapp/addinstitute.html',context=mydict)

def Viewinstitute(request):
    InstituteForm.objects.all();
    return render(request,'edApp/viewinstitute.html')


def rules(request):
    ruleForm=rulesForm();
    mydict={'ruleForm':ruleForm}
    if request.method=='POST':
        #DB insert code goes here
        ruleForm=rulesForm(request.POST);
        ruleForm.save();#insert query
        print("Data inserted")
        mydict.update({'msg':'Change Successfully'})
    return render(request,'edApp/rules.html',context=mydict)

def fees(request):
    feeForm=feesForm();
    mydict={'feeForm':feeForm}
    if request.method=='POST':
        #DB insert code goes here
        feeForm=feesForm(request.POST);
        feeForm.save();#insert query
        print("Data inserted")
        mydict.update({'msg':'Change Successfully'})
    return render(request,'edApp/fees.html',context=mydict)
