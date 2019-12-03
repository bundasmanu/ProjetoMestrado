from . import Train, Preview
import expDjango.TreinoPrevisao.Forms.trainPredForm as tpForm
import expDjango.utils as ut
from django.shortcuts import render_to_response,render

def uploadTrainPredict(request):

    try:

        if request.method == 'POST': #IF FORM HAS BEEN SUBMITTED

            #GET MY FORM WITH PARAMETERS THAT I NEED TO PREVIEW AND PREDICT
            upload = tpForm.TrainPredForm(request.POST, request.FILES) #DATA SHOULD BE SEND VIA HTTP POST, MORE SECURE

            #IF ALL DATA IS VALID --> TRAIN AND PREDICT
            if upload.is_valid():

                #GET ALL DATA
                gammaValue = upload.cleanedData.get(ut.getVarName(tpForm.TrainPredForm.gammaValue))
                dropdDownSelectedValue = upload.cleaned_data.get(ut.getVarName(tpForm.TrainPredForm.dropDownDatasets))

                #CALL PREVIEW (PREVIEW INSIDE CALLS TRAIN)
                accuracyResult = Preview.preview(gammaValue=gammaValue, dropdownValue=dropdDownSelectedValue)

                #RENDER TO RESPONSE--> SEND DATA TO NEW TEMPLATE
                return render(request, 'showAccuracy.html', {'accValue' : accuracyResult})

        else:
            #REDIRECT TO SAME PAGE WITH UPGRADED FORM
            form = tpForm.TrainPredForm()
            return render(request,'trainPreview.html', {'form' : form}) #ALTERAR DPS O NOME DA FORM
    except:
        raise

