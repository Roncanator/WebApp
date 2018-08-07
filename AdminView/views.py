from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
# Create your views here.
from .models import LabSlot


def index(request):
    lab_list = LabSlot.objects.order_by('-lab_name')[:5]
    template = loader.get_template('AdminView/index.html')
    context = {
        'lab_list': lab_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, labslot_id):
    lab = get_object_or_404(LabSlot, pk=labslot_id)
    return render(request, 'AdminView/detail.html', {'lab': lab})