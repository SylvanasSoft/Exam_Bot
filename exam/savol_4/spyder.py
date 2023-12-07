import asyncio

import httpx
from bs4 import BeautifulSoup


async def get_response(url: str):
    async with httpx.AsyncClient() as res:
        temp = await res.get(url)
    return temp.content


async def get_news():
    response = await get_response('https://www.fitnessblender.com/')
    soup = BeautifulSoup(response, 'html.parser')
    article = soup.find('div', class_='vue cards')
    titles = [i.text for i in article.find_all('h2', class_='category')]
    # for i in article.find('div', class_='summary-group'):
    #     print(i)
    times = [i.text for i in soup.find_all('a')]
    return titles
