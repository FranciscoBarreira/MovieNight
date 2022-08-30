from django.shortcuts import render

# Create your views here.


def view_contacts_page(request):
    """ A view to return the contacts page """

    return render(request, 'contacts/contacts.html')