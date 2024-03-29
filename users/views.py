from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from catalog.models import BookInstance


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ProfileView(View):
    def get(self, request):
        book_copy = BookInstance.objects.filter(borrower=self.request.user)
        return render(request, 'profile.html', {'book_copy': book_copy})
