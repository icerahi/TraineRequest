from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from accounts.models import Profile
from projsrc.forms import CustomLoginForm

def user_login(request):
    form= CustomLoginForm()
    if request.method == "POST":
        form = CustomLoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request,user)

                get_user = Profile.objects.get(user_id=request.user.id)
                if get_user.ChangePass == True:
                    return redirect('request_list')
                else:
                    get_user.ChangePass = True
                    get_user.save()
                    return redirect('change_password')


            else:
                return redirect('login')

    context = {"form":form}

    return render(request,'login.html',context)

