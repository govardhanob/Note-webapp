from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.urls import reverse
import re
from django.contrib import messages
# Create your views here.
def index(request):
    if 'tid' in request.session:
     details=Usernotes.objects.filter(email=request.session['tid'])
     return render(request, 'index.html',{'u':details})
    else:
        return render(request,'register.html')
def registering(request):
    if request.method=='POST':
        fullname=request.POST['Name']
        email=request.POST['Email']
        password=request.POST['Password']
        if Userdetails.objects.filter(email=email).exists():
            # messages.info(request,'user already exists')
            # return redirect(index)
            return HttpResponse('user already exists')
        else:
            pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
            regex = re.compile(pattern)
            if regex.match(password):
                z=Userdetails.objects.create(fullname=fullname,email=email,password=password)
                z.save()
                request.session['tid']=email

                return redirect(index)
            else:
                # messages.info(request,'password is not strong')
                # return redirect(index)
                return HttpResponse('password is not strong')
            
def loggingin(request):
    if request.method=='POST':
        email=request.POST['Email']
        password=request.POST['Password']
    
        if Userdetails.objects.filter(email=email).exists():
            user=Userdetails.objects.get(email=email)
            
            if user.password==password:
                
                
                request.session['tid']=email
                # return redirect(profile,email=email)
                return redirect(index)
            else:
                # messages.info(request,'Incorrect Password')
                # return render(request,'login.html')
                return HttpResponse('Incorrect Password')
        else:
            # return index(request,message='invalid User')
            return HttpResponse('Invalid User')
       

        
            
      



def addingnote(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        email = request.session.get('tid')
        
        try:
            note_id = request.POST.get('id')
            if note_id:
                # If ID is present, update existing note
                note = Usernotes.objects.get(id=note_id)
                note.title = title
                note.description = content
                note.save()
            else:
                # If ID is not present, add new note
                note = Usernotes(title=title, description=content, email=email)
                note.save()
        except Exception as e:
            # Handle exceptions if necessary
            print(e)
        finally:
            # Redirect to index page
            return redirect(reverse('index'))  # Make sure 'index' is the correct view name
    else:
        return HttpResponse('Method not allowed')
    
def signout(request):
    request.session.flush()
    return redirect(index)

def deletenote(request,noteid):
    note = Usernotes.objects.get(id=noteid)
    note.delete()
    return redirect(index)

