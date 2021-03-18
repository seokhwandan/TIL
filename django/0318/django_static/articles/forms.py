from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # form 꾸미기
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'class': 'my-title abc',
                'placeholder': "제목을 10자로 적어주세요.",
            }
        )
    )

    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 적어주세요.',
            }
        )
    )
    # 메타 데이터를 저장하는 class
    class Meta:
        model = Article
        # 원하는 필드만 입력받을 경우
        # field = ('title', 'content')
        # 모든 필드를 입력받고 싶은 경우
        fields = '__all__'