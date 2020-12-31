from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def profile_not_exists(view_func):
    def wrapper_func(request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
