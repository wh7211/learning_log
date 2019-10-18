from django import forms
from .models import Topic, Entry



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'ppp', 'myt', 'ma']
        labels = {'text': '主题', 'ppp': '公开显示-所有人都能看到你发布的主题', 'myt': '测试框', 'ma': '测试邮件地址框'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
