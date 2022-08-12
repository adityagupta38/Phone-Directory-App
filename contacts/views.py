from django.shortcuts import render
from contacts.models import Contacts
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from contacts.forms import ContactsForm
# Create your views here.


class Home(ListView):
    model = Contacts


class ContactDetail(DetailView):
    model = Contacts


class CreateContact(CreateView):
    model = Contacts
    fields = '__all__'
    success_url = '/'


class UpdateContact(UpdateView):
    model = Contacts
    fields = '__all__'
    success_url = '/'


class DeleteContact(DeleteView):
    model = Contacts
    success_url = '/'


def addcontact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        title = 'Add Contact'
        if form.is_valid():
            form.save()
            form = ContactsForm()
            msg = 'Contact Added Successfully'
        else:
            form = ContactsForm()
            msg = 'Contact Name already exist  Pls Go to Update Contact '
        return render(request, 'add_update_contacts.html', {'form': form, 'msg': msg, 'title': title})
    else:
        form = ContactsForm()
        title = 'Add Contact'
        return render(request, 'add_update_contacts.html', {'form': form, 'title': title})


def updatepage(request):
    title = 'Update Contact By Name'
    return render(request, 'updatebyname.html', {'title': title})


def updateexistcont(request):
    title = 'Update Contact By Name'
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        conins = Contacts.objects.get(id=id)
        form = ContactsForm(request.POST, instance=conins)
        if form.is_valid():
            form.save()
            msg = 'Conatact Updated Successfully'
            return render(request, 'updatebyname.html', {'msg': msg, 'title': title})
        else:
            title = 'Update Contact By Name'
            msg = 'Conatact Already Exist With The Same Name Try Diff Name'
            conid = conins.id
            return render(request, 'add_update_contacts.html', {'form': form, 'title': title, 'msg': msg, 'conid': conid})
    else:
        name = request.GET['cname'].strip()
        '''''
        conli = Contacts.objects.all()
        for con in conli:
            if name == con.name:
                conins = Contacts.objects.get(name=name)
                form = ContactsForm(instance=conins)
                conid = conins.id
                return render(request, 'add_update_contacts.html', {'form': form, 'title': title, 'conid': conid})
        else:
            msg = 'Contact Does Not Exist'
            return render(request, 'updatebyname.html', {'msg': msg, 'title': title})
        '''
        try:
            conins = Contacts.objects.get(name=name)
            form =ContactsForm(instance=conins)
            conid = conins.id
            return render(request, 'add_update_contacts.html', {'form': form, 'title': title, 'conid': conid})
        except:
            msg = f'Contacts Does Not Exist or pls check ({name}) name is case sensitive'
            return render(request, 'updatebyname.html', {'msg': msg, 'title': title})

def delpage(request):
    title = 'Delete Contact By Name'
    return render(request, 'delbyname.html', {'title': title})


def delcontact(request):
    if request.method == 'POST':
        title = 'Delete Contact By Name'
        name = request.POST['cname'].rstrip()
        try:
            name = Contacts.objects.get(name=name)
            name.delete()
            msg = 'Contact Deleted Successfully'
            return render(request, 'delbyname.html', {'title': title, 'msg': msg})
        except Contacts.DoesNotExist:
            msg = 'Contact Does Not Exist'
            return render(request, 'delbyname.html', {'title': title, 'msg': msg})


def searchpage(request):
    title = 'Search Contact By Name'
    return render(request, 'searchbyname.html', {'title': title})


def searchbyname(request):
    name = request.GET['cname'].rstrip()
    try:
        coninst = Contacts.objects.get(name=name)
        msg = ''
    except Contacts.DoesNotExist:
        title = 'Search Contact By Name'
        msg = 'Contact Does Not Exist'
        return render(request, 'searchbyname.html', {'title': title, 'msg': msg})
    return render(request, 'contacts/contacts_detail.html', {'object': coninst, 'msg': msg})
