from django.shortcuts import render, HttpResponse
import json
from .models import cou, sta, cit


def home(req):
    val = list(cou.objects.all())
    state_list = sta.objects.all()
    city_list = cit.objects.all()

    return render(request=req, template_name='Home.html', context={'country_list': val, 'state_list': state_list, 'city_list': city_list})



def countries(req):
    f = open('C:\\Users\\Vinay Chopda\\Desktop\\data\\countries.json', encoding='utf-8')
    json_data = json.load(f)

    for obj in json_data:
        text = ''
        for ele in obj:
            if ele == 'id' or ele == 'name':
                continue
            text += '{'+str(ele)+':'+str(obj[ele])+'}'
        cou.objects.create(id=obj['id'], name=obj['name'], inter_data=text)

    return HttpResponse("countries")


def states(req):
    f = open('C:\\Users\\Vinay Chopda\\Desktop\\data\\states.json', encoding='utf-8')
    json_data = json.load(f)

    for obj in json_data:
        text = ''
        for ele in obj:
            if ele == 'id' or ele == 'name' or ele == 'country_id':
                continue
            text += '{'+ele+':'+str(obj[ele])+'}'
        sta.objects.create(id=obj['id'], name=obj['name'], country_id=obj['country_id'], inter_data=text)

    return HttpResponse("states")


def cities(req):
    f = open('C:\\Users\\Vinay Chopda\\Desktop\\data\\cities.json', encoding='utf-8')
    json_data = json.load(f)

    for obj in json_data:
        text = ''
        for ele in obj:
            if ele == 'id' or ele == 'name' or ele == 'country_id' or ele == 'state_id':
                continue
            text += '{' + ele + ':' + str(obj[ele]) + '}'
        cit.objects.create(id=obj['id'], name=obj['name'], country_id=obj['country_id'], state_id=obj['state_id'], inter_data=text)

    return HttpResponse("cities")
# Create your views here.
