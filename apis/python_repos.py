"""
Uses the GitHub public API to chart the most starred public Python repos
"""
from typing import Any, Dict, List

import requests
from requests.models import Response
import pygal
from pygal import style
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS
from pygal.config import Config

# Make an API call and store the response
url: str = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
resp: Response = requests.get(url)
print(f'Status code: {resp.status_code}')

# Examine response. This will also let us know if something went wrong.
response_dict: Dict[str, Any] = resp.json()
print(response_dict.keys())
print('Total repositories: ', response_dict['total_count'])

# Collect information we are interested in from response
repos: List[Dict[str, Any]] = response_dict['items']

names: List[str] = []
plot_entries: List[Dict[str, Any]] = []

for repo in repos:
    names.append(repo['name'])
    description = repo['description']
    if not description:
        description = 'No description provided.'
    plot_entry = {
        'value': repo['stargazers_count'],
        'label': description,
        'x-link': repo['html_url']
    }
    plot_entries.append(plot_entry)

# Make visualization
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config: Config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', plot_entries)
chart.render_to_file('python_repos.svg')
