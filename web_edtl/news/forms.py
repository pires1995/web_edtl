
from django import forms
from news.models import NewsUser, News, NewsImage, NewsComment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML


class DateInput(forms.DateInput):
    input_type = 'date'


class NewsUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsUser
        fields = ['email']
        labels = {
            'email': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email'
            })
        }

        # def __init__(self, *args, **kwargs):
        #     super(NewsUserSignUpForm, self).__init__(*args, **kwargs)
        #     self.fields['email'].label = ""

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email


class NewsForm(forms.ModelForm):
    title = forms.CharField(label="Title")
    headline = forms.CharField(label="Headline", widget=forms.Textarea(
        attrs={"rows": 3}), required=False)
    content = forms.CharField(label="Content", widget=SummernoteWidget(
        attrs={'summernote': {'width': '100%', 'height': '400px'}}))

    class Meta:
        model = News
        fields = ['language', 'news_category', 'title',
                  'headline', 'content', 'image', 'image_description']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        # self.fields['image'].required = True
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('language', css_class='form-group col-md-2 mb-0'),
                Column('news_category', css_class='form-group col-md-2 mb-0'),
                Column('image', css_class='form-group col-md-4 mb-0'),
                Column('image_description',
                       css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('title', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('headline', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('content', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" type="submit"><i class="bi bi-lock text-white"></i> Save</button> """)
        )

class NewsCommentForm(forms.ModelForm):

    class Meta:
        model = NewsComment
        fields = ['name', 'email', 'comments']

    def __init__(self, *args, **kwargs):
        super(NewsCommentForm, self).__init__(*args, **kwargs)
        # self.fields['image'].required = True
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('comments', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary text-white" type="submit">Post Comment</button> """)
        )


class NewsImageForm(forms.ModelForm):
    image = forms.FileField(label="Upload image", required=True,
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))
    description_tet = forms.CharField(
        label="Description (Tetum)", required=False, widget=forms.Textarea(attrs={"rows": 3}))
    description_por = forms.CharField(
        label="Description (Portugues)", required=False, widget=forms.Textarea(attrs={"rows": 3}))
    description_eng = forms.CharField(
        label="Description (English)", required=False, widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = NewsImage
        fields = ['description_tet', 'description_por',
                  'description_eng', 'image']

    def __init__(self, *args, **kwargs):
        super(NewsImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('description_tet', css_class='form-group col-md-4 mb-0'),
                Column('description_por', css_class='form-group col-md-4 mb-0'),
                Column('description_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML(
                """ <a class="btn btn-secondary" href="{% url 'admin-news-detail' hashid %}"><i class="fa fa-close"></i> Fila</a> """),
            HTML(""" <button class="btn btn-primary" type="submit"> Rai <i class="fa fa-save"></i></button> """)
        )


class NewsImageUpdateForm(forms.ModelForm):
    image = forms.FileField(label="Upload image", required=True)
    description_tet = forms.CharField(
        label="Description (Tetum)", required=False, widget=forms.Textarea(attrs={"rows": 3}))
    description_por = forms.CharField(
        label="Description (Portugues)", required=False, widget=forms.Textarea(attrs={"rows": 3}))
    description_eng = forms.CharField(
        label="Description (English)", required=False, widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = NewsImage
        fields = ['description_tet', 'description_por',
                  'description_eng', 'image']

    def __init__(self, *args, **kwargs):
        super(NewsImageUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('description_tet', css_class='form-group col-md-4 mb-0'),
                Column('description_por', css_class='form-group col-md-4 mb-0'),
                Column('description_eng', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML(
                """ <a class="btn btn-secondary" href="{% url 'admin-news-detail' hashid2 %}"><i class="bi bi-backspace"></i> Back</a> """),
            HTML(""" <button class="btn btn-primary" type="submit"> Save <i class="bi bi-lock"></i></button> """)
        )
