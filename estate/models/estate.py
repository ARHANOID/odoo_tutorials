from odoo import fields, models

class Estate(models.Model):
    _name = "estate"
    _description = "Test test_model Estate"

    name = fields.Char(required=True, default="Unknown0")
    action = fields.Char(required=True, default="Unknown1")
    action1 = fields.Char(required=True, default="Unknown2")
    action2 = fields.Char(required=True, default="Unknown3")
    action3 = fields.Char(required=True, default="Unknown4")
    action4 = fields.Char(required=True, default="Unknown5")
    action5 = fields.Char(required=True, default="Unknown6")
    action6 = fields.Char(required=True, default="Unknown7")
    action7 = fields.Char(required=True, default="Unknown8")
    action8 = fields.Char(required=True, default="Unknown9")
    action9 = fields.Char(required=True, default="Unknown99")
