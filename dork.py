#! /usr/bin/python3
from dork.controllers.controller_google import ControllerGoogle
from dork.controllers.controller_bing import ControllerBing

from dork.models.model_google import ModelGoogle
from dork.models.model_bing import ModelBing

from dork.views.view_google import ViewGoogle
from dork.views.view_bing import ViewBing


google = ControllerGoogle(ModelGoogle(), ViewGoogle())
bing = ControllerBing(ModelBing(), ViewBing())
