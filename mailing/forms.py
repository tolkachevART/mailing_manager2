from django import forms
from django.forms import DateTimeInput

from mailing.models import Mailing, Client, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mail_to'].queryset = Client.email.all()

    class Meta:
        model = Mailing
        exclude = ('next_date', 'owner', 'status', 'is_activated',)
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mail_to'].queryset = Client.objects.all()


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
