from django.shortcuts import render
from django.shortcuts import redirect


def root(request):
    return redirect('./index')


def index(request):
    if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index/')
    return render(request, 'index/index.html')
