from django.shortcuts import render

def index(request):

    def waktu():
        import time
        a = time.localtime()
        hr = a.tm_hour
        mn = a.tm_min
        sc = a.tm_sec
        return ('{}:{}:{}'.format(hr,mn,sc))
    
    context = {
        'judul':'Home Page',
        'content':'Ini adalah halaman home website ini',
        'jam':waktu()
    }
    return render(request, 'index.html',context)