from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
def api_note_list(request):
    if request.method == 'POST':
        new_note_data = request.data
        note = Note()
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.img = new_note_data['img']
        note.save()

    notes = Note.objects.all()
    serialized_notes = NoteSerializer(notes, many = True)
    return Response(serialized_notes.data)

@api_view(['GET', 'POST'])
def api_delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.delete()
    return Response()
    