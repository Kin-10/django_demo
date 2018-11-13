from django.shortcuts import render,HttpResponse
from .service.HomeService import HomeService

service = HomeService()

# Create your views here.
def page_index(request):
    """
    :param request:
    :return:
    """
    params = {
        "name":"hello Django"
    }
    return render(request,"app1/home/index.html",params)


def page_data(request):
    """
    :param request:
    :return:
    """
    data = service.get_list()
    params = {
        "data":data
    }
    return render(request,"app1/home/data.html",params)