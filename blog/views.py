from django.shortcuts import render

# Create your views here.

def blog(request):
    print('Blog 4!')
    
    return render(
        request, 
        'blog/index.html',
        {
            'text': 'Estamos no Blog',
            'title': ' Blog'
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
