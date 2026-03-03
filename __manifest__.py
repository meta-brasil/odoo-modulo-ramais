{
    "name": "Ramais",
    "version": "1.0.0",
    "author": "Guilherme Borsi",
    "license": "AGPL-3",
    "category": "Employee",
    "summary": "Modulo para controle de ramais",
    "description": """
Módulo para gerenciamento e controle de ramais.
""",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/ramal_views.xml",
    ],
    "installable": True,
    "application": True,
}