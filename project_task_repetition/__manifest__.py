# -*- coding: utf-8 -*-
{
    'name': "Project task repetition",
    'summary'       : 'Allows to set repetition of project tasks',
    'description'   : """
With this module you are able to repeat project tasks pretty much in the same way as you repeat calendar events.
    """,

    'author'        : 'Openworx',
    'website'        : 'http://www.openworx.nl',
    'license': 'AGPL-3',
    'price': 29.00,
    'currency': 'EUR',
    'category': 'Project',
    'version': '1.1',
    'depends': ["project"],
    'data': [
        'project_task_repetition_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
