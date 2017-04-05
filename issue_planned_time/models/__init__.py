# -*- coding: utf-8 -*-

from . import models

class ProjectIssue(models.Model):
    _inherit = 'project.issue'
    _date_name = "date_start"
	date_end = fields.Datetime(string='Ending Date', index=True, copy=False)
	planned_hours = fields.Float(string='Initially Planned Hours', help='Estimated time to do the task, usually set by the project manager when the task is in draft state.')
    remaining_hours = fields.Float(string='Remaining Hours', digits=(16,2), help="Total remaining time, can be re-estimated periodically by the assignee of the task.")
     @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        if any(self.filtered(lambda task: task.date_start and task.date_end and task.date_start > task.date_end)):
            raise ValidationError(_('Error ! Task starting date must be lower than its ending date.'))