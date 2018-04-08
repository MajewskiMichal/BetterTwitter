from django.shortcuts import render
from django.views import View

# Create your views here.



class SchoolView(View):

    def get(self, request):

        return render(request, "MyTwitter/base.html")



