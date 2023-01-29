#! /usr/bin/python3
from dork.controllers.controller_google import ControllerGoogle
from dork.controllers.controller_bing import ControllerBing

from dork.models.model_google import ModelGoogle
from dork.models.model_bing import ModelBing

from dork.views.view_google import ViewGoogle
from dork.views.view_bing import ViewBing

from args import parser


arg = parser()


def run(controller: object) -> None:
    controller.view.banner()
    controller.view.user_agent(controller.user_agent)
    controller.set_page_count(arg.counter_page)

    if arg.element: 
        controller.set_item(arg.element)

    if arg.file_type:
        controller.file_type(arg.file_type)
    if arg.in_text:
        controller.in_text(arg.in_text)
    if arg.in_all_text:
        controller.in_all_text(arg.in_all_text)
    
    controller.search()
    controller.view.query(controller.query)


if arg.google:
    google = ControllerGoogle(ModelGoogle(), ViewGoogle())
    run(google)


elif arg.bing:
    bing = ControllerBing(ModelBing(), ViewBing())
    run(bing)

else:
    print('choisi')
