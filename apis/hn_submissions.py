"""
Exploration of the Hacker News Api
"""


from typing import Any, Dict, List, Union
import requests
from operator import itemgetter

# Fetch top story IDs
url: str = 'https://hacker-news.firebaseio.com/v0/topstories.json'
resp = requests.get(url)
print(f'Status code: {resp.status_code}')
submission_ids: list[int] = resp.json()

# Fetch submission details for first 30 story IDs
submissions: List[Dict[str, Union[str, int]]] = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/'
        + str(submission_id)
        + '.json')
    submission_resp = requests.get(url)
    print(submission_resp.status_code)
    submission_resp_body: Dict[str, str] = submission_resp.json()

    submission = {
        'title': submission_resp_body['title'],
        'link': f'http://news.ycombinator.com/item?id={str(submission_id)}',
        'comments': submission_resp_body.get('descendants', 0)
        }
    submissions.append(submission)

submissions = sorted(submissions, key=itemgetter('comments'), reverse=True)

for submission in submissions:
    print('\nTitle: ', submission['title'])
    print('Discussion Link: ', submission['link'])
    print('Comments: ', submission['comments'])
