import json
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Application(Model):
    """
    A DynamoDB Application Model
    """
    class Meta:
        table_name = "application"
    app_name = UnicodeAttribute(hash_key=True)
    rss_link = UnicodeAttribute(null=True)
    updates = UnicodeAttribute(null=True)

    def set_updates(self, updates_list):
        self.updates = json.dumps(updates_list)
    
    def get_updates(self):
        return json.loads(self.updates)

    def md_generator(self):
        md_doc = f"""# {self.app_name} #\n"""
        for update in self.get_updates():
            update_string = f"""## {update['version']} ##\n ### {update['updated']} ### \nLink: {update['link']} \n{update['description']}\n"""
            md_doc += update_string

        return md_doc

class ApplicationUpdate:
   
    def __init__(self, version, updated, description, link):
        self.version = version
        self.updated = updated
        self.description = description
        self.link = link
