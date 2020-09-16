#input id: 'notes'
from browser import document

def show_text(e):
    document['output'].textContent = e.target.value;

document['notes'].bind('input', show_text)