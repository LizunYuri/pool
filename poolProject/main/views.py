from django.shortcuts import render
from content.models import FirstPageTitleModel


def index(request):
    titles = FirstPageTitleModel.objects.all()

    return render(request, 'main/index.html', {'titles' : titles})
