from django.shortcuts import render,get_object_or_404,redirect
from .models import UrlTable
from datetime import datetime
import hashlib
from redis import Redis


redis = Redis(host='redis', port=6379)

def home(request):
    if request.method == 'POST':
        h=hashlib.sha512(request.POST.get("url","").encode('utf-8')).hexdigest()
        long_url=request.POST.get("url","")
        short_url=None
        for i in range(0,120):
            try:
                t=UrlTable.objects.get(short_url=h[i:i+7])
                if t==request.POST.get("url",""):
                    short_url='www.tinyurls.me/'+h[i:i+7]
                    break
                else:
                    continue
            except:
                UrlTable.objects.create(short_url=h[i:i+7],long_url=request.POST.get("url",""))
                short_url='www.tinyurls.me/'+h[i:i+7]
                break
        return render(request,'home.html',{'long_url': long_url,'short_url': short_url})
    else:
        return render(request,'home.html',{'long_url': '','short_url': ''})



def redirectfun(request,p):
    if redis.exists(p):
       return redirect(redis.get(p))
    url=get_object_or_404(UrlTable,short_url=p)
    redis.setex(p,url.long_url,86400)
    return redirect(url.long_url)


