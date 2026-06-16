from django.shortcuts import render

# Create your views here.
def profiles(request):
    """ A view to return the profiles page """
    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
