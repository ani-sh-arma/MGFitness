from django.core.mail import send_mail
from django.conf import settings



def send_email_to_client(mail_subject , mail_message , recipients):
    subject = mail_subject
    message = mail_message
    from_email = settings.EMAIL_HOST_USER
    recipient_list = recipients

    send_mail(subject, message, from_email , recipient_list)