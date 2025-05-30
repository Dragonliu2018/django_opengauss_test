from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Company

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        
        Company.objects.create(
            id=id,
            name=name,
            age=age,
            address=address,
            salary=salary
        )
        messages.success(request, '职工信息添加成功！')
        return redirect('company_list')
    return render(request, 'company_form.html')

def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.id = request.POST.get('id')
        company.name = request.POST.get('name')
        company.age = request.POST.get('age')
        company.address = request.POST.get('address')
        company.salary = request.POST.get('salary')
        company.save()
        messages.success(request, '职工信息更新成功！')
        return redirect('company_list')
    return render(request, 'company_form.html', {'company': company})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        messages.success(request, '职工信息删除成功！')
        return redirect('company_list')
    return render(request, 'company_confirm_delete.html', {'company': company}) 