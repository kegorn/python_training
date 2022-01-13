# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    yield fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group1", header="new_group1", footer="new_group1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
