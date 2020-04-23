import asyncio
import downloder
import search

loop = asyncio.get_event_loop()

check = input("다운은 1번 검색은 2번을 입력해주세요\n")
if check == str(1):
    num = input("번호를 입력해주세요\n")
    downloder.createFolder(f'./{num}')
    lists = loop.run_until_complete(downloder.getimg(num=num))
    tasks = [downloder.download(x, num=num) for x in lists]
    loop.run_until_complete(asyncio.wait(tasks))

if check == str(2):
    check = input("리스트검색은 1번, 제목,태그검색은 2번을 입력해주세요\n")

    if check == str(1):
        num = input("리스트검색입니다. 몇번쨰 페이지를 검색할까요?\n")
        idlist = loop.run_until_complete(search.hiyobilist(num=num))
        check = input("다운로드할까요? Y/N\n")
        if check == str('Y') or str('y'):
            num = input("리스트중 골라주세요\n")
            hiyoid = idlist[int(num) - 1]
            downloder.createFolder(f'./{hiyoid}')
            lists = loop.run_until_complete(downloder.getimg(num=hiyoid))
            tasks = [downloder.download(x, num=hiyoid) for x in lists]
            loop.run_until_complete(asyncio.wait(tasks))

    if check == str(2):
        para = input("제목,태그검색입니다. 어떤걸 검색할까요?\n")
        idlist = loop.run_until_complete(search.hiyobisearch(para=para))
        check = input("다운로드할까요? Y/N\n")
        if check == str('Y') or str('y'):
            num = input("리스트중 골라주세요\n")
            hiyoid = idlist[int(num) - 1]
            downloder.createFolder(f'./{hiyoid}')
            lists = loop.run_until_complete(downloder.getimg(num=hiyoid))
            tasks = [downloder.download(x, num=hiyoid) for x in lists]
            loop.run_until_complete(asyncio.wait(tasks))