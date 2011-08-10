# This passes custom variables defined using signals to the template context

# Requires a function called get_analytics_dictionary
# which accepts a request and returns a dictionary with any set of the following keys
dict_keys = (1,2,3,4,5)
# (My function stores the dictionary in sessions, with this tuple as the key.)

# The integer keys should map to instances of the following objects
# key,value may be unicode strings of up to 64 characters
# scope can be 1: visitor-level 2: session-level 3: pageview-level
class ga_custom_variable:
    def __init__(self, key, value, scope):
        self.key = key
        self.value = value
        self.scope = int(scope)
# 'user_defined' should map to the unicode string of up to 64 characters
# Refer to google-analytics for more details

# This is our context processor
def google_async_variables(request):
    return {'ga_custom_variables': get_analytics_dictionary(request)}

def clean_analytics_dictionary(dictionary):
    copy = dictionary
    for key in copy.keys():
        if key not in dict_keys:
            del copy[key]
    return copy

def get_analytics_dictionary(request):
    if dict_keys in request.session:
        dictionary = request.session[dict_keys]
        del request.session[dict_keys]
        dictionary = clean_analytics_dictionary(dictionary)
        return dictionary
    else:
        return None
