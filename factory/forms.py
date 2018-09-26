"""
factory/forms.py
--------------------------------------------------------------
Defining our form classes for the factory application.
"""

from django import forms

from factory import models

class WidgetForm(forms.ModelForm):
  class Meta:
    model = models.Widget
    fields = ['widget_number', 'type', 'description']

class WidgetRunForm(forms.ModelForm):
  class Meta:
    model = models.WidgetRun
    fields = ['widget', 'status']
