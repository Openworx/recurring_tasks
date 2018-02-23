# -*- coding: utf-8 -*-
{
    'name': "Project task repetition",
    'summary': 'Allows to set repetition of project tasks',
    'description': """
With this module you are able to repeat project tasks pretty much in the same way as you repeat calendar events.
    """,

    'author': 'Openworx',
    'website': 'http://www.openworx.nl',
    'license': 'AGPL-3',
    'price': 39.00,
    'currency': 'EUR',
    'category': 'Projects',
    'version': '1.1',
    'depends': ["project"],
    'data': [
        'views/project_task_repetition_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
