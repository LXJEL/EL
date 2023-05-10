from django.shortcuts import render
from django.shortcuts import HttpResponse
from pagemanagement import utils
from StaticFile import default_setting

import json

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def get_data(request):
    return render(request,'page1.html')

def VisualPage(request):
    return render(request,'visual.html')

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request,'about_us.html')

def help(request):
    return render(request,'help.html')

def login(request):
    return render(request,'login.html')

def get_KG(request):
    if request.method == 'POST':

        KG_ID = request.POST.get("KG_id")
        node_count=request.POST.get("number")
        # print(node_count)
        # print(KG_ID)
        global KG_list
        KG_list = []
        # KG_list.append(KG_ID)
        # print(KG_list)
        KG_list.append("Bing")
        # print(KG_list)
        knowledgegraph = get_knowledgegraph(node_count)
        # print(knowledgegraph)
    return HttpResponse(knowledgegraph)

def get_knowledgegraph(node_count):
    node_list = []
    link_list = []
    data_json = {}
    print(node_count)
    if KG_list[0] == "Bing":
        node_list, link_list = utils.get_kg_fromyago(int(node_count))
    data_json['nodes'] = node_list
    data_json['links'] = link_list
    return json.dumps(data_json)