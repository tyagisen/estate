from django import forms
from .models import HomeFeatures

class HomeFeaturesForm(forms.ModelForm):
    Feature_Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Total_feature=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= HomeFeatures
        fields='__all__'