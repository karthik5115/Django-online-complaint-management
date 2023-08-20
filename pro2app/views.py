from django.shortcuts import render, get_object_or_404
from .forms import UserForm, ProfileForm, Raise_Complaint
from .models import User, UserInfo, Complaints
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from twilio.rest import Client


def home(request):
    complaints = Complaints.objects.filter(solved=True)
    complaints = complaints[::-1]
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        print(user_info.profile.url)
        return render(request, 'home.html', {'user_info': user_info, 'complaints': complaints})
    return render(request, 'home.html', {'complaints': complaints})


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profiles = profile_form.save(commit=False)
            profiles.user = user
            if 'profile' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profiles.profile = request.FILES['profile']

            # Now save model
            profiles.save()
            user.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    print("abc")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("abc")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("user is not active..")
        else:
            return HttpResponse("invalid login")
    return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def raise_complaint(request):
    if request.user.is_authenticated:
        raisecomplaint_form = Raise_Complaint(request.POST, request.FILES)
        if request.method == 'POST':
            if raisecomplaint_form.is_valid():
                raisecomplaint_form.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                print('not a valid form')
            return HttpResponse("FORM NOT VALID")
        return render(request, 'raisecomplaint.html', {'raisecomplaint_form': raisecomplaint_form})
    return user_login(request)


def mycomplaints(request):
    if request.user.is_authenticated:
        mycomplaintslist = Complaints.objects.filter(user=request.user)
        return render(request, 'mycomplaints.html', {'mycomplaintslist': mycomplaintslist})
    return user_login(request)
# Create your views here.


def headbase(request):
    complaints = Complaints.objects.filter(solved=False)
    complaints = complaints[::-1]
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        print(user_info.profile.url)
        return render(request, 'headbase.html', {'user_info': user_info, 'complaints': complaints})
    return render(request, 'headbase.html', {'complaints': complaints})


def todo(request):
    if request.user.is_authenticated:
        todocomplaints = Complaints.objects.filter(solved=False)
        todocomplaints = todocomplaints[::-1]
        return render(request, 'todo.html', {'todocomplaints': todocomplaints})
    return user_login(request)


def solvefunc(request, pk):
    complaint = get_object_or_404(Complaints, pk=pk)
    try:
        sendmsg(request, complaint)
    except Exception as e:
        # handle the error
        print(f"Error: {e}")
    complaint.solved = True
    complaint.save()

    return todo(request)


def solved(request):
    if request.user.is_authenticated:
        todocomplaints = Complaints.objects.filter(solved=True)
        todocomplaints = todocomplaints[::-1]
        return render(request, 'solved.html', {'todocomplaints': todocomplaints})
    return user_login(request)


def addlike(request, pk):
    if not request.user.is_authenticated:
        return user_login(request)
    complaint = get_object_or_404(Complaints, pk=pk)
    user = request.user
    if user in complaint.liked_users.all():
        complaint.likes = complaint.likes-1
        complaint.liked_users.remove(user)
        complaint.save()
    else:
        complaint.likes = complaint.likes+1
        complaint.liked_users.add(user)
        complaint.save()
    return home(request)


def adddislike(request, pk):
    if not request.user.is_authenticated:
        return user_login(request)
    complaint = get_object_or_404(Complaints, pk=pk)
    user = request.user
    if user in complaint.disliked_users.all():
        complaint.dislikes = complaint.dislikes-1
        complaint.disliked_users.remove(user)
        complaint.save()
    else:
        complaint.dislikes = complaint.dislikes+1
        complaint.disliked_users.add(user)
        complaint.save()
    return home(request)


def sendmsg(request, comp):
    client = Client('ACa3a95eb4cb438e92dae7b17d79af6dc9',
                    '06bc21253879c576f4f85c29328a5823')
    num = '+91'+str(comp.phone)
    des = "hello sir/madam "+str(comp.complaint_name)+"  is solved"
    message = client.messages.create(
        body=des,
        from_='+16205089669',
        to=num
    )
    return


def tododes(request, pk):
    complaint = get_object_or_404(Complaints, pk=pk)
    return render(request, 'tododes.html', {'complaint': complaint})
