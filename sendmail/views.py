from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

def index(request):
    """題名"""
    subject = "題名"
    """本文"""
    message = "本文です\nこんにちは。メールを送信しました。届いていますか？"
    """送信元メールアドレス"""
    from_email = "information@myproject"
    """宛先メールアドレス"""
    recipient_list = [
        "dsduoa31@gmail.com"
    ]

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('<h1>email send complete.</h1>')

class IndexView(generic.TemplateView):
    template_name = "sendmail/home.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name )
