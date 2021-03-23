from django import forms
class Bar(forms.Form):
    def __init__(self, fields, *args, **kwargs):
        super(Bar, self).__init__(*args, **kwargs)
        for i in range(len(fields)):
            self.fields['%s' %fields[i]] = forms.CharField()

class Foo(forms.Form):
    field = forms.CharField()
