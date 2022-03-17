from turtle import title
from django import forms

class ProfileForm(forms.Form):
    user_file = forms.FileField()
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'test'