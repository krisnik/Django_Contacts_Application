from django.shortcuts import render

# Create your views here.

from .models import Contact
from django.template import loader
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    contacts_list = Contact.objects.all()

    template = loader.get_template('contacts/index.html')
    context = {
        'contacts_list': contacts_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    phone = request.POST['phone']

    contact = Contact.objects.create(first_name=first_name, last_name=last_name, phone=phone)

    contact.save()

    print "Created a  contact with id ", contact.id
    return HttpResponseRedirect(reverse('contacts:index'))
    pass

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    print "in update contact is ",contact

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    phone = request.POST['phone']

    contact.first_name = first_name
    contact.last_name = last_name
    contact.phone = phone

    contact.save()
    print "Updated the contact for id ",contact_id
    return HttpResponseRedirect(reverse('contacts:index'))
    pass

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    contact.delete()

    print "Deleted the contact for id ", contact_id
    return HttpResponseRedirect(reverse('contacts:index'))
    pass

def read(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    print "contact in read ",contact
    template = loader.get_template('contacts/details.html')
    context = {
        'contact': contact,
    }
    return HttpResponse(template.render(context, request))
    pass

