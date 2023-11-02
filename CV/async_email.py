from django.core.mail import EmailMessage

def send_mail(subject, message, from_email, recipient_list, atachments=None):
    email = EmailMessage(
        subject,
        message,
        from_email,
        recipient_list
    )
    
    if atachments:
        for attachment in atachments:
            email.attach_file(attachment)
    
    email.content_subtype = "html"
    email.send()