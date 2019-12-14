from django.shortcuts import HttpResponse

def showAccResponse(request):

    try:

        #PARA JA APENAS UM RESPONSE
        return HttpResponse()

    except:
        raise