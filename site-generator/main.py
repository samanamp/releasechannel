from application_model import Application

for app in Application.scan():
    with open(app.app_name+".md", 'w') as app_md_doc:
        app_md_doc.write(app.md_generator())
