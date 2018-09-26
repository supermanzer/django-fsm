from django.db import models
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
    STATUS = (
      (1, 'Planned'),
      (2, 'Locked'),
      (3, 'Running'),
      (4, 'Complete'),
      (5, 'Error')
    )
    status = FSMIntegerField(verbose_name='Run Status', db_index=True, choices=STATUS, default=STATUS[0])
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)


    class Meta:
        app_label = 'factory'

    @transition(field=status, source='Planned', target='Locked')
    def lock(self):
      """
      Add side effects here, status will be updated when trigered.
      """
      return 'Widget Run Locked'

    @transition(field=status, source='Locked', target='Running')
    def run(self):
      return 'Widget Run in Process'

    @transition(field=status, source='Running', target='Complete')
    def complete(self):
      return 'Widget Run Completed'

    @transition(field=status, source='*', target='Error')
    def uh_oh(self):
      return 'Soemething went wrong'
