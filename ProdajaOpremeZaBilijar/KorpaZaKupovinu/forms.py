from django import forms
CHOOSE_NUMBER_OF_PRODUCT = [(i, str(i)) for i in range(1, 11)]

class FormaZaDodavanjeProizvodaUKorpu(forms.Form):
    quantity = forms.TypedChoiceField( choices=CHOOSE_NUMBER_OF_PRODUCT, empty_value=1,coerce=int ) # convert to int
    add_to_quantity = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)