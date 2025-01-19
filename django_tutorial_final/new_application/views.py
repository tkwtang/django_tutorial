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
