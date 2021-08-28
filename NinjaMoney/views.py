from django.shortcuts import render,redirect
from random import randint
# Create your views here.
def index(request):
    if 'gold_cant' not in request.session:
        request.session['gold_cant'] = 0 #Se crea variable de session
    return render(request,'index.html')

def process_money(request):
    if "farm" in request.POST: #pregunta si el objeto viene en el request del formulario en su metodo POST
        ranfarm = randint(10,20) #valor aleatorio entre 10 y 20
        request.session['gold_cant'] += ranfarm
    if "cave" in request.POST:
        rancave = randint(5,10) 
        request.session['gold_cant'] += rancave
    if "house" in request.POST:
        ranhouse = randint(2,5)
        request.session['gold_cant'] += ranhouse
    if "casino" in request.POST:
        request.session['gold_cant'] += randint(-50,50)

    return redirect('/')
