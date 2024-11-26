from django import forms
from .models import Feedback


# 1. Approach without model

# class FeedbackForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label="Your Name", error_messages={
#         "required": "The username should not be empty",
#         "max_length": "The username should be small"
#     })
    
#     remarks = forms.CharField(max_length=200, widget=forms.Textarea)

#     rating = forms.IntegerField(max_value=5, min_value=1)


# 2. Approach with model

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = "__all__"
        # fields = ["username","rating"]
        # exclude = ['owner_content']
        labels = {"username": "Your Name", "description": "Remarks"}
        error_messages = {"username": {"required": "The username should not be empty", "max_length": "The username should be small"}}