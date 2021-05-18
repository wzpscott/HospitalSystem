from django.shortcuts import render
from django.shortcuts import redirect


def root(request):
    return redirect('./Hospital')


def index(request):
    '''if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index/')'''
    return render(request, 'Hospital/index.html')
