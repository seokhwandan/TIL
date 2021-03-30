from django import forms
from .models import Article, Comment
from django.contrib.auth.models import Group


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    def __init__(self, pk, *args, **kwargs):
        topic = Article.objects.get(pk=pk)
        super().__init__(*args, **kwargs)

        t1 = topic.topic1 if topic else 'RED'
        t2 = topic.topic2 if topic else 'BLUE'

        PICKS = [
            (1, t1),
            (2, t2),
        ]
        self.fields['pick'] = forms.ChoiceField(choices=PICKS, widget=forms.Select())

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('article',)