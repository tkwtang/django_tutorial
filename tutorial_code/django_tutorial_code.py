"""0. root """

-------------
"""1. create a virtual environment in conda"""
(~2mins)
conda create -n django-tutorial python=3
conda activate django-tutorial

"""2. install required package"""
pip install django numpy matplotlib


"""3. create a new project, start the server and check the admin pages"""
mkdir django_tutorial

django-admin startproject new_project django_tutorial

cd django_tutorial

python manage.py runserver


"""1. mysite/urls.py and check the following two webpages"""
127.0.0.1:8000
127.0.0.1:8000/admin


"""====================================
Step 2: make an application called new_application
===================================="""

"""5. start an app and activate it in the INSTALLED_APPS list of the settings.py"""
python manage.py startapp new_application


settings.py => add INSTALLED_APPS


"""====================================
Step 3: create a webpage with the following urls: application/index.html
===================================="""
"""1. add the second line to new_project/urls.py"""
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("application/", include("new_application.urls"))
]

"""1. create new_application/urls.py"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index", views.index, name = "index")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



"""3. create new_application/views.py"""
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponse, JsonResponse
import json, uuid
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('Agg')

# Create your views here.
def index(request):
    return render(request, "index.html")



"""====================================
Step 3: Define a function to response to the user data input
===================================="""
"""6. Add the graph_generator pattern to the urlpatterns of new_application/urls.py"""

urlpatterns = [
    path("index", views.index, name = "index"),
    path("graph_generator", views.graph_generator, name = "graph_generator")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



"""5. print data in the server and then return an empty object to the webpage """
@requires_csrf_token
def graph_generator(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(f"data from the website: ")
        print(data)

        returnData = { }

        return JsonResponse(returnData)





@requires_csrf_token
def graph_generator(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(f"data from the website: ")
        print(data)

        def plotGaussian(mean, std, N, imageName):
            sample = np.random.normal(mean, std, N)
            plt.hist(sample, bins=100)
            plt.savefig(f"new_application/static/{imageName}.png")
            plt.close()

        imageName = str(uuid.uuid4())
        plotGaussian(mean = data['mean'], std = data["std"], N = data["N"], imageName = imageName)
        print(imageName)
        returnData = {
            "imgSrc": f"{imageName}.png"
        }

        return JsonResponse(returnData)
