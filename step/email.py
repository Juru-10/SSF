from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def marks_message(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to SSF'
    sender = 'rijuruas@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/marks.txt',{"name": name})
    html_content = render_to_string('email/marks.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def discipline_message(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to SSF'
    sender = 'rijuruas@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/discipline.txt',{"name": name})
    html_content = render_to_string('email/discipline.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
