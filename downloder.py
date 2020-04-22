import asyncio
import aiohttp
import aiofiles
import json
import os
 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' +  directory)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def getimg(num):
    async with aiohttp.ClientSession() as session:
        json = await fetch(session, f'https://cdn.hiyobi.me/data/json/{num}_list.json')
        listimg = [d['name'] for d in json]
        return listimg

async def download(s: str,num):
    async with aiohttp.ClientSession() as resp:
        async with resp.get(f'https://cdn.hiyobi.me/data/{num}/{s}') as res:
            async with aiofiles.open(f'{num}/{s}', mode='wb') as f:
                await f.write(await res.read())

if __name__ == '__main__':
    num = input("번호를 입력해주세요\n")
    loop = asyncio.get_event_loop()
    createFolder(f'./{num}')
    lists = loop.run_until_complete(getimg(num=num))
    tasks = [download(x, num=num) for x in lists]
    loop.run_until_complete(asyncio.wait(tasks))
