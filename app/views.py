from django.http import JsonResponse

def ola(request):
    return JsonResponse("Olá, bem vindo a minha API - UERN", safe=False)

def list_pizzas(request):
    pizzas = [
        {'id':1, 'name': 'Margherita', 'ingredientes': ['Tomate', 'Mussarela', 'Manjericão']},
        {'id':2, 'name': 'Pepperoni', 'ingredientes': ['Pepperoni', 'Mussarela', 'Tomate']},
        {'id':3, 'name': 'Vegetariana', 'ingredientes': ['Tomate', 'Mussarela', 'Cogumelos']},
        {'id':4, 'name': '3 Queijos', 'ingredientes': ['Catupiry', 'Mussarela', 'Parmesão']},
        {'id':5, 'name': 'Frango', 'ingredientes': ['Tomate', 'Mussarela', 'Frango']},
        {'id':6, 'name': 'Bacon', 'ingredientes': ['Tomate', 'Mussarela', 'Bacon', 'Azeitonas']},
        {'id':7, 'name': 'Portuguesa', 'ingredientes': ['Ovos', 'Mussarela', 'Presunto', 'Queijo']},
        {'id':8, 'name': 'Baiana', 'ingredientes': ['Tomate', 'Mussarela', 'Pimenta']},
        {'id':9, 'name': 'Calabresa', 'ingredientes': ['Tomate', 'Mussarela', 'Calabresa']},
        {'id':10, 'name': 'Atum', 'ingredientes': ['Tomate', 'Mussarela', 'Atum']},
    ]
    return JsonResponse(pizzas, safe=False)

