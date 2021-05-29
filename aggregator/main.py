import feedparser
from time import sleep
import pprint
from application_model import Application, ApplicationUpdate
import yaml
# from db_handler_class import DbHandler

# db_handler = DbHandler().f()
# NewsFeed = feedparser.parse("https://github.com/vuejs/vue/releases.atom")
# entry = NewsFeed.entries[1]

# Application.create_table(read_capacity_units=1, write_capacity_units=1)

# app = Application('Nginx Ingress Controller')
# app.rss_link = "https://github.com/kubernetes/ingress-nginx/releases.atom"
# app.save()
with open(r'app_list.yaml') as app_list_file:
    app_list = yaml.load(app_list_file, Loader=yaml.FullLoader)['apps']

for app in app_list:
    print(app['name'])
    NewsFeed = feedparser.parse(app['rss'])
    application = Application()
    application.app_name = app['name']
    application.rss_link = app['rss']

    update_list = []
    for entry in NewsFeed.entries:
        app_update = ApplicationUpdate(entry['title'], entry['updated'], entry['content'][0]['value'], entry['link'])
        update_list.append(app_update.__dict__)
    
    application.set_updates(update_list)
    application.save()
    sleep(0.5)

