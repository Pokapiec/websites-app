from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Website, WebsiteCategory

class WebsiteListView(ListView):
    paginate_by = 25
    model = Website
    template_name = 'website_list.html'
    context_object_name = 'websites'

    def get_queryset(self):
        filter_val = self.request.GET.get('category', None)
        
        order = self.request.GET.get('orderby', 'date_added')
        if filter_val:
            category = WebsiteCategory.objects.get(name=filter_val)
            new_context = Website.objects.filter(
                category=category,
            ).order_by(order)
            return new_context

        new_context = Website.objects.all().order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = WebsiteCategory.objects.values_list('name', flat=True)
        context['categories'] = categories
        return context


class WebsiteDetailView(DetailView):
    model = Website
    template_name = 'website_detail.html'
    context_object_name = 'website'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
