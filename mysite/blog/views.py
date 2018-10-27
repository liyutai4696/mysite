from django.shortcuts import render

# Create your views here.


def index(request):
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





