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

class ApplicationUpdate:
   
    def __init__(self, version, updated, description, link):
        self.version = version
        self.updated = updated
        self.description = description
        self.link = link
