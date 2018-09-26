from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from factory import models
from factory import forms

from mixins.json_response import JSONResponseMixin

#------------------ WIDGET VIEWS -----------------------
class IndexView(generic.TemplateView):
    """
    Our basic index view.
    """
    template_name = 'factory/index.html'

    def get_context_data(self, *args):
        """
        adding some extra context to our index view
        """
        context = super(IndexView, self).get_context_data(*args)
        context['title'] = 'Manufacturing FSM'

        return context

class CreateWidget(JSONResponseMixin, generic.CreateView):
    """
    Basic view for creating new Widget instances
    """
    model = models.Widget
    form_class = forms.WidgetForm
    template_name = 'factory/components/widget_create.html'
    success_url = reverse_lazy('factory:widget-list')

    def get_context_data(self, *args):
      context = super(CreateWidget, self).get_context_data(*args)
      context['form_title'] = 'Create Widget'

      return context

    def render_to_response(self, context, **response_kwargs):
      return self.render_to_response_json(context, **response_kwargs)

class EditWidget(JSONResponseMixin, generic.UpdateView):
    """
    A basic view for editing widgent instances
    """
    model = models.Widget
    form_class = forms.WidgetForm
    template_name = 'factory/components/widget_create.html'
    success_url = reverse_lazy('factory:widget-list')

    def get_context_data(self, *args):
      context = super(CreateWidget, self).get_context_data(*args)
      context['form_title'] = 'Edit Widget'

      return context


    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class DeleteWidget(JSONResponseMixin, generic.DeleteView):
    """
    A CBV for deleting widget instances
    """
    model = models.Widget
    template_name = 'templates/confirm_delete.html'
    success_url = reverse_lazy('factory:widget-list')

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class ListWidgets(JSONResponseMixin, generic.ListView):
    """
    A simple list of existing Widget instances
    """
    model = models.Widget
    template_name = 'factory/components/widget_list.html'
    context_object_name = 'widgets'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

#------------------- WIDGET RUN VIEWS --------------------
class WidgetRunList(JSONResponseMixin, generic.ListView):
    """
    A listing of our Widget maunufacturing runs.
    """
    model = models.WidgetRun
    template_name = 'factory/components/widgetrun_list.hmtl'
    context_object_name = 'runs'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class CreateWidgetRun(JSONResponseMixin, generic.CreateView):
    """
    A view to allow creating a new Widget manufacturing run.
    """
    model = models.WidgetRun
    context_object_name = 'run'
    form_class = forms.WidgetRunForm
    template_name = 'factory/components/widgetrun_create.html'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)
