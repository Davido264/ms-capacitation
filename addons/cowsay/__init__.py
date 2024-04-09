# -*- coding: utf-8 -*-
import os
import sys

dirname = os.path.dirname
odoo_path = os.path.join(dirname(dirname(dirname(__file__))),"odoo","odoo")
sys.path.insert(0,odoo_path)

from . import controllers
from . import models
