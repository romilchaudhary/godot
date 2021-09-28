from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import PartnerForm, MemberForm
from .models import Partner, Member
from django.contrib import messages
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import MemberSerializer
from rest_framework.decorators import api_view


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
    context = dict()
    context['partner_name'] = partner.partner_name
    context['partner_id'] = partner.id
    form = MemberForm(instance=member, initial={'partner': pk})
    context['form'] = form
    context['members_list'] = Member.member_obj.filter(partner=pk).order_by('-id')
    return render(request, 'partner/member-list.html', context)


# member ajax submit
def member_ajax_save(request, pk=None):
    """
    ajax callback for member form submit
    :param request: form data
    :param pk: partner id
    :return: submitted form data and message
    """
    if pk:
        partner = get_object_or_404(Partner, pk=pk)
    if request.is_ajax():
        name = request.POST.get('member_name', None)
        email = request.POST.get('member_email', None)
        phone = request.POST.get('member_phone', None)
        Member.member_obj.create(
            member_name=name,
            partner=partner,
            member_phone=phone,
            member_email=email,
        )
        response = {
                     'msg': 'Your form has been submitted successfully',
                     'member_name': name,
                     'member_phone': phone,
                     'member_email': email,
        }
        return JsonResponse(response) # return response as JSON


@api_view(['POST'])
def save_member_api(request):
    if request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
