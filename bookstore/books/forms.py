from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        fields = '__all__'