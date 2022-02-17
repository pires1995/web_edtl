from django.shortcuts import render, redirect, get_object_or_404
from news.models import NewsUser, News, NewsCategory, NewsImage
from news.forms import NewsUserSignUpForm, NewsForm, NewsImageForm, NewsImageUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import title_seo, getnewid
from datetime import datetime
import datetime
from django.contrib.auth.models import Group
import os
from news.tasks import send_email, new_news
from django.template.loader import get_template
from django.core import serializers

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import re
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
# Create your views here.

# NEWS USER


@login_required
def news_unsubscribed(request):
    form = NewsUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsUser.objects.filter(email=instance.email).exists():
            NewsUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your email has been removed',
                             'alert alert-success alert-dismissible')
        else:
            messages.warning(
                request, 'Your Email is not in the database', 'alert alert-warning alert-dismissible')
    context = {
        'form': form
    }
    template = 'main/index.html'
    return render(request, template, context)


# NEWS MANAGEMENT
@login_required
def news_list(request):

    group = request.user.groups.all()[0].name
    news = News.objects.all().order_by('-entered_date')
    context = {
        'news': news, 'title': 'News List', 'group': group
    }
    return render(request, 'news/news_list.html', context)


@login_required
def news_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(News)
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.title_seo = title_seo(form.cleaned_data.get('title'))
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add News')
            return redirect('admin-news-list')
    else:
        form = NewsForm()
    context = {
        'form': form, 'title': 'Add News'
    }
    return render(request, 'news/add.html', context)


@login_required
def news_detail(request, hashid):
    group = request.user.groups.all()[0].name
    object = get_object_or_404(News, hashed=hashid)
    images = NewsImage.objects.filter(news=object).all()
    context = {
        'object': object, 'title': 'News Detail', 'images': images,
        'group': group
    }
    return render(request, 'news/detail.html', context)


@login_required
def news_update(request, hashid):
    object = get_object_or_404(News, hashed=hashid)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.title_seo = title_seo(form.cleaned_data.get('title'))
            instance.save()
            messages.success(request, f'Successfully Update News')
            return redirect('admin-news-list')
    else:
        form = NewsForm(instance=object)
    context = {
        'form': form, 'title': 'Update News', 'object': object
    }
    return render(request, 'news/add.html', context)


@login_required
def news_activate(request, hashid):
    object = get_object_or_404(News, hashed=hashid)
    object.is_active = True
    object.save()
    messages.success(request, f'Successfully Activate News')
    return redirect('admin-news-list')


@login_required
def news_deactivate(request, hashid):
    object = get_object_or_404(News, hashed=hashid)
    object.is_active = False
    object.save()
    messages.success(request, f'Successfully Deactivate News')
    return redirect('admin-news-list')


@login_required
def news_sent(request, hashid):
    object = get_object_or_404(News, hashed=hashid)
    object.is_sent = True
    if object.is_reject:
        object.is_reject = False
        object.comment = ''
    object.save()
    messages.success(request, f'Successfully Send News')
    return redirect('admin-news-list')


@login_required
def news_approval_request_list(request):
    group = request.user.groups.all()[0].name
    news = News.objects.filter(
        is_sent=True, is_approved=False).order_by('-entered_date')
    if request.method == 'POST':
        id = request.POST.get('id')
        comments = request.POST.get('comments')
        objects = get_object_or_404(News, pk=id)
        objects.comment = comments
        objects.is_reject = True
        objects.is_sent = False
        objects.save()
        messages.success(request, f'Successfully Send News to Media')
        return redirect('admin-news-request-list')
    context = {
        'news': news, 'group': group,
        'title': 'Approval Request News List'
    }
    return render(request, 'coordinator/news_approval__request_list.html', context)


@login_required
def news_approved_list(request):
    group = request.user.groups.all()[0].name
    news = News.objects.filter(is_approved=True).order_by('-entered_date')
    context = {
        'news': news, 'group': group,
        'title': 'Approved News List'
    }
    return render(request, 'coordinator/news_approved_list.html', context)


@login_required
def news_approved2(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    objects.approved_by = request.user
    objects.approved_date = datetime.datetime.now()
    objects.is_approved = True
    subject = 'News Notification'
    body_html = render_to_string('email/send.html')
    from_email = settings.EMAIL_HOST_USER
    to_email = 'joao.pires@ti.ukdw.ac.id'
    msg = EmailMultiAlternatives(
        subject,
        body_html,
        from_email=from_email,
        to=[to_email]
    )
    msg.mixed_subtype = 'related'
    msg.attach_alternative(body_html, "text/html")
    img_dir = settings.BASE_DIR / 'static_project/web_admin/img'
    image = 'edtl.png'
    file_path = os.path.join(img_dir, image)
    print(file_path)
    with open(finders.find(file_path),'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<{name}>'.format(name=image))
        img.add_header('Content-Disposition', 'inline', filename=image)
    msg.attach(img)
    msg.send()
    # objects.save()
    messages.success(request, f'Successfully Approved News')
    return redirect('admin-news-request-list')

@login_required
def news_approved(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    objects.approved_by = request.user
    objects.approved_date = datetime.datetime.now()
    objects.is_approved = True
    # email_users = NewsUser.objects.all()
    # for email_to in email_users:
    #     set_name = email_to.email
    #     set_name2 = re.split(r'[@.]', set_name)
    #     new_news.delay(email_to.email,set_name2[0], objects.title)
    objects.save()
    messages.success(request, f'Successfully Approved News')
    return redirect('admin-news-request-list')


# NEWS IMAGES
@login_required
def news_image_add(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.getlist('image')
        for i in image:
            newid, new_hashid = getnewid(NewsImage)
            object = NewsImage.objects.create(
                id=newid,
                news=objects,
                description_tet=data['description_tet'],
                description_por=data['description_por'],
                description_eng=data['description_eng'],
                user=request.user,
                hashed=new_hashid,
                image=i
            )
        messages.success(request, f'Add Image Successfully')
        return redirect('admin-news-detail', hashid=hashid)
    else:
        form = NewsImageForm()
    context = {
        'hashid': hashid, 'objects': objects, 'form': form,
        'title': f'Add Image to news "{objects.title}"" ', 'subtitle': 'Please Fill News Image Information and Select Image'
    }
    return render(request, 'news/add.html', context)


@login_required
def news_image_update(request, hashid, hashid2):
    objects = get_object_or_404(NewsImage, hashed=hashid)
    if request.method == 'POST':
        form = NewsImageUpdateForm(
            request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Update Image')
            return redirect('admin-news-list')
    else:
        form = NewsImageUpdateForm(instance=objects)
    context = {
        'hashid': hashid, 'objects': objects, 'form': form, 'hashid2': hashid2,
        'title': 'Update News Image', 'legend': 'Update Image'
    }
    return render(request, 'news/news_image_update.html', context)


@login_required
def news_image_delete(request, hashid, hashid2):
    objects = NewsImage.objects.get(hashed=hashid)
    objects.delete()
    messages.success(request, f'Successfully Delete Image')
    return redirect('admin-news-detail', hashid2)

@login_required
def news_send(request, hashid):
    objects = get_object_or_404(News, hashed=hashid)
    template = render_to_string('email/send.html')
    email = EmailMessage(
        'Thank you',
        template,
        settings.EMAIL_HOST_USER,
        ['pires.joao1995@gmail.com']      
    )
    email.fail_silently= False
    email.content_subtype = "html"
    email.send()
    messages.success(request, f'Successfully Send Email')
    return redirect('admin-news-list')
