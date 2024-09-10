import requests
from bs4 import BeautifulSoup


def getGitHubRepositories(username: str) -> list[dict]:
    '''Parsing GitHub user repositories.

    :param username - github user name.
    '''

    html = requests.get(f'https://github.com/{username}?tab=repositories').text
    soup = BeautifulSoup(html, 'html.parser')

    repositories = []
    repositories_html = soup.find(id='user-repositories-list')
    if repositories_html:
        for r in repositories_html.find_all('li'):
            title = r.find(itemprop="name codeRepository").string.strip()
            description_value = r.find(itemprop="description")
            if description_value:
                description = description_value.string.strip()

            repositories.append({
                'title': title, 
                'description': description,
                'link': f'https://github.com/{username}/{title}',
            })

    return repositories


def getTelegramChannelPosts(channel_name: str) -> list[dict]:
    '''Parsing all the posts from Telegram channel.
    
    :param channel_name: Telegram channel name.
    '''

    html = requests.get(f'https://t.me/s/{channel_name}').text
    soup = BeautifulSoup(html, 'html.parser')

    posts = []
    posts_html = soup.find_all(class_='tgme_widget_message_bubble')
    if posts_html:
        for p in posts_html[1:]:
            title = p.find(class_='tgme_widget_message_text').find('b').string
            text = p.find(class_='tgme_widget_message_text').decode_contents()
            text = text.replace(f'<b>{title}</b><br/><br/>', '') # Removing title block from text
            link = p.find(class_='tgme_widget_message_date').get('href')
            posts.append({
                'title': title,
                'text': text,
                'link': link,
            })

    return posts
