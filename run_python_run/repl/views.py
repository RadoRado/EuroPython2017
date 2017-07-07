from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from .forms import CodeRunForm
from .services import run_code
from .models import CodeRun


class ReplIndexView(LoginRequiredMixin, ListView):
    template_name = 'repl/index.html'
    queryset = CodeRun.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['code_run_form'] = CodeRunForm()

        return context


class ReplCodeRunResultView(LoginRequiredMixin, DetailView):
    model = CodeRun
    pk_url_kwarg = 'code_run_id'

    template_name = 'repl/code_run_detail.html'


class ReplCodeRunView(LoginRequiredMixin, View):
    def post(self, request):
        form = CodeRunForm(request.POST)

        if form.is_valid():
            code_run = run_code(**form.cleaned_data)

            return redirect('repl:code-run-detail', code_run_id=code_run.id)

        return redirect('repl:index')
