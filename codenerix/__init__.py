__version__ = "1.1.24"

__authors__ = [
    'Juan Miguel Taboada Godoy <juanmi@juanmitaboada.com>',
    'Juan Soler Ruiz <soleronline@gmail.com>',
]

__requirements__ = {
    'all': [
        "pymongo",
        "python-dateutil",
        "django-recaptcha>=1.2.1,<1.3",
        "django-rosetta",
        "jsonfield",
        "openpyxl",
        "Pillow",
        "Unidecode",
        "Django>=1.10.8",
        "django-multi-email-field",
        "ldap3",
        "django-haystack>=2.6.1",
        "pytz",
        "elasticsearch>=2.0.0,<3.0.0",
    ],
    '2': [
        "html5lib==1.0b8",  # Default version 0.99999999 is broken with error 'from html5lib import treebuilders, inputstream' => 'ImportError: cannot import name inputstream' (1.0b10 also fails)
    ],
    '3': [
        "html5lib",
        ],
    }
