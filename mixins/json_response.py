"""
mixins/json_response.py
-----------------------------------------------------
This file defines very simplistic JSON Response mixin.
It's allows us to be a bit more DRY in our Class Based View
development.
"""
from django.http import JsonResponse
from django.template.loader import render_to_string


class JSONResponseMixin(object):
  """
  A mixin used to return a rendered template as a JSON
  response.  Responses will include an html, is_valid, and/or
  err_msg attributes.
  """

  def render_to_response_json(self, context, **response_kwargs):
      """
      This function returns the dictionary generated by the
      get_data method as a JSON response.  This is called in
      Class Based Views to override default behavior.
      """
      return JsonResponse(
        self.get_data(context, **response_kwargs)
      )

  def get_data(self, context):
      """
      This function does most of the work translating a CBV
      request into something that can be serialized into JSON.
      """
      template_name = self.template_name
      resp = {'is_valid': False}
      try:
        resp['html'] = render_to_string(template_name, context, self.request)
        resp['is_valid'] = True
      except Exception as e:
        resp['err_msg'] = str(e)

      return resp