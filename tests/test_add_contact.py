from model.contact import Contact


def test_add_contact(app):
    app.contactHelper.create(Contact(firstname="new_fn_1", lastname="new_ln_1", address2="some_address_2"))