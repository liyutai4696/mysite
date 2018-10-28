from django.shortcuts import render

# Create your views here.


def index(request):
    x = request.META.get('HTTP_X_FORWARDED_FOR')
    ip =""
    if x:
        ip = x.split(',')[0]
        print("来自IP：",ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print("来自代理IP：",ip)
    c = {}
    c['szcj']="<p>博主努力ing...</p>"
    c['chsy']="博主努力ing..."
    c['ylxy']="博主努力ing..."
    c['yyml']="博主努力ing..."
    return render(request,'index.html',c)


def pp(request):
    return render(request,'pp.html')

def sgz(request):
    return render(request,'sgz.html')





