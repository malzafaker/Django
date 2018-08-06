# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, redirect, resolve_url


def error400(request):
    response = render_to_response('errors/op_error_400.html', {})
    response.status_code = 400
    return response


def error403(request):
    response = render_to_response('errors/op_error_403.html', {})
    response.status_code = 403
    return response


def error404(request):
    response = render_to_response('errors/op_error_404.html', {})
    response.status_code = 404
    return response


def error500(request):
    response = render_to_response('errors/op_error_501.html', {})
    response.status_code = 500
    return response
