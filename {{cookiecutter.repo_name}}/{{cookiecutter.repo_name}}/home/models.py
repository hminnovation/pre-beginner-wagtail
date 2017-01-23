from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
        FieldPanel,
        MultiFieldPanel,
        PageChooserPanel
        )


class HomePage(Page):
    """
    The HomePage model does whatever you want it to...
    """
    pass
