from django import forms
from django.forms.models import ModelForm

from .models import Suggestion


class CreateSuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = ('title', 'start_time', 'end_time', 'memo')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'memo': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }

    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time < start_time:
            raise forms.ValidationError(
                '終了時間は開始時間よりも後に設定してください。'
            )
        return end_time
