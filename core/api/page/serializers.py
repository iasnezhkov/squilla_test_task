# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from core.models import Page


class PageSerializer(serializers.ModelSerializer):
    sub_pages = serializers.ListSerializer(source='children', child=RecursiveField(), read_only=True)

    class Meta:
        model = Page
        fields = ('id', 'name', 'content', 'parent', 'sub_pages')
