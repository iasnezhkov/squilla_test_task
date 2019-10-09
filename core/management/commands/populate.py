#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from core.models import Page
from random import randint

User = get_user_model()


def create_user():
    username = 'test'
    password = 'testtest'
    user = User.objects.filter(username=username).first()

    if not user:
        user = User.objects.create_user(username=username, password=password)
        user.save()

    print('Username: `{username}` with password: `{password}` created!'.format(username=username, password=password))


def create_pages(page_ids=None, count=0):
    if not page_ids:
        page_ids = []

    count += 1
    new_page_ids = []

    if count >= 4:
        return False

    if not page_ids:
        for i in range(randint(1, 2)):
            page = Page(name='Page %s' % i, content='Page content %s' % i)
            page.save()
            new_page_ids.append(page.id)

    for page_id in page_ids:
        for i in range(randint(1, 3)):
            page = Page(name='Page %s %s' % (page_id, i), content='Page content %s %s' % (page_id, i), parent_id=page_id)
            page.save()
            new_page_ids.append(page.id)

    for i in range(3):
        create_pages(page_ids=new_page_ids, count=count)

    return True


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_user()
        create_pages()
