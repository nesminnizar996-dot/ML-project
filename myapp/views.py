from django.shortcuts import render
import pickle
import numpy as np
import os
from django.conf import settings

model = pickle.load(open('myapp/migration_model.pkl', 'rb'))
encoder = pickle.load(open('myapp/result.pkl', 'rb'))

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def prediction(request):

    result=None

    if request.method=="POST":

        male = int(request.POST['male'])
        female = int(request.POST['female'])
        children = int(request.POST['children'])
        youth = int(request.POST['youth'])
        adult = int(request.POST['adult'])
        seniors = int(request.POST['seniors'])

        data = np.array([[male,female,children,youth,adult,seniors]])

        prediction = model.predict(data)

        result = encoder.inverse_transform(prediction)

    return render(request,'prediction.html',{'result':result})