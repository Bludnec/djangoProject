from django.shortcuts import redirect
from django.urls import reverse_lazy


def my_login_required(func):
    def decorated_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        next_url = reverse_lazy(request.resolver_match.view_name)
        redirect_url = reverse_lazy('authentication:login')
        try:
            return redirect("%s?next=%s" % (redirect_url, next_url))
        except Exception as e:
            try:
                return redirect("%s?next=%s" % (redirect_url, request.META['REQUEST_URI']))
            except Exception as e:
                return redirect(redirect_url)

    return decorated_function
