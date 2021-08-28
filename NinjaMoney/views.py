from django.shortcuts import render,redirect
from random import randint
from datetime import datetime
# Create your views here.
lista=[]
def index(request):
    if 'gold_cant' not in request.session:
        request.session['gold_cant'] = 0 #Se crea variable de session
        request.session['move'] = [] #Se crea variable de session de una lista
    return render(request,'index.html')

def process_money(request):
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S %p") #metodo tiempo strftime da formato a la fecha
    if "farm" in request.POST: #pregunta si el objeto viene en el request del formulario en su metodo POST
        ranfarm = randint(10,20) #valor aleatorio entre 10 y 20
        request.session['gold_cant'] += ranfarm
        request.session['move'].append([ranfarm,'farm',fecha])
    if "cave" in request.POST:
        rancave = randint(5,10) 
        request.session['gold_cant'] += rancave
        request.session['move'].append([rancave,'cave',fecha])
    if "house" in request.POST:
        ranhouse = randint(2,5)
        request.session['gold_cant'] += ranhouse
        request.session['move'].append([ranhouse,'house',fecha])
    if "casino" in request.POST:
        rancasino = randint(-50,50)
        request.session['gold_cant'] += randint(-50,50)
        request.session['gold_cant'] += rancasino
        request.session['move'].append([rancasino,'casino',fecha])

    return redirect('/')
