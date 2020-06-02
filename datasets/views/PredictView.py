# from django.views.generic.edit import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
# import expDjango.settings as settings
# from ..forms import PredictForm
# from django.contrib import messages
# from expDjango import config
# import os
#
# class PredictView(LoginRequiredMixin, FormView):
#
#     template_name = 'dataset/predict.html'
#     login_url = settings.LOGOUT_REDIRECT_URL
#     form_class = PredictForm.PredictForm
#
#     def delete_image(self, image_url):
#
#         '''
#         This function is used to delete temporary images that are saved (images > 2.5MB)
#         :param image_url: url of image
#         :return: bool --> if True delete works well, if False problems occured in process
#         '''
#
#         try:
#             if os.path.exists(image_url):
#                 os.remove(image_url) # os.remove doesn't have return, i.e. if it goes wrong it generates exception
#                 return True
#         except:
#             return False
#
#     def get_context_data(self, **kwargs):
#         context = super(PredictView, self).get_context_data(**kwargs)
#         return context
#
#     def form_valid(self, form):
#
#         try:
#
#             dataset_id = form.cleaned_data['dataset_dropdown']
#             model_id = form.cleaned_data['models_dropdown']
#             image = form.cleaned_data['image_upload']
#
#             url_image = None
#             if image.size > config.SIZE_GREATER_TEMPORARY: # if file is greater than 2.5MB, i need to store is url
#                 url_image = image.file.name
#
#             # process predict considering dataset and model --> i need to create a queryset that by model_id get's model file
#
#             # if file is temporary (saved in disk >2.5MB) --> i need to delete them, in order to avoid memory problems
#             if url_image is not None:
#                 safe_delete = self.delete_image(url_image)
#                 if safe_delete == False:
#                     raise
#
#             return
#         except:
#             storage = messages.get_messages(self.request)
#             storage.used = True
#             messages.add_message(self.request, messages.ERROR, config.ERROR_ON_PREDICT)
#
#     def form_invalid(self, form):
#
#         storage = messages.get_messages(self.request)
#         storage.used = True
#         messages.add_message(self.request, messages.ERROR, config.PLEASE_FILL_FORM_CORRECTLY)
#         return super(PredictView, self).form_invalid(form)
