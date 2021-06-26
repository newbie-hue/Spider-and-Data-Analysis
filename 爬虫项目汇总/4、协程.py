#requests.get()   同步的代码——》异步的操作 aiohttp


import asyncio
import aiohttp

urls=[

]


async  def aiodownload(url):
     name=url.rsplit('/',1)[1]
     async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:  # resp=session.get(url)
            with open(name,'ab+',encoding='utf-8') as f:
                f.write(await resp.content.read())
     print('iib')

async def main():
    tasks=[]
    for url in urls:
        tasks.append(url)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())

