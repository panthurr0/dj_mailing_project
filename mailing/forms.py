from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from mailing.models import Mailing


class MixinForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class MailingForm(MixinForms):

    class Meta:
        model = Mailing
        fields = ['start_time', 'end_time', 'frequency', 'clients', 'mail']
        widgets = {
            'start_time': DateTimePickerInput(),
            'end_time': DateTimePickerInput(),
        }