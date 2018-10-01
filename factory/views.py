from django.shortcuts import render
from django.views import generic, View
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
###### READ ONLY VIEWS ######
class WidgetRunList(JSONResponseMixin, generic.ListView):
    """
    A listing of our Widget maunufacturing runs.
    """
    model = models.WidgetRun
    template_name = 'factory/components/widgetrun_list.hmtl'
    context_object_name = 'runs'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class WidgetRunDetail(JSONResponseMixin, generic.DetailView):
    """
    A simple view to display a single widget run
    """
    model = models.WidgetRun
    template_name = 'factory/components/widgetrun_detail.html'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

###### WRITE VIEWS ######
class CreateWidgetRun(JSONResponseMixin, generic.CreateView):
    """
    A view to allow creating a new Widget manufacturing run.
    """
    model = models.WidgetRun
    context_object_name = 'run'
    form_class = forms.WidgetRunForm
    template_name = 'factory/components/widgetrun_create.html'

    def get_context_data(self, *args):
      context = super(EditWidgetRun,self).get_context_data(*args)
      context['title'] = 'Create Run'

      return context

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class EditWidgetRun(JSONResponseMixin, generic.UpdateView):
    """
    A CBV to allow for the editing of widget manufacturing runs.
    """
    model = models.WidgetRun
    context_object_name = 'run'
    form_class = forms.WidgetRunForm
    template_name = 'factory/components/widgetrun_create.html'

    def get_context_data(self, *args):
      context = super(EditWidgetRun,self).get_context_data(*args)
      context['title'] = 'Edit Run'

      return context


    def render_to_response(self, context, **response_kwargs):
        return self.render_to_response_json(context, **response_kwargs)

class DeleteWidgetRun(JSONResponseMixin, generic.DeleteView):
    """
    Allowing the deletion of widget runs
    """
    model = models.WidgetRun
    template_name = 'templates/confirm_delete.html'

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class ChangeRunStatus(JSONResponseMixin, generic.DetailView):
  """
  Using a custom CBV to handle the changing of our finite
  status field.
  """

  model = models.WidgetRun

  def post(self, request, **kwargs):
    """
    The method where we will check to see if we can apply the status change and, if we can, change it.
    """
