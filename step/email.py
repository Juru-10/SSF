from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import requests

def marks_message(name,receiver):
    print(name)
    # Creating message subject and sender
    # subject = 'Welcome to SSF'
    # sender = 'juruassumpta@zoho.com'
    print(requests.post(
        "https://api.mailgun.net/v3/sandbox3b2294b871f94f64a36ffc2fbfaeda8a.mailgun.org/messages",
        auth=("api", "12b331c378fdbdbb5e141eb368ae2200-e566273b-fd988a9e"),
        data={"from": "SSF <postmaster@sandbox3b2294b871f94f64a36ffc2fbfaeda8a.mailgun.org>",
              "to": receiver,
              "subject": "Hello Assumpta Uwanyirijuru",
              "text": "New Marks for "+name}))

    #passing in the context vairables
    # text_content = render_to_string('email/marks.txt',{"name": name})
    # html_content = render_to_string('email/marks.html',{"name": name})
    #
    # msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    # msg.attach_alternative(html_content,'text/html')
    # msg.send()

def discipline_message(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to SSF'
    sender = 'rijuruas@gmail.com'
    # requests.post(
    # "https://api.mailgun.net/v3/sandbox9930d3bfa0b44cf2973dac02dc9caab9.mailgun.org/messages",
    # auth=("api", "ed1c33b06c461035385a8b4de19f1c25-e566273b-3f0308f2"),
    # data={"from": "Mailgun Sandbox <postmaster@sandbox9930d3bfa0b44cf2973dac02dc9caab9.mailgun.org>",
    #       "to": receiver,
    #       "subject": "SSF marks notification for "+name,
    #       "text": "Mwareba imyitwarire y'umwana mukigo"})
    #passing in the context vairables
    # text_content = render_to_string('email/discipline.txt',{"name": name})
    # html_content = render_to_string('email/discipline.html',{"name": name})
    #
    # msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    # msg.attach_alternative(html_content,'text/html')
    # msg.send()
