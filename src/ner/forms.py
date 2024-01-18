from django import forms
from django.forms import ModelForm, RadioSelect, TextInput, Textarea
from crispy_forms.helper import FormHelper
from .models import Item


class ItemFilterForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    publish = forms.BooleanField()


class ItemUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # fields that are null=true
        self.fields["date"].required = False
        self.fields["notes"].required = False
        self.fields["body"].required = False
        # fields that do not save
        self.fields["date"].disabled = True

    class Meta:
        model = Item
        fields = (
            "date",
            "author",
            "title",
            "body",
            "pool_report",
            "publish",
            "off_the_record",
            "review_status",
            "notes",
        )

        widgets = {
            "date": TextInput(attrs={"disabled": True}),
            "author": TextInput(attrs={"class": "form-control"}),
            "review_status": RadioSelect(attrs={"id": "value"}),
            "notes": Textarea(attrs={"class": "form-control"}),
        }
