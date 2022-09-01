from django.shortcuts import render

entries = [
    {
        'title': 'ITG',
        'acronym': 'In Theatre GUI',
        'description': 'Graphical user interface for the in theatre bit that the surgeon sees for cydar which shows all the shmancy stuff'
    },
    {
        'title': 'Vault',
        'description': 'Bit that gets all the data and does stuff with it'
    },
]

# Create your views here.
def home(request):
    context = {
        'entries': entries
    }
    return render(request, 'table.html', context)

