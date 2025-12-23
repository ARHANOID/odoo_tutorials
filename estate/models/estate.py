from odoo import fields, models


class Estate(models.Model):
    _name = "estate"
    _description = "Test test_model Estate"

    name = fields.Char(string="Title",required=True, default="Your new house")
    Description = fields.Char(default="Description")
    Postcode = fields.Char(required=True, default="Unknown2")
    Expected_Price = fields.Integer(required=True, default="100500")
    Bedrooms = fields.Integer(required=True, default="2")
    Facades = fields.Char(required=True, default="Unknown5")
    Garden = fields.Boolean(default=False)
    Garden_Orientation = fields.Char(required=True, default="Unknown7")
    Active = fields.Boolean(default=False)
    Avalible_From = fields.Datetime(string="Avalible_From",copy=False, default=fields.Datetime.now)
    Selling_Price = fields.Integer(required=True, readonly=True, copy=False, default="100500")
    Living_Area = fields.Integer(string="Living_Area(sqm)", required=True, default="0")
    Garage = fields.Boolean(default=False)
    Garage_Area = fields.Integer(string="Living_Area(sqm)", required=True, default="0")
    Status = fields.Char(required=True, default="Unknown99")
    print(fields.Datetime.now("6000"),fields.Datetime.now())



    def action_od_button(self):
        print("Estate first_od_button")
    # service_type = fields.Selection(string="Service Type", selection=[
    #     ("mobilised", "Mobilised"),
    #     ("contract", "Contract"),
    #     ("regular", "Regular")])
