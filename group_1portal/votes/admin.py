from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html
from votes.models import Vote, Option

class OptionInLine(admin.TabularInline):
    model = Option
    fields = ["value"]
    extra = 2

class VoteAdmin(admin.ModelAdmin):
    model = Vote
    inlines = [OptionInLine]
    list_display = ("title", "details")

    def details(self, obj):
        url = reverse_lazy("votes:vote-detail", kwargs={"pk": obj.pk})
        return format_html('<a href="{}">See details</a>', url)
    details.short_description = "Details page"


# Register your models here.
admin.site.register(Vote, VoteAdmin)