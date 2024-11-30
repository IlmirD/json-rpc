from django.shortcuts import render
from django.views.generic import TemplateView

import os

from . request import rpc_request

from mysite.settings import cert, key

class MainView(TemplateView):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):

        # создаем файлы, если не существуют

        if not os.path.isfile("client.crt"):
            with open("client.crt", "w") as file:
                file.write(cert)
        
        if not os.path.isfile("client.key"):
            with open("client.key", "w") as file: 
                file.write(key)

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        method = request.POST.get('method')
        params = request.POST.get('params')

        result = rpc_request(method, params)

        context = {"result": result}

        return render(request, self.template_name, context)

    
