from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Friend, Message
from .forms import SearchForm
from .forms import FriendForm, MessageForm
from .forms import FindForm
from .forms import CheckForm
from django.shortcuts import redirect
from django.db.models import Q
from django.db.models import Count
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Min
from django.db.models import Max
from django.core.paginator import Paginator
# from .forms import SessionForm
# from .forms import HelloForm


## ミドルウェア
def sample_middleware(get_response):

    def middleware(request):
        counter = request.session.get('counter',0)
        request.session['counter'] = counter + 1
        response = get_response(request)
        print("count:" + str(counter))
        return response
    return middleware


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    # re1 = Friend.objects.aggregate(Count('age'))
    # re2 = Friend.objects.aggregate(Sum('age'))
    # re3 = Friend.objects.aggregate(Avg('age'))
    # re4 = Friend.objects.aggregate(Min('age'))
    # re5 = Friend.objects.aggregate(Max('age'))

    # msg = "count:" + str(re1['age__count']) + "<br>Sum:" + str(re2['age__sum']) + "<br>Avg:" + str(re3['age__avg']) + "<br>Min:" + str(re4['age__min']) + "<br>Max:" + str(re5['age__max'])

    params = {
        'title':'Hello',
        'message':'all friends',
        # 'form':SearchForm(),
        'data':page.get_page(num),
        # 'msg':msg
    }
    # if(request.method == "POST"):
    #     num = request.POST['id']
    #     try:
    #         item = Friend.objects.get(id=num)
    #         params['data'] = [item]
    #     except:
    #         pass
    #     params['form'] = SearchForm(request.POST)
    return render(request,"hello/index.html",params)


def create(request):
    if(request.method == "POST"):
        obj = Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")
    params={
        "title":"Hello",
        "form":FriendForm(),
        # "form":HelloForm(),
    }
    # if(request.method=="POST"):
    #     name = request.POST['name']
    #     mail = request.POST['mail']
    #     gender = "gender" in request.POST
    #     age = request.POST['age']
    #     birthday = request.POST['birthday']
    #     friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birthday)

    #     friend.save()
        
    #     return redirect(to="/hello")

    return render(request,"hello/create.html",params)


## edit
def edit(request, num):
    obj = Friend.objects.get(id=num)

    if(request.method == "POST"):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")

    params={
        'title':'Hello',
        'form':FriendForm(instance=obj),
        'id':num,
    }

    return render(request,"hello/edit.html",params)


## delete
def delete(request, num):
    obj = Friend.objects.get(id=num)

    if(request.method == "POST"):
        obj.delete()
        return redirect(to="/hello")

    params={
        'title':'Hello',
        'obj':obj,
        'id':num,
    }

    return render(request,"hello/delete.html",params)


# find関数
# def find(request):
#     if(request.method == 'POST'):
#         find = request.POST['find']
#         # data = Friend.objects.filter(Q(name__contains=find) | Q(mail__contains=find))
#         list = find.split() # 半角スペースで区切ってリスト化
#         # data = Friend.objects.filter(name__in=list)
#         data = Friend.objects.all()[int(list[0]):int(list[1])]
#         msg = '検索結果:'+str(data.count())
#     else:
#         msg = '検索ワード'
#         data = Friend.objects.all()
#     params = {
#         'title':'Hello',
#         'message':msg,
#         'form':FindForm(),
#         'data':data,
#     }

#     return render(request, 'hello/find.html', params)


def findSql(request):
    if(request.method == 'POST'):
        find = request.POST['find']
        sql = "select * from hello_friend"

        if (find != ''):
            sql += ' where ' + find
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = '検索ワード'
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':FindForm(),
        'data':data,
    }

    return render(request, 'hello/find.html', params)


def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form':FriendForm(),
    }
    if (request.method == 'POST'):
        form = FriendForm(request.POST)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'

    return render(request, 'hello/check.html', params)


def message(request, page=1):
    if (request.method == "POST"):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title':'Message',
        'form':MessageForm(),
        'data':paginator.get_page(page),
    }

    return render(request, "hello/message.html", params)


class FriendList(ListView):
    model = Friend


class FriendDetail(DetailView):
    model = Friend


## getリクエストの受け取り方
# Create your views here.
# def index(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'you typed:"' + msg + '".'
#     else:
#         result = 'please send msg parameter!'

## 
# def index(request,id,nickname):
#     result = 'id: ' + str(id) + "name: " + nickname
#     return HttpResponse(result)

## ３ページ遷移
# def index(request):
#     params = {
#         'title':'hello/index',
#         'msg':'this is sample page',
#         'goto':'next'
#     }
#     return render(request,'hello/index.html',params)
# def next(request):
#     params = {
#         'title':'hello/next',
#         'msg':'this is next page',
#         'goto':'test'
#     }
#     return render(request,'hello/index.html',params)
# def test(request):
#     params = {
#         'title':'hello/test',
#         'msg':'this is test page',
#         'goto':'index'
#     }
#     return render(request,'hello/index.html',params)

## formを作る
# def index(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'お名前は?'
#     }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title':'Hello/Form',
#         'msg':'こんにちは' + msg + 'さん。'
#     }
#     return render(request, 'hello/index.html', params)

## forms.pyを使ってformを作る
# def index(request):
#     params = {
#         'title':'Hello',
#         'message':'your data',
#         'form':HelloForm()
#     }
#     if request.method == 'POST':
#         params['message'] = '名前' + request.POST['name'] + \
#             '<br>メール:' + request.POST['mail'] + \
#             '<br>年齢:' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request,'hello/index.html',params)

## HelloViewクラスを作る
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message': 'your data',
#             'form': HelloForm()
#         }
#     def get(self,request):
#         return render(request, 'hello/index.html', self.params)
#     def post(self,request):
#         msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'
#         self.params['message'] = msg
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## checkboxをクリックするとsuccessと表示する
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title' : 'hello',
#             'form' : HelloForm(),
#             'result' :  None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         if('check' in request.POST):
#             self.params['result'] = 'Checked!!'
#         else:
#             self.params['result'] = "Not Checked.."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## null も含めたcheck box
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         chk = request.POST['check']
#         self.params['result'] = "you checked " + chk + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## プルダウンメニューの作成(ラジオボタン、選択リストでも同じでできる)
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST['choice']
#         self.params['result'] = "you checked " + ch + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## 複数選択項目リスト
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':HelloForm(),
#             'result':None
#         }
#     def get(self,request):
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ch = request.POST.getlist('choice')
#         self.params['result'] = "you checked " + str(ch) + "."
#         self.params['form'] = HelloForm(request.POST)
#         return render(request,"hello/index.html",self.params)

## session 
# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             'title':'',
#             'form':SessionForm(),
#             'result':None
#         }
#     def get(self,request):
#         self.params['result'] = request.session.get('last_msg','No message')
#         return render(request,"hello/index.html",self.params)
#     def post(self,request):
#         ses = request.POST['session']
#         self.params['result'] = "send : '" + ses + "'."
#         request.session['last_msg'] = ses
#         self.params['form'] = SessionForm(request.POST)
#         self.params['s'] = request.session.keys()
#         return render(request,"hello/index.html",self.params)