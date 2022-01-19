
from model.group import Group


def test_delete_first_group(app):
    if app.groupHelper.count_groups() == 0:
        app.groupHelper.create(Group(name="Group_to_delete"))
    app.groupHelper.delete_first_group()


# def test_delete_all_groups(app):
#     while app.groupHelper.count_groups() > 0:
#         app.groupHelper.delete_first_group()