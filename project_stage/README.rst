.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============
Project Stage
=============

Create module project stage and add it on project header form and project search.
This is a port of https://github.com/ingadhoc/project/tree/9.0/project_stage
To make it fully work we need to replase last line of file security/ir.model.access.csv to meet with odoo 10 external ids. Currently Odoo 10 say it doesn't recornize base.group_sale_salesman I suppose it was renamed in odoo 10. If you know it's new name please tell.
To install the module currently you neet to delete last line of file security/ir.model.access.csv

Configuration
=============

To configure this module, you need to:
add stages in project kanban view

Usage
=====

To use this module, you need to:


.. branch is "10.0" for example


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/m3dbedb/{project_repo}/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.


