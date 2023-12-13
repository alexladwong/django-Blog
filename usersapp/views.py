from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # context = {"title": "Register"}
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account Successfully Created for {username}, Login In Here!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request,
        "usersapp/register.html",
        {"form": form},
    )


# User's Profile
@login_required
def profile(request):
    context = {"title": "Profile"}
    return render(request, "usersapp/profile.html")


@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"You Successfully Updated your Profile!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form, "title": "Profile Update"}
    return render(request, "usersapp/profile_update.html", context)
