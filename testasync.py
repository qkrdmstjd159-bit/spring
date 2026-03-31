# testasync.py  비동기처리를 확인

import time
import asyncio

print('비동기처리 async await ')
async def first():
    print('first회원인증 시작')
    await asyncio.sleep(3)
    print('first회원인증 종료')

async def two():
    print('\ntwo함수 mcp초린이야')
    print('two함수 mcp중린이야\n')

async def main():
    await first()
    print()
    await first()
    print()
    await first()
    await two()

asyncio.run(main())
