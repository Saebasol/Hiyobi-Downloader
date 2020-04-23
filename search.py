import asyncio
import aiohttp
import json

async def hiyobilist(num):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://api.hiyobi.me/list/{num}') as r:
            response = await r.json() 
        titlelist = [a['title'] for a in response['list']]
        idlist = [a['id'] for a in response['list']]
        hiyolist = [str(index) + ". " + t for index, t in enumerate(titlelist, 1)]
        print("\n".join(hiyolist))
        return idlist

async def hiyobisearch(para):
    search = [t for t in para]
    data = {"search":search,"paging":1}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.hiyobi.me/search', json=data) as r:
            response = await r.json()
    idlist = [a['id'] for a in response['list']]
    titlelist = [a['title'] for a in response['list']]
    hiyolist = [str(index) + ". " + t for index, t in enumerate(titlelist, 1)]
    print("\n".join(hiyolist))
    return idlist


