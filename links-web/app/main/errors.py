from flask import request, jsonify
from . import main
from links.exceptions import LinksError


def format_json():
    return (
        request.accept_mimetypes.accept_json
        and not request.accept_mimetypes.accept_html
    )


@main.errorhandler(LinksError)
def internal_server_error(e):
    msg = 'Internal Server Error'
    if format_json():
        return jsonify({'error': msg})
    return msg, 500
