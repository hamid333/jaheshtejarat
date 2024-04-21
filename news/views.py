from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import NewsTransportationForm
from .models import News_Transportation

# Create your views here.

from accounts.models import CustomUser

@login_required
def List_News(request):
    list = News_Transportation.objects.all()
    context = {
        'list': list,
    }

    return render(request, 'news/list_news.html', context)

@login_required
def news_transportation(request):
    print(request.user)
    form = NewsTransportationForm()
    if request.method == "POST":
        form = NewsTransportationForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = get_object_or_404(CustomUser, id=request.user.id)
            fs.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('List_News')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('List_News')
    context = {
        'form': form,
    }

    return render(request, 'news/add_news.html', context)

@login_required
def news_transportation_update(request,id):
    list = News_Transportation.objects.get(id=id)
    form = NewsTransportationForm(instance=list)
    if request.method == "POST":
        form = NewsTransportationForm(request.POST, request.FILES, instance=list)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = get_object_or_404(CustomUser, id=request.user.id)
            fs.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('List_News')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('List_News')
    context = {
        'form': form,
    }
    return render(request, 'news/add_news.html', context)
