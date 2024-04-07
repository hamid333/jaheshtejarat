from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def transportation_air(request):
    form = Transportation_Air_Form()
    if request.method == "POST":
        form = Transportation_Air_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_air')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_air')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/transportation/transportation_air.html', context)

@login_required
def transportation_road(request):
    form = Transportation_Road_Form()
    if request.method == "POST":
        form = Transportation_Road_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_road')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_road')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/transportation/transportation_road.html', context)

@login_required
def transportation_maritime(request):
    form = Transportation_Maritime_Form()
    if request.method == "POST":
        form = Transportation_Maritime_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_maritime')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_maritime')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/transportation/transportation_maritime.html', context)

@login_required
def transportation_about(request):
    form = Transportation_About_Form()
    if request.method == "POST":
        form = Transportation_About_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_air')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_air')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/transportation/transportation_about.html', context)

@login_required
def transportation_members(request):
    members = Transportation_Members.objects.all()
    form = Transportation_Members_Form()
    if request.method == "POST":
        form = Transportation_Members_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_members')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_members')

    context = {
        'form': form,
        'members': members
    }

    return render(request, 'dashboard/transportation/transportation_members.html', context)

@login_required
def transportation_member_update(request, id):
    members = Transportation_Members.objects.all()
    member = Transportation_Members.objects.get(id=id)
    form = Transportation_Members_Form(instance=member)
    if request.method == "POST":
        form = Transportation_Members_Form(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_members')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_members')
    context = {
        'form': form,
        'members': members,
    }
    return render(request, 'dashboard/transportation/transportation_members.html', context)


@login_required
def transportation_certificate(request):
    certificates = Transportation_Certificate.objects.all()
    form = Transportation_Certificate_Form()
    if request.method == "POST":
        form = Transportation_Certificate_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_certificate')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_certificate')

    context = {
        'form': form,
        'certificates': certificates,
    }

    return render(request, 'dashboard/transportation/transportation_certificate.html', context)

@login_required
def transportation_certificate_update(request, id):
    certificates = Transportation_Certificate.objects.all()
    certificate = Transportation_Certificate.objects.get(id=id)
    form = Transportation_Certificate_Form(instance=certificate)
    if request.method == "POST":
        form = Transportation_Certificate_Form(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'ثبت با موفقیت انجام شد')
            return redirect('transportation_certificate')
        else:
            messages.add_message(request, messages.WARNING, 'خطا در ثبت اطلاعات')
            return redirect('transportation_certificate')

    context = {
        'form': form,
        'certificate': certificate,
        'certificates': certificates,
    }

    return render(request, 'dashboard/transportation/transportation_certificate.html', context)
