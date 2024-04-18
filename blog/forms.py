from .models import Comments
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=["blog"]
        #exclude=[]
        labels={
            "user_name":"Your Name",
            "comment_text":"Your Feedback"
            
        }
        error_messages={
            "user_name":{
                "required":"Your name must not be empty"}
        }