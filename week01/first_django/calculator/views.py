from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def check_for_param(f):
    def accepter(*params, **kwargs):
        # import ipdb; ipdb.set_trace()
        param = params[0].GET.get('format', '')
        return f(*params, forma=param, **kwargs)
    return accepter

@check_for_param
def add(request, a, b, forma=''):
    a = int(a)
    b = int(b)
    if forma.lower() == 'json':
        return JsonResponse({
            'result': a + b
        })
    return HttpResponse(a + b)

@check_for_param
def multiply(request, a, b, forma=''):
    a = int(a)
    b = int(b)
    if forma.lower() == 'json':
        return JsonResponse({
            'result': a * b
        })
    return HttpResponse(a * b)

@check_for_param
def power(request, a, b, forma=''):
    a = int(a)
    b = int(b)
    if forma.lower() == 'json':
        return JsonResponse({
            'result': a ** b
        })
    return HttpResponse(a ** b)

@check_for_param
def call_fact(request, a, forma=''):
    a = int(a)
    if forma.lower() == 'json':
        return JsonResponse({
            'result': fact(a)
        })
    return HttpResponse(fact(a))

def fact(a):
    a = int(a)
    if a == 0:
        return 1
    elif a == 1:
        return 1
    return fact(int(a)-1)*int(a)
