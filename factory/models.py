from django.db import models
from django.urls import reverse_lazy

from django_fsm import transition, FSMIntegerField


# Create your models here.
class Widget(models.Model):

    """
    A simple class that defines the widgets that are manufactured by the factory.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Widget_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='Widget_modified')
    widget_number = models.CharField(max_length=10, help_text='The unqiue identifier for this particular widget.')
    WIDGET_TYPES = (
      ('th', 'Thingy'),
      ('dl', 'Dealy'),
      ('fl', 'Flubber')
    )
    type = models.CharField(max_length=2, null=True, choices=WIDGET_TYPES, blank=True, help_text='The type of widget this is.')
    description = models.CharField(max_length=200, null=True, blank=True, help_text='A description of this widget')

    def __str__(self):
      return self.widget_number + ' - ' + self.description

    def get_delete_url(self):
      return reverse_lazy('factory:delete-widget', pk=self.id)

    class Meta:
        app_label = 'factory'

class WidgetRun(models.Model):
    """
    This model represents individual runs of widgets being
    manufactured.  This is the model where finite states will
    be employed.
    """
    date_created = models.DateTimeField(auto_now_add=True, help_text='date record created.')
    date_modified = models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')
    created_by = models.ForeignKey('auth.User', help_text='user who created record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='WidgetRun_created')
    modified_by=models.ForeignKey('auth.User', help_text='user who most recently modified record.', null=True, blank=True, on_delete=models.SET_NULL, related_name='WidgetRun_modified')
    PLANNED = 1
    LOCKED = 2
    RUNNING = 3
    COMPLETED = 4
    ERROR = 5
    STATUS = (
      (PLANNED, 'Planned'),
      (LOCKED, 'Locked'),
      (RUNNING, 'Running'),
      (COMPLETED, 'Complete'),
      (ERROR, 'Error')
    )
    status = FSMIntegerField(verbose_name='Run Status', db_index=True, choices=STATUS, default=STATUS[0][0])
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)


    class Meta:
        app_label = 'factory'

    def get_delete_url(self):
      return reverse_lazy('factory:delete-widgetrun', pk=self.id)

    @transition(field=status, source=PLANNED, target=LOCKED)
    def lock(self):
      """
      Add side effects here, status will be updated when trigered.
      """
      return 'Widget Run Locked'

    @transition(field=status, source=LOCKED, target=RUNNING)
    def run(self):
      return 'Widget Run in Process'

    @transition(field=status, source=RUNNING, target=COMPLETED)
    def complete(self):
      return 'Widget Run Completed'

    @transition(field=status, source='*', target=ERROR)
    def uh_oh(self):
      return 'Soemething went wrong'
