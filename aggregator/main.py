import feedparser
import pprint
from application_model import Application, ApplicationUpdate
# from db_handler_class import DbHandler

# db_handler = DbHandler().f()
# NewsFeed = feedparser.parse("https://github.com/vuejs/vue/releases.atom")
# entry = NewsFeed.entries[1]

# Application.create_table(read_capacity_units=1, write_capacity_units=1)

# app = Application('Nginx Ingress Controller')
# app.rss_link = "https://github.com/kubernetes/ingress-nginx/releases.atom"
# app.save()

for app in Application.scan():
    print(app.rss_link)
    NewsFeed = feedparser.parse(app.rss_link)
    entry = NewsFeed.entries[1]
    # print(entry)
    # print(entry['title'])
    update_list = []
    for entry in NewsFeed.entries:
        app_update = ApplicationUpdate(entry['title'], entry['updated'], entry['content'][0]['value'], entry['link'])
        update_list.append(app_update.__dict__)

    app.updates = str(update_list)
    app.save()

