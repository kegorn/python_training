# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.contact import ContactHelper
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    yield fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.create(Group(name="new_group1", header="new_group1", footer="new_group1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.create(Group(name="", header="", footer=""))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contactHelper.create(Contact(firstname="new_fn_1", lastname="new_ln_1", address2="some_address_2"))
    app.session.logout()