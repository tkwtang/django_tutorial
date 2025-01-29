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
