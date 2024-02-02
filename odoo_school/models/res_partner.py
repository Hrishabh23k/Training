from odoo import fields, models, api, sql_db, SUPERUSER_ID
import psycopg2
from datetime import date


class Teacher(models.Model):
    _inherit = 'res.partner'


