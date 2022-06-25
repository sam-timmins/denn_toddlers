def site_contexts(request):
    """ Site variables """
    playgroup_name = 'Denn Toddlers'

    contexts = {
        'playgroup_name': playgroup_name,
    }

    return contexts
