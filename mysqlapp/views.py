from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Person, Partner, Client, Worker, Contract

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class InfoView(TemplateView):
    template_name = "info_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["personas_count"] = len(Person.objects.all())
        context["partners_count"] = len(Partner.objects.all())
        context["clients_count"] = len(Client.objects.all())
        context["workers_count"] = len(Worker.objects.all())
        context["contracts_count"] = len(Contract.objects.all())
        return context



class pInfoView(ListView):
    template_name = "info.html"
    model = Person
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "person"
        return context
    

class paInfoView(ListView):
    template_name = "info.html"
    model = Partner
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "partner"
        return context
    

class clInfoView(ListView):
    template_name = "info.html"
    model = Client
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "client"
        return context
    

class coInfoView(ListView):
    template_name = "info.html"
    model = Contract
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "contract"
        return context


class wInfoView(ListView):
    template_name = "info.html"
    model = Worker
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "worker"
        return context



class pCreateView(CreateView):
    template_name = "create.html"
    model = Person

    fields = ["passport", "password", "username", "first_name", "last_name", "middle_name", "email", "birthdate", "phonenumber"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "person"
        return context
    
    def get_success_url(self):
        return reverse("personas_info")
    

class paCreateView(CreateView):
    template_name = "create.html"
    model = Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "partner"
        return context
    
    def get_success_url(self):
        return reverse("partners_info")
    

class clCreateView(CreateView):
    template_name = "create.html"
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "client"
        return context
    
    def get_success_url(self):
        return reverse("clients_info")
    

class coCreateView(CreateView):
    template_name = "create.html"
    model = Contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "contract"
        return context
    
    def get_success_url(self):
        return reverse("contracts_info")


class wCreateView(CreateView):
    template_name = "create.html"
    model = Worker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "worker"
        return context
    
    def get_success_url(self):
        return reverse("workers_info")
    


class pUpdateView(UpdateView):
    template_name = "update.html"
    model = Person

    fields = ["passport", "password", "username", "first_name", "last_name", "middle_name", "email", "birthdate", "phonenumber"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "person"
        return context
    
    def get_success_url(self):
        return reverse("personas_info")
    

class paUpdateView(UpdateView):
    template_name = "update.html"
    model = Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "partner"
        return context
    
    def get_success_url(self):
        return reverse("partners_info")
    

class clUpdateView(UpdateView):
    template_name = "update.html"
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "client"
        return context
    
    def get_success_url(self):
        return reverse("clients_info")
    

class coUpdateView(UpdateView):
    template_name = "update.html"
    model = Contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "contract"
        return context
    
    def get_success_url(self):
        return reverse("contracts_info")


class wUpdateView(UpdateView):
    template_name = "update.html"
    model = Worker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "worker"
        return context
    
    def get_success_url(self):
        return reverse("workers_info")
    


class pDeleteView(DeleteView):
    template_name = "delete.html"
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "person"
        return context
    
    def get_success_url(self):
        return reverse("personas_info")
    

class paDeleteView(DeleteView):
    template_name = "delete.html"
    model = Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "partner"
        return context
    
    def get_success_url(self):
        return reverse("partners_info")
    

class clDeleteView(DeleteView):
    template_name = "delete.html"
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "client"
        return context
    
    def get_success_url(self):
        return reverse("clients_info")
    

class coDeleteView(DeleteView):
    template_name = "delete.html"
    model = Contract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "contract"
        return context
    
    def get_success_url(self):
        return reverse("contracts_info")


class wDeleteView(DeleteView):
    template_name = "delete.html"
    model = Worker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = "worker"
        return context
    
    def get_success_url(self):
        return reverse("workers_info")