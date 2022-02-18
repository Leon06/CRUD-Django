
from .models import Page

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import PageForm

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    """    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #Es lo mismo que tener : staff_member_required|||
        #if not request.user.is_staff:
            #return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

# ListView
class PageListView(ListView):
    model = Page

#DetailView
class PageDetailView(DetailView):
    model = Page

#CreateView
@method_decorator(staff_member_required,name="dispatch")
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


#UpdateView
class PageUpdate(StaffRequiredMixin,UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'

#DeleteView    
class PageDelete(StaffRequiredMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')