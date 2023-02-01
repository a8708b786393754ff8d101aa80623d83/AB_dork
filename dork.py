#! /usr/bin/python3
from dork.controllers.controller_google import ControllerGoogle
from dork.controllers.controller_bing import ControllerBing
from dork.controllers.controller_duck_duck_go import ControllerDuckDuckGo

from dork.models.model_google import ModelGoogle
from dork.models.model_bing import ModelBing
from dork.models.model_duck_duck_go import ModelDuckDuckGo

from dork.views.view_google import ViewGoogle
from dork.views.view_bing import ViewBing
from dork.views.view_duck_duck_go import ViewDuckDuckGo

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
    if arg.map:
        controller.map(arg.map)
    if arg.film:
        controller.film(arg.film)
    if arg.in_anchor:
        controller.in_anchor(arg.in_anchor)
    if arg.blog_url:
        controller.blog_url(arg.blog_url)
    if arg.loc:
        controller.loc(arg.loc)
    if arg.site:
        controller.site(arg.site)

    controller.search()
    controller.view.query(controller.query)


if arg.google:
    google = ControllerGoogle(ModelGoogle(), ViewGoogle())
    run(google)


elif arg.bing:
    bing = ControllerBing(ModelBing(), ViewBing())
    run(bing)

elif arg.duck_duck_go:
    duck_duck_go = ControllerDuckDuckGo(ModelDuckDuckGo(), ViewDuckDuckGo())
    run(duck_duck_go)

else:
    print('choisi')
