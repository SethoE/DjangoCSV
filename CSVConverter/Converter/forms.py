from django import forms

class ConverterForm(forms.Form):
    user_file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(ConverterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['id'] = 'selectFile'
            visible.field.widget.attrs['accept'] = '.csv'

