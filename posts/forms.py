from django.core.exceptions import ValidationError
from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'body', 'url', 'categories', 'fecha_publicacion']

    def clean_body(self):
        body = self.cleaned_data.get('body')
        BADWORDS = ['fuck', 'bastard', 'asshole', 'shit', 'Abollao', 'Limpiatubos', 'Mascachapas']
        for badword in BADWORDS:
            if badword.lower() in body.lower():
                raise ValidationError('{0} is a badword'.format(badword))
        return body
