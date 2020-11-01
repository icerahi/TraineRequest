from django.contrib.auth.models import User
from django.forms import ModelForm, forms

from accounts.models import TraineRequest, Profile


class SubmitRequestForm(ModelForm):

    class Meta:
        model = TraineRequest
        fields = ('title','employee_id','employee_name','designation',
                 'designation','zone','branch')

    def __init__(self, *args, **kwargs):
        super(SubmitRequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['employee_id'].widget.attrs['class'] = 'form-control'
        self.fields['employee_name'].widget.attrs['class'] = 'form-control'

        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['zone'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].widget.attrs['class'] = 'form-control'

# class UserEditForm(ModelForm):
#
#     class Meta:
#         model = User
#         fields= ('email',)
#     def __init__(self, *args, **kwargs):
#         super(UserEditForm, self).__init__(*args, **kwargs)
#         self.fields['email'].widget.attrs['class'] = 'form-control'

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('designation','zone','branch')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['zone'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].widget.attrs['class'] = 'form-control'