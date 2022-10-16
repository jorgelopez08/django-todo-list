from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Models
from .models import Notes
from .forms import NotesForm


def index(request):
    # Todo: change user.id for JWT
    sess = request.session.get('auth_user')
    if not sess:
        return redirect('/login')
    user = User.objects.get(id=sess)

    if request.method == 'POST':

        form = NotesForm(request.POST)
        if form.is_valid():
            new_note = Notes()
            new_note.user_id = user
            new_note.details = form.cleaned_data['details']
            new_note.save()
            print(new_note.details)

    del user.password
    notes = Notes.objects.filter(user_id=user)
    return render(request, 'index.html', {'notes': notes, 'user': user})


def delete(request, note_id):
    sess = int(request.session.get('auth_user'))
    if not sess:
        return redirect('/login')

    note = Notes.objects.get(id=note_id)
    if note.user_id.id == sess:
        note.delete()
    return redirect('/')
