from django.shortcuts import render

# Create your views here.

def blog(request):
    print('Blog 4!')
    
    return render(
        request, 
        'blog.html'
    )


def exemplo(request):
    print('Exemplo 4!')
    
    return render(
        request, 
        'exemplo.html'
    )
