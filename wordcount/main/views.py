from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    rowText = request.GET['fulltext']
    words = rowText.split()
    wordDic = {}

    for word in words:
        if word in wordDic:
            #increase
            wordDic[word] += 1
        else:
            #add to dict
            wordDic[word] = 1
    
    return render(request, 'result.html', {'rowText': rowText, 'total' : len(words), 'dict' : wordDic.items()})