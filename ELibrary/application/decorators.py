from django.http.response import HttpResponsePermanentRedirect


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return HttpResponsePermanentRedirect("/login/")

    return wrapper