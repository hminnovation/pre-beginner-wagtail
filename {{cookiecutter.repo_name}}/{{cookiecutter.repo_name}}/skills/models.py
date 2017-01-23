from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
# from wagtail.wagtailsearch import index
# from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
# from wagtail.wagtailcore.fields import RichTextField
# from wagtail.wagtailadmin.edit_handlers import FieldPanel


class SkillsPage(Page):
    """
    This is a page for all the details about a specific skill (if you've got any)
    """
    pass


class SkillsIndexPage(Page):
    """
    This is a page to list all the skills on the site
    """
    pass
