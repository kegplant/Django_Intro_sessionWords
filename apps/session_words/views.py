from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# the index function is called when root is visited
def index(request):
    try:
        request.session['words']
    except:
        request.session['words']=[]

    context={
        'words':request.session['words']
    }
    #return HttpResponse(response)
    return render(request,'session_words/index.html',context)
def process(request):
    try:
        request.session['words']
    except:
        request.session['words']=[]

    if request.method=='POST':    
        try:
            request.POST['isBig']
            weight='bold'
        except:
            weight='normal'
        newWord={
            'word':request.POST['word'],
            'color':request.POST['color'],
            'weight':weight,
            'date':datetime.now().strftime('%H:%M:%S%p, %b %d %Y')
        }
        request.session['words'].append(newWord)
        request.session.modified = True

    return redirect('/')
def clear(request):
    del request.session['words']
    #return HttpResponse(response)
    return redirect('/')