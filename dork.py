#! /usr/bin/python3
from dork.controllers.controller_google import ControllerGoogle

from dork.models.model_google import ModelGoogle

from dork.views.view_google import ViewGoogle


google = ControllerGoogle(ModelGoogle(), ViewGoogle())

google.file_type('pdf')