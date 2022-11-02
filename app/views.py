from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import UserData


@login_required
def index(request):
    return render(request, "app/index.html")


class UserListView(LoginRequiredMixin, generic.ListView):
    model = UserData
    queryset = UserData.objects.all()


def user_data_list_view(request):
    user_data_list = UserData.objects.all()

    context = {
        "user_data_list": user_data_list
    }

    return render(request, "app/data.html", context=context)
