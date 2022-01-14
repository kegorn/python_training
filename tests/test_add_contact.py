from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contactHelper.create(Contact(firstname="new_fn_1", lastname="new_ln_1", address2="some_address_2"))
    app.session.logout()