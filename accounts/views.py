from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from accounts.forms import SubmitRequestForm
from accounts.models import TraineRequest


class IndexView(TemplateView):
    template_name = 'base.html'


class SubmitRequestView(CreateView):
    model = TraineRequest
    form_class = SubmitRequestForm
    template_name = 'request_submit.html'
    success_url = reverse_lazy('request_list')

    def form_valid(self, form):
        form = SubmitRequestForm(self.request.POST)
        form.instance.user= self.request.user

        return super(SubmitRequestView, self).form_valid(form)



class TraineRequestListView(ListView):
    model = TraineRequest
    template_name = 'request_list.html'
