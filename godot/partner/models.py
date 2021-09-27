from django.db import models


class Partner(models.Model):
    partner_name = models.CharField(max_length=100)
    partner_gst = models.CharField(max_length=100)
    partner_phone = models.IntegerField()
    partner_email = models.EmailField()
    agency_website = models.URLField()

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"
        db_table = "partner"
    partner_obj = models.Manager()


class Member(models.Model):
    member_name = models.CharField(max_length=100)
    partner = models.ForeignKey('Partner', models.DO_NOTHING, null=True, blank=True)
    member_phone = models.IntegerField()
    member_email = models.EmailField()

    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"
        db_table = "member"

    member_obj = models.Manager()
