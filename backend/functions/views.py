from django.shortcuts import render, get_object_or_404
from .models import Function
from .forms import FunctionForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def save_function_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            functions = Function.objects.all()
            data['html_function_list'] = render_to_string('functions/includes/partial_function_list.html', {
                'functions': functions
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def function_list(request):
    functions = Function.objects.all()
    return render(request, 'functions/function_list.html', {'functions': functions})


def function_create(request):
    if request.method == 'POST':
        form = FunctionForm(request.POST)
    else:
        form = FunctionForm()
    return save_function_form(request, form, 'functions/includes/partial_function_create.html')


def function_update(request, pk):
    function = get_object_or_404(Function, pk=pk)
    if request.method == 'POST':
        form = FunctionForm(request.POST, instance=function)
    else:
        form = FunctionForm(instance=function)
    return save_function_form(request, form, 'functions/includes/partial_function_update.html')


def function_delete(request, pk):
    function = get_object_or_404(Function, pk=pk)
    data = dict()
    if request.method == 'POST':
        function.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        functions = Function.objects.all()
        data['html_function_list'] = render_to_string('functions/includes/partial_function_list.html', {
            'functions': functions
        })
    else:
        context = {'function': function}
        data['html_form'] = render_to_string('functions/includes/partial_function_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
