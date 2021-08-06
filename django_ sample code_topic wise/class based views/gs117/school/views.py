from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class ojasRedirectView(RedirectView):
 url = 'https://www.ojas-it.com/'


class newRedirectView(RedirectView):
 pattern_name = 'mindex'
 permanent = True


 def get_redirect_url(self, *args, **kwargs):
  print(kwargs)
  kwargs['pk'] = 16
  return super().get_redirect_url(*args, **kwargs)
