from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class RamaisWebsite(http.Controller):

    @http.route('/ramaisfun', type='http', auth='public', website=True)
    def ramais_list(self, **kw):
        _logger.warning("ROTA /ramaisfun FOI CHAMADA")

        Ramal = request.env['ramal.funcionario'].sudo()
        ramais = Ramal.search([], order='employee_id asc')

        return request.render('ramais.ramais_page', {
            'ramais': ramais,
        })