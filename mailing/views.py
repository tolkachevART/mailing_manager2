from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


class HomePageListView(ListView):
    model = Mailing
    template_name = 'mailing/base.html'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mailing
    permission_required = 'mailing.change_mailing'
    success_url = reverse_lazy('mailing:mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageListView(ListView):
    model = Message
    template_name = 'message/message_list.html'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message/message_detail.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:create')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
