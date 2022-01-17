from model.group import Group


def test_modify_group_name(app):
    app.groupHelper.modify_first_group(Group(name="updated name"))


def test_modify_group_header(app):
    app.groupHelper.modify_first_group(Group(header="updated header"))