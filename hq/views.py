from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from hq.models import Job

# Create your views here.

class HomeView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', self.context)


class AboutUsView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html', self.context)

    def post(self, request, *args, **kwargs):
        return render(request, 'job_listing.html', self.context)


class JobsView(ListView):
    model = Job
    template_name = 'job_listing.html'


class JobDetailView(View):
    context = {}
    def get(self, request, pk, *args, **kwargs):
        job = Job.objects.get(id=pk)
        self.context['job'] = job
        return render(request, 'job_details.html', self.context)

    def post(self, request, pk, *args, **kwargs):
        return render(request, 'contact.html', self.context)

class ContactPageView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', self.context)

    def post(self, request, *args, **kwargs):
        return render(request, 'contact.html', self.context)
