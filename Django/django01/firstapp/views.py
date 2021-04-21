from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'greeting' : 'Hello!', 'content': 'Count letters.'}
    return render(request, 'index.html', context)

def result(request):
    if request.method == 'POST':
        countcontent = request.POST['countcontent']
        context = {
          'countcontent': countcontent, 
          'count': len(countcontent), 
          'countwithoutspace': len(countcontent.replace(' ', ''))
          }
    return render(request, 'resultpage.html', context)