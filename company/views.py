from django.shortcuts import render


def company_view(request, state):
    context = {
        'state': state
    }
    return render(request, 'company.html', context)


def intro(request):
    return company_view(request, 'intro')


def organization(request):
    return company_view(request, 'organization')


def history(request):
    return company_view(request, 'history')


def link(request):
    return company_view(request, 'link')
