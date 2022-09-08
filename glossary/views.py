from django.shortcuts import render
from .models import Domain, Entry

def entries(request):

    domains = []

    for domain in Domain.objects.all():
        domains.append({
            'domain' : domain,
            'entries': get_domain_entries(domain)
        })

    return render(request, 'entries.html', {'domains': domains})

def entry(request, entry_id):
    context = {
        'entry': Entry.objects.get(id=entry_id)
    }
    return render(request, 'entry.html', context)

def get_domain_entries(domain):
    return Entry.objects.filter(domain=domain)