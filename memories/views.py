from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import MemoryPost
import re


# =========================================
# FEED PAGE
# =========================================

# name : riya, password : 1234
# saurya , password : 0987

def feed_page(request):

    posts = (
        MemoryPost.objects
        .select_related('user')
        .prefetch_related('likes')
        .order_by('-created_at')
    )

    return render(
        request,
        'feed.html',
        {'posts': posts}
    )


# =========================================
# REGISTER PAGE
# =========================================

def register_page(request):

    if request.method == 'POST':

        username = request.POST.get('username').strip()

        password = request.POST.get('password')

        # Username validation

        if len(username) < 3:

            messages.error(
                request,
                'Username must be at least 3 characters'
            )

            return redirect('register_page')


        # Existing username check

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect('register_page')
        
        # =========================================
        # PASSWORD VALIDATION
        # =========================================

        if len(password) < 8:

            messages.error(
                request,
                'Password must be at least 8 characters long.'
            )

            return redirect('register_page')

        if len(password) > 12:

            messages.error(
                request,
                'Password must not exceed 12 characters.'
            )

            return redirect('register_page')

        # Uppercase check

        if not re.search(r'[A-Z]', password):

            messages.error(
                request,
                'Password must contain at least one uppercase letter.'
            )

            return redirect('register_page')

        # Lowercase check
        if not re.search(r'[a-z]', password):

            messages.error(
                request,
                'Password must contain at least one lowercase letter.'
            )

            return redirect('register_page')

        # Number check

        if not re.search(r'[0-9]', password):

            messages.error(
                request,
                'Password must contain at least one number.'
            )

            return redirect('register_page')

        # Special character check

        if not re.search(r'[@$!%*#?&]', password):

            messages.error(
                request,
                'Password must contain at least one special character.'
            )

            return redirect('register_page')

        # Create user

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(
            request,
            'Registration successful'
        )

        return redirect('login_page')

    return render(
        request,
        'register.html'
    )


# =========================================
# LOGIN PAGE
# =========================================

def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('feed_page')

        messages.error(
            request,
            'Invalid username or password'
        )

    return render(
        request,
        'login.html'
    )


# =========================================
# LOGOUT
# =========================================

@login_required
def logout_page(request):

    logout(request)

    return redirect('login_page')


# =========================================
# CREATE POST
# =========================================

@login_required
def create_post_page(request):

    if request.method == 'POST':

        image = request.FILES.get('image')

        description = request.POST.get('description')

        if not image:

            messages.error(
                request,
                'Image is required'
            )

            return redirect('create_post_page')

        MemoryPost.objects.create(
            user=request.user,
            image=image,
            description=description
        )

        return redirect('feed_page')

    return render(
        request,
        'create_post.html'
    )


# =========================================
# LIKE POST
# =========================================

@login_required
def like_post(request, id):

    post = get_object_or_404(
        MemoryPost,
        id=id
    )

    if request.user in post.likes.all():

        post.likes.remove(request.user)

    else:

        post.likes.add(request.user)

    return redirect('feed_page')


# =========================================
# DELETE POST
# =========================================

@login_required
def delete_post(request, id):

    post = get_object_or_404(
        MemoryPost,
        id=id
    )

    if post.user == request.user:

        post.delete()

    else:

        messages.error(
            request,
            'You can delete only your own posts'
        )

    return redirect('feed_page')