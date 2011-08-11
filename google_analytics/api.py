from google_analytics.context_processors import dict_keys, ga_custom_variable
    
def set_variable(request, slot, key, value, scope):
    """
    Call this function in a view to queue a custom variable for the response
    These are cleared after each pageview.
    If a variable slot has already been taken, KeyError will be raised

    In the future I will add support for keeping track of session and visitor-level variables.  For now, you will have to keep track of those on your own.

    """
    custom_variable = ga_custom_variable(key, value, scope)
    if dict_keys in request.session:
        dictionary = request.session[dict_keys]
    else:
        dictionary = {}
    if slot in dictionary:
        raise KeyError('A variable already exists in that slot')
    dictionary[slot] = custom_variable
    request.session[dict_keys] = dictionary
