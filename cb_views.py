# users/cb_views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from .models import CustomUser
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.signing import TimestampSigner

class SignupView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:signup_done')

    def form_valid(self, form):
        user = form.save()
        self.send_email_verification(user)
        return super().form_valid(form)

    def send_email_verification(self, user):
        signer = TimestampSigner()
        token = signer.sign(user.email)
        verification_url = self.request.build_absolute_uri(f'/verify/{token}/')
        send_mail(
            'Email Verification',
            f'Please verify your email by clicking the link: {verification_url}',
            settings.EMAIL['HOST_USER'],
            [user.email]
        )

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('todo_list')
from django.shortcuts import render, redirect
from django.core.signing import TimestampSigner, BadSignature
from .models import CustomUser

def verify_email(request, token):
    signer = TimestampSigner()
    try:
        email = signer.unsign(token, max_age=86400)  # 1일 이내에만 유효
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        return render(request, 'users/verify_success.html')
    except BadSignature:
        return render(request, 'users/verify_failed.html')
ø
ø

