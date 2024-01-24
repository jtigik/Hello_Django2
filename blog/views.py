from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('Blog 4!')
    
    return render(
        request, 
        'blog/index.html',
        {
            # 'text': 'Estamos no Blog',
            'title': ' Blog',
            'posts':posts
        }
    )

def post(request, post_id):
    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    return render(
        request, 
        'blog/post.html',
        {
            'title': 'Post',
            'post': found_post
        }
    )

def exemplo(request):
    print('Exemplo 4!')
    
    return render(
        request, 
        'blog/exemplo.html',
        {
            'text': 'Estamos no Exemplo',
            'title': ' Exemplo'
        }
    )
