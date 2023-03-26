from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import User, Admin,Booking,WrapUser
from .forms import ProfileForm

#loader and home\
def loader(request):
    return render(request,'loader.html')
def get_start(request):
    return render(request,'get_start.html')
# Admin pages

def admin_home(request):
    if 'aname' in request.session:
        data = {'name':request.session.get('aname')}
        return render(request,'admin_home.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'admin_login.html',context=data)
    
def login_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = Admin.objects.get(name=name)

            if user.password == password:
                request.session['aname'] = name
                # return HttpResponse('ffaf')
                return admin_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'admin_login.html',context=data)

        except Exception as e:
            data = {'status':"Invalid Username"}
            return render(request,'admin_login.html',context=data)
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")


def admin_logout(request):
    if 'aname' in request.session:
        del request.session['aname']

    return render(request,'admin_login.html')

#user registration
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')

        if(password == re_password):
            user = User(name=name,email=email,photo=photo,password=password)
            user.save()
            email = [email]
            request.session['uname'] = name
            request.session['email'] = email
            return dashboard(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'signup.html',context=data)
    else:
        return render(request, 'signup.html')
    
def signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(name=name,email=email)

        if user.password == password:
            request.session['uname'] = name
            request.session['email'] = email
            return redirect("dashboard")
        else:
            data = {'status':"Incorrect Password!!!"}
            return render(request,'signin.html',context=data)
    else:
        return render(request, 'signin.html')



def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    return render(request,'signin.html')

#User Home Page
def dashboard(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'sigin.html',context=data)
    
def booking(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        bookings = Booking.objects.all()
        # return render(request,'booking.html',context=data)
        return render(request,'booking.html',{'bookings': bookings})
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def rewards(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'rewards.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def track(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'track.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
#dashboard pages
def dropoff(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard/dropoff.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def pickup(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        if request.method == 'POST':
            users  = User.objects.get(name=request.session['uname'])
            print(users.email)
            wastetype = request.POST.get('wastetype')
            date = request.POST.get('date')
            booking_address = request.POST.get('booking_address')
            print(date)
            book = Booking(wastetype=wastetype,name=users.name,uid=users.uid ,date=date,email=users.email, booking_address=booking_address)
            book.save()
        return render(request,'dashboard/pickup.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def purchase(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard/purchase.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def report(request):
    if 'uname' in request.session:
        data = {'name':request.session.get('uname')}
        return render(request,'dashboard/report.html',context=data)
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)
    
def profile(request):
    if request.method == 'POST':
        user= User()
        user.name = request.POST.get('uname')
        user.email = request.POST.get('email')
        user.photo = request.FILES.get('photo')
        
        data = {'name':request.session.get('uname')}
        if user.photo:
            user.photo = request.FILES.get('photo')
        user = User(name=name,email=email,photo=user.photo)
        user.save()
        return redirect('profile')
    else:
         if 'uname' in request.session:
            name = request.session.get('uname')
            email = request.session.get('email')
            # password = {'name':request.session.get('password')}
            my_dict = {
                'name': name,
                'email':email
            }
            return render(request,'profile.html',my_dict)
         else:
            data = {'status':'You need to login first'}
            return render(request,'signin.html',context=data)


#notification
def notification(request):
    if 'uname' in request.session:
        return render(request,'notification.html')
    else:
        data = {'status':'You need to login first'}
        return render(request,'signin.html',context=data)