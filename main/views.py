from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail
from smtplib import SMTPException

from main.models import Project, ResearchPaper, Team, Gallery
from blog.models import Article
from main.forms import ContactForm
from blog.views import ArticleListView

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['articles'] = Article.objects.all()
        context['teams'] = Team.objects.all()
        context['projects'] = Project.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class PaperListView(ListView):
    model = ResearchPaper


class TeamListView(ListView):
    model = Team

def contact(request):
    form = ContactForm()
    if form.is_valid():
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        recipient_list = ['thedscku@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            return response('Email sent successfully')
        except SMTPException as e:
            return response('There was an error sending an email: ', e) 
    
    return render(request, 'contact.html', {'form': form})


class GalleryListView(ListView):
    model = Gallery
    paginate_by = 12  # if pagination is desired
