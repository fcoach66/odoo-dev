# -*- coding: utf-8 -*-
from odoo import models, fields, api 

class TodoTask(models.Model): 
    _inherit = 'todo.task' 
    user_id = fields.Many2one('res.users', 'Responsible') 
    date_deadline = fields.Date('Deadline')
	
	@api.multi 
	def do_clear_done(self): 
    domain = [('is_done', '=', True), 
               '|', ('user_id', '=', self.env.uid), 
                    ('user_id', '=', False)] 
    dones = self.search(domain) 
    dones.write({'active': False}) 
    return True