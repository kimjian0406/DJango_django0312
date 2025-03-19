from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user_email, verification_url):
    subject = '이메일 인증을 완료해주세요.'
    message = f'아래 링크를 클릭하여 이메일 인증을 완료해주세요:\n{verification_url}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [user_email])

