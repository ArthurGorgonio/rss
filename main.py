from dateutil import parser
from datetime import datetime
import feedparser
import pytz


today_utc = datetime.now().astimezone(pytz.utc)


with open('urls.txt', 'r') as f:
    urls = f.readlines()

for url in urls:
    feed = feedparser.parse(url)
    count = 0

    for entry in feed.entries:

        try:
            article_date = entry['updated']
        except KeyError:
            article_date = entry['published']
        article_published_at = parser.parse(article_date).astimezone(pytz.utc)

        if (today_utc - article_published_at).days > 0:
            send_slack = False
        else:
            send_slack = True
            count += 1

        if not send_slack:
            continue
        else:
            article_title = entry.title
            article_link = entry.link
            content = entry.summary
            print(f'{article_title}[{article_link}]\n'
                  f'Published at {article_published_at}\n'
                  f'Make a Slack Post? {send_slack}\n'
                  f'----------------------------------\n\n\n')
    if count:
        print(f'{count} posts must be sended to slack')
    else:
        print(f'No more posts to be sent in\n {url}')
