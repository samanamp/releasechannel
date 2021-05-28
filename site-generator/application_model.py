import json
from datetime import datetime
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
        md_doc = f"""# {self.app_name}\n\n<div>
<demo-component app-code="{self.app_name.lower().replace(' ', '-')}"/>
</div>\n\n"""
        for update in self.get_updates():
            update_string = f"""\n## {update['version']}
<p style="font-size:12px;"> {datetime.strptime(update['updated'].replace('T',' ').replace('Z',''), '%Y-%m-%d %H:%M:%S').strftime('%d, %b %Y')} 
<a href="{update['link']}" target="_blank"> 
Source </a><OutboundLink /></p>\n{update['description']}\n"""
            md_doc += update_string

        return md_doc

class ApplicationUpdate:
   
    def __init__(self, version, updated, description, link):
        self.version = version
        self.updated = updated
        self.description = description
        self.link = link
