from flask import flash, render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access, SimpleFormView
from flask_babel import lazy_gettext as _

from . import appbuilder, db
from .forms import MyForm

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

"""
    Added 06/06 - Refactoring sqlflask (meetplan2dataset)
"""

class MyView(BaseView):
    default_view = 'databases'

    @expose('/databases/')
    @has_access
    def databases(self):
        # do something with param1
        # and return it
        param1 = 'Hello'
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)

    @expose('/tables/<string:param1>')
    @has_access
    def tables(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)
    
    @expose('/columns/<string:param1>')
    @has_access
    def columns(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        self.update_redirect()
        return self.render_template('method3.html',
                               param1 = param1)


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = "This is my first form view"
    message = "My form was submitted"

    def form_get(self, form):
        form.field1.data = "This was prefilled"

    def form_post(self, form):
        # post process form
        flash(self.message, "info")


appbuilder.add_view(
    MyFormView,
    "My form View",
    icon="fa-group",
    label=_("My form View"),
    category="My Forms",
    category_icon="fa-cogs",
)


appbuilder.add_view(MyView,"Databases", category='Admin')
appbuilder.add_link("Tables",href="/myview/tables/john", category="Admin")
appbuilder.add_link("Columns",href="/myview/columns/john", category="Admin")

db.create_all()
