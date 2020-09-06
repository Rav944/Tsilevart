from django.views.generic import TemplateView
from django.shortcuts import render
from Tsilevart.settings import OBTAINING_POINTS_METHODS
from .forms import CodeMethodForm


class PaymentMethodView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": OBTAINING_POINTS_METHODS})


class CodeMethodView(TemplateView):
    form_class = CodeMethodForm
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return render(request, self.template_name, {"form": OBTAINING_POINTS_METHODS})
