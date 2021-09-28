from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('partner',
                  'member_name',
                  'member_email',
                  'member_phone')