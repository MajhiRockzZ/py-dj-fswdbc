from django.shortcuts import render
from django.views.generic import View, TemplateView
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class based views are cool.")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context


""" 
*args -> Will give all function parameters as a tuple.

**kwargs -> Will give all keyword arguments except for those 
            corresponding parameter as a dictionary.
 """
