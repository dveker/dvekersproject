from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .serializer import MemberSerializer

def crudapps(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myhtml.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def ids(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('id.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


class idsApi(generics.ListAPIView):
  queryset = Member.objects.all()
  serializer_class = MemberSerializer 