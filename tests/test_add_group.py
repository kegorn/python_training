# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.groupHelper.create(Group(name="new_group1", header="new_group1", footer="new_group1"))


def test_add_empty_group(app):
    app.groupHelper.create(Group(name="", header="", footer=""))


