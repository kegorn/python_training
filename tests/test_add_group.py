# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.create(Group(name="new_group1", header="new_group1", footer="new_group1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.create(Group(name="", header="", footer=""))
    app.session.logout()

