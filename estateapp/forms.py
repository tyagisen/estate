from django import forms
from .models import HomeFeatures,Home,UserProfile

class HomeFeaturesForm(forms.ModelForm):
    feature_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    total_feature=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= HomeFeatures
        fields='__all__'

class HomeDForm(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    name=forms.ModelChoiceField(queryset=UserProfile.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    date_built= forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"])
    image=forms.ImageField()
    house_type= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    street_no =forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    property_size= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    property_type= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file= forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

    # Error on Saving ManytoManyFieldData
    features=HomeFeatures.objects.all()

    class Meta:
        model= Home
        fields='__all__'
