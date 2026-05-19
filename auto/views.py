from django.views import generic
from . import models

class AutoListView(generic.ListView):
    template_name = 'cars.html'
    context_object_name = 'cars'
    model = models.Car

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')