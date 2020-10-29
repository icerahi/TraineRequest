from django.forms import ModelForm

from accounts.models import TraineRequest


class SubmitRequestForm(ModelForm):

    class Meta:
        model = TraineRequest
        fields = ('title','employee_id','employee_name','designation',
                 'email','designation','zone','branch')

    def __init__(self, *args, **kwargs):
        super(SubmitRequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['employee_id'].widget.attrs['class'] = 'form-control'
        self.fields['employee_name'].widget.attrs['class'] = 'form-control'
        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['zone'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].widget.attrs['class'] = 'form-control'