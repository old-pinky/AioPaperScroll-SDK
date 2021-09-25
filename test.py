from re import I
from asyncpaperscroll import AsyncPaperScroll
from asyncpaperscroll.methods import PaperScrollMethods
import asyncio

aps = AsyncPaperScroll(access_token='rngerngrgrerognreogne', merchant_id=5489449784)


async def main():
    someMerchants = await PaperScrollMethods(aps).getMerchants()
    print(someMerchants)


asyncio.run(main())
