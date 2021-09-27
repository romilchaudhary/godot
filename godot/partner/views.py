from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import PartnerForm, MemberForm
from .models import Partner, Member
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    partners = Partner.partner_obj.all()
    context = {'partners_list': partners}
    return render(request, 'partner/index.html', context)


@login_required
def add_edit_partner(request, pk=None):
    """
    Add/Edit Partner details in this form
    :param request:
    :return: partner form
    """
    if pk:
        partner = get_object_or_404(Partner, pk=pk)
    else:
        partner = Partner()
    context = {}
    if 'partner/add_new_partner' in request.path:
        context['add'] = 'Add Partner'
    else:
        context['add'] = 'Edit Partner'
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.save()
            if 'partner/add_new_partner' in request.path:
                messages.success(request, 'Partner details Added Successfully.')
                return redirect('partner:index')
            else:
                messages.success(request, 'Partner details Updated Successfully.')
                return redirect('partner:index')
    else:
        if request.GET.get("partner"):
            context['page_title'] = context['add'] + ' for ' + request.GET.get("partner")
            form = PartnerForm(instance=partner, initial={'name': request.GET.get("partner")})
        else:
            form = PartnerForm(instance=partner)
    context['form'] = form
    return render(request, 'partner/add-edit-partner.html', context)


@login_required
def add_edit_member(request, pk=None):
    """
    Add/Edit/List Member details in this form
    :param request:
    :return: Member form/Member List
    """
    if pk:
        partner = get_object_or_404(Partner, pk=pk)
    member = Member()
    context = {}
    context['partner_name'] = partner.partner_name
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.partner = partner
            form_data.save()
            return redirect('partner:members_list', pk=pk)
    else:
        form = MemberForm(instance=member, initial={'partner': pk})
    context['form'] = form
    context['members_list'] = Member.member_obj.filter(partner=pk)
    print(context['members_list'])
    return render(request, 'partner/member-list.html', context)


