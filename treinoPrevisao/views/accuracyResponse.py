from django.shortcuts import render
import ast


def showAccResponse(request, **kwargs):

    try:

        x = kwargs.get('arrayConf')
        kk = [int(k) for k in x]
        acc = kwargs.get('acc')
        prec = kwargs.get('prec')
        rec = kwargs.get('rec')
        f1 = kwargs.get('f1')

        return render(request, 'treinoPrevisao/showAccuracy.html', {'arrayConf' : x, 'acc' : acc,'prec' : prec, 'rec' : rec, 'f1' : f1})

    except:
        raise