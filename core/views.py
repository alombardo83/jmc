import os

from django.shortcuts import render, redirect
from django.http import FileResponse
from django.views import generic
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


class HomePageView(generic.TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hide_sidebar'] = True
        return context


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Demande du site Web"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_CONTACT_TO])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")

    form = ContactForm()
    return render(request, "core/contact.html", {'form': form})


def media_access(request, path):
    access_granted = False
    user = request.user
    if path.startswith('public/') or path.startswith('photologue/') or user.is_staff:
        access_granted = True

    if access_granted:
        path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(path):
            return FileResponse(open(path, 'rb'))
        else:
            return handler404(request)
    else:
        return handler403(request)


def handler404(request, *args, **argv):
    response = render(request, 'core/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'core/500.html')
    response.status_code = 500
    return response


def handler403(request, *args, **argv):
    response = render(request, 'core/403.html')
    response.status_code = 403
    return response
