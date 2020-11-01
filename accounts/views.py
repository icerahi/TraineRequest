from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from accounts.forms import SubmitRequestForm, ProfileEditForm
from accounts.models import TraineRequest



class SubmitRequestView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = TraineRequest
    form_class = SubmitRequestForm
    template_name = 'request_submit.html'
    success_url = reverse_lazy('request_list')
    success_message = '"New Traine Request has been created!"'

    def form_valid(self, form):
        form = SubmitRequestForm(self.request.POST)
        form.instance.user= self.request.user

        return super(SubmitRequestView, self).form_valid(form)



class SubmitRequestUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=TraineRequest
    form_class = SubmitRequestForm
    template_name = 'request_update.html'
    success_url = reverse_lazy('request_list')
    success_message = ' "Request has been updated!"'


class SubmitRequestDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model=TraineRequest
    template_name = 'request_delete_confirm.html'
    success_url = reverse_lazy('request_list')
    success_message = '"Request has been deleted!"'


class TraineRequestListView(SuccessMessageMixin,LoginRequiredMixin,ListView):
    model = TraineRequest
    template_name = 'request_list.html'
    
    def get_queryset(self,*args,**kwargs):
       queryset=TraineRequest.objects.all()
       queryset=queryset.filter(user=self.request.user)
       return queryset


class UserInfo(LoginRequiredMixin,DetailView):
    queryset = User.objects.all()
    models = User
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))


@login_required()
def profile_edit(request,pk,username):

    if request.method == "POST":
        profile_form = ProfileEditForm(request.POST or None,instance=request.user)
        if profile_form.is_valid():
            profile_form.user = request.user
            profile_form.save()
            return redirect('profile',pk=request.user.pk,username=request.user.username)
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)


    context ={

            'profile_form':profile_form,
        }
    return render(request,'profile_edit.html',context)


