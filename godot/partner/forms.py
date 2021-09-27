from .models import Partner, Member
from django import forms


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['partner_name', 'partner_gst', 'partner_phone', 'partner_email', 'agency_website']

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['partner', 'member_name', 'member_phone', 'member_email']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
