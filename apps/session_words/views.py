from django.shortcuts import render, HttpResponse, redirect
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
        newWord={}
        request.session['words'].append(request.POST)
        request.session.modified = True

    return redirect('/')
def clear(request):
    del request.session['words']
    #return HttpResponse(response)
    return redirect('/')