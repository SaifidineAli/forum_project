from django import forms
from .models import Category, SubCategory, Thread, Post

class CategoryForm(forms.ModelForm):
    #edit_category = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Category
        fields = ('name', 'description')
        #widgets = {
        #    'description': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        #}
        

class CreateSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('name', 'description')
        
        
class EditSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('category', 'name', 'description')
        
        
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title',)
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }