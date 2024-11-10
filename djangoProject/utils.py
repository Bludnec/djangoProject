from django.shortcuts import render

from djangoProject.decorators import my_login_required


@my_login_required
def main_render(request, template, page_dict, page_name=None, page_main_menu=None, page_title=None, page_subtitle=None):
    page_dict['page_name'] = page_name
    page_dict['page_main_menu'] = page_main_menu
    page_dict['page_title'] = page_title
    page_dict['page_subtitle'] = page_subtitle
    page_dict['user'] = request.user

    return render(request, template, page_dict)
