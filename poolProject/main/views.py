from django.shortcuts import render, get_object_or_404
from content.models import FirstPageTitleModel, FirstPageAboutModel
from catalog.models import ServicesModel


def index(request):
    titles = FirstPageTitleModel.objects.all()
    services = ServicesModel.objects.all()
    abouts = FirstPageAboutModel.objects.all()

    return render(request, 'main/index.html', {'titles' : titles,
                                               'services' : services,
                                               'abouts' : abouts})



def service_detail(request, pk):
    service = get_object_or_404(ServicesModel, pk=pk)

    return render(request, 'catalog/services_detail.html', {'service' : service})