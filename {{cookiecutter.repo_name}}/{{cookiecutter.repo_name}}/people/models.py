from __future__ import unicode_literals

from django.db import models

from modelcluster.models import ClusterableModel
# from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
# from wagtail.wagtailsearch import index
# from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
# from wagtail.wagtailcore.fields import StreamField
# from wagtail.wagtailadmin.edit_handlers import (
#         FieldPanel,
#         InlinePanel,
#         StreamFieldPanel,
#         PageChooserPanel
#         )
from wagtail.wagtailsnippets.models import register_snippet
# from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
# from {{cookiecutter.repo_name}}.blocks import GlobalStreamBlock


@register_snippet
class PersonStatus(ClusterableModel):
    """
    This snippet may or may not need to be here...
    """
    pass


class PersonStatusRelationship(models.Model):
    """
    If a relationship _does_ need to happen
    Docs: http://www.tivix.com/blog/working-wagtail-i-want-my-m2ms/
    """
    pass


class PersonLocationRelationship(models.Model):
    """
    Depending if you want a location relationship
    """
    pass


class PersonSkillsRelationship(Orderable, models.Model):
    """
    Depending if you want a skills relationship

    """
    pass


class PersonPage(Page):
    pass


class PersonIndexPage(Page):
    pass
