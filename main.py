import asyncio
import dotenv

from bot import __main__
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

dotenv.load_dotenv()


async def worker():
    print(1)


async def bot():
    for i in range(0, 10):
        print(i)
        await asyncio.sleep(1.)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(__main__())

    loop.close()

