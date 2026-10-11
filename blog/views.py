from django.shortcuts import render

def index(request):
    content = {
        'post': [
            {'title': 'Post 1'},
            {'title': 'Post 2'},
            {'title': 'Post 3'},
        ]
    }
    return render(request, 'blog/index.html', content)
