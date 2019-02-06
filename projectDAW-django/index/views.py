from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.conf import settings

# Create your views here.


def index(request):
	return render(
		request,
		'index.html'
		)

def contact(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('nombre', '')
			contact_email = request.POST.get('correo', '')
			form_subject = request.POST.get('asunto', '')
			form_content = request.POST.get('mensaje', '')
			template = get_template('contact_template.txt')
			context = {
				'nombre': contact_name,
				'correo': contact_email,
				'asunto': form_subject,
				'mensaje': form_content,
			}
			
			content = template.render(context)
			email = EmailMessage(form_subject, content, from_email=contact_email, to=[settings.EMAIL_HOST_USER])
			email.send()
			return redirect('contact')
	return render(request, 'contact.html', {
		'form': form_class,
	})

def about(request):
	return render(
		request,
		'about.html'
		)

def galeria(request):
	return render(
		request,
		'galeria.html'
		)