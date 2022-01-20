from model.group import Group


def test_modify_group_name(app):
    app.groupHelper.modify_first_group(Group(name="updated name"))


# def test_modify_group_empty_name(app):
#     if app.groupHelper.check_first_group(Group(name="")):
#         app.groupHelper.create(Group(name=""))
#         app.groupHelper.modify_first_group(Group(name="updated name for empty name17"))
#     else:
#         app.groupHelper.modify_first_group(Group(name="updated name for empty name18"))


def test_modify_group_header(app):
    app.groupHelper.modify_first_group(Group(header="updated header"))