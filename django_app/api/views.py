from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict

from .models import Message2, Good2

import json

page_max = 10
# Create your views here.
@login_required(login_url="/admin/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/admin/login/")
def msgs(request, page=1):
    msgs = Message2.objects.all()
    paginate = Paginator(msgs, page_max)
    page_items = paginate.get_page(page)
    serialized_data = serialize("json", page_items)
    return HttpResponse(serialized_data, content_type="application/json")


@login_required(login_url="/admin/login/")
def plast(request):
    msgs = Message2.objects.all()
    paginate = Paginator(msgs, page_max)
    last_page = paginate.num_pages
    return JsonResponse({"result":"OK", "value":last_page})


@login_required(login_url="/admin/login/")
def usr(request, usr_id=-1):
    if usr_id == -1:
        usr = request.user
    else:
        usr = User.objects.filter(id=usr_id).first()
    return JsonResponse({"result":"OK", "value":usr.username})


@login_required(login_url="/admin/login/")
def post(request):
    if request.method == "POST":
        byte_data = request.body.decode("utf-8")
        json_body = json.loads(byte_data)

        msg = Message2()
        msg.owner = request.user
        msg.owner_name = request.user.username
        msg.content = json_body["content"]
        msg.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("NG")


@login_required(login_url="/admin/login")
def good(request, good_id):
    good_msg = Message2.objects.get(id=good_id)
    is_good = Good2.objects.filter(owner=request.user).filter(message=good_msg).count()

    if is_good > 0:
        return HttpResponse("NG")
    else:
        good_msg.good_count += 1
        good_msg.save()
        good = Good2()
        good.owner = request.user
        good.message = good_msg
        good.save()
        return HttpResponse("OK")