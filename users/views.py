from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER



class RegisterView(CreateView):
    template_name = 'users/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        self.send_wellcome_email(user.email)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_wellcome_email(self, user_email):
        subject = 'Добро пожаловать в наш интернет магазин'
        message = 'Спасибо, что зарегистрировались в нашем интернет магазине!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
