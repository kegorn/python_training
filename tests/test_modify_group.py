from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.modify_first_group(Group(name="updated name"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.groupHelper.modify_first_group(Group(header="updated header"))
    app.session.logout()