from odoo import models, fields

class RamalFuncionario(models.Model):
    _name = "ramal.funcionario"
    _description = "Ramal do Funcionário"
    _rec_name = "employee_id"

    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Funcionário",
        required=True,
        ondelete="cascade",
    )

   
    employee_name = fields.Char(
        string="Nome",
        related="employee_id.name",
        store=True,
        readonly=True,
    )

    ramal = fields.Char(string="Ramal", required=True)

    mobile_phone = fields.Char(
        string="Celular",
        related="employee_id.mobile_phone",
        store=True,
        readonly=False,
    )

    work_email = fields.Char(
        string="E-mail",
        related="employee_id.work_email",
        store=True,
        readonly=False,  
    )

    _sql_constraints = [
        ("uniq_employee", "unique(employee_id)", "Este funcionário já possui um ramal cadastrado."),
        ("uniq_ramal", "unique(ramal)", "Este ramal já está em uso."),
    ]