from flask import current_app, flash, jsonify, redirect, render_template, request, url_for

from links.usecases import bookmark_details
from links.usecases import create_bookmark
from links.usecases import list_bookmarks
from links.usecases.interfaces import View
from links.settings import Settings


class BookmarkDetailsView(View):
    def generate_view(self, view_model):
        return render_template('bookmark_details.html', bookmark=view_model)


class ListBookmarksView(View):
    def generate_view(self, view_model):
        return render_template('list_bookmarks.html', bookmarks=view_model)


class ListBookmarksJSONView(View):
    def generate_view(self, view_model):
        return jsonify({'bookmarks': [bookmark for bookmark in view_model]})


class CreateBookmarkView(View):
    def __init__(self):
        self.form = None
        self.close_bookmarklet_window = False

    def generate_view(self, view_model):
        if self.form is None:
            raise Exception("A Flask WTF form was expected")
        if view_model['errors']:
            self._set_form_errors(view_model)
            return render_template('create_bookmark.html', form=self.form)

        if self.close_bookmarklet_window:
            current_app.logger.info("Closing bookmarklet window")
            return render_template('_close_bookmarklet_popup.html')

        # on success flash a message and redirect
        flash('Data saved!', 'info')
        return redirect(url_for('main.index'))

    def _set_form_errors(self, view_model):
        """
        Set form errors returned by the use case. This is not flask-wtf's auto form
        error filler thing.
        :param view_model:
        :return:
        """
        errors = view_model['errors']
        for key, error in errors.items():
            try:
                field = getattr(self.form, key)
            except AttributeError:
                continue
            field.errors.extend(view_model['errors'][key])


CONTROLLERS = {
    'get_bookmark_details': (
        bookmark_details.BookmarkDetailsController,
        bookmark_details.BookmarkDetailsUseCase,
        bookmark_details.BookmarkDetailsPresenter,
        BookmarkDetailsView,
    ),
    'list_bookmarks': (
        list_bookmarks.ListBookmarksController,
        list_bookmarks.ListBookmarksUseCase,
        list_bookmarks.ListBookmarksPresenter,
        ListBookmarksView,
    ),
    'list_bookmarks_json': (
        list_bookmarks.ListBookmarksController,
        list_bookmarks.ListBookmarksUseCase,
        list_bookmarks.ListBookmarksPresenter,
        ListBookmarksJSONView,
    ),
    'create_bookmark': (
        create_bookmark.CreateBookmarkController,
        create_bookmark.CreateBookmarkUseCase,
        create_bookmark.CreateBookmarkPresenter,
        CreateBookmarkView,
    ),
}


def controller_factory(name):
    parts = CONTROLLERS.get(name)
    if parts is None:
        raise Exception("Unknown Controller: {}".format(name))

    controller_cls, *args = parts
    controller = controller_cls(*(cls_() for cls_ in args))
    return controller
