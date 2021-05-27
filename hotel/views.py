from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from user.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# Create your views here.
@login_required(login_url='/login')
def index(request):
    user = request.user
    form = createHotel(initial={'manager_id': user.id})
    form.fields['manager_id'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = createHotel(request.post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'pages/createHotel.html', {"user": user, "form": form})


def about_us_view(request):
    return render(request, 'pages/about.html', {
        'nav': 'about'
    })

# def userView(request):
#     user = User.uname
#     recommend = {"hotels": Hotels.objects.get()}
#     return render(request, 'pages/home.html', user, recommend)


@login_required
def CreateRoomType(request):
    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':

        roomTypeForm = RoomTypeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())


        if roomTypeForm.is_valid() and formset.is_valid():
            post_form = roomTypeForm.save(commit=False)
            # post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Image(room_type=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return HttpResponseRedirect("/")
        else:
            print(roomTypeForm.errors, formset.errors)
    else:
        roomTypeForm = RoomTypeForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'index.html',
                  {'roomTypeForm': roomTypeForm, 'formset': formset},
                  context_instance=RequestContext(request))