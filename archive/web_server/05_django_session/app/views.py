from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def set_session(request):
    username = request.POST.get('username')
    request.session['username'] = username
    request.session['point'] = 123456789
    request.session['prob'] = 0.123456
    request.session['expired'] = True
    request.session['nums'] = [1, 2, 3, 4, 5]
    request.session['data'] = {
        'message': 'Hello, Django Session',
        'today': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return redirect('app:index')

def modify_session(request):
    request.session['favorite_color'] = 'springgreen'
    request.session['nums'].append(999)
    request.session['data']['new_item'] = 'new_item'
    request.session.modified = True

    del request.session['point']

    return redirect('app:index')

def delete_session(request):
    request.session.flush()
    return redirect('app:index')

def set_cookie(request):
    name = request.POST.get('cookie_name')
    value = request.POST.get('cookie_value')

    response = redirect('app:index')
    response.set_cookie(
        name, value,
        path='/app/',
        max_age = 120,
        httponly=True,
        samesite='Lax',
        secure=False
    )

    return response

def delete_cookie(request):
    response = redirect('app:index')
    name = request.POST.get('cookit_name')
    response.delete_cookie(name, path='/app/')
    return response