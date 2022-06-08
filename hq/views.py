from multiprocessing import context
from django.shortcuts import render
from django.views import View

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
        return render(request, 'about.html', self.context)


class JobsView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'job_listing.html', self.context)

    def post(self, request, *args, **kwargs):
        return render(request, 'job_listing.html', self.context)


class ContactPageView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', self.context)

    def post(self, request, *args, **kwargs):
        return render(request, 'contact.html', self.context)
