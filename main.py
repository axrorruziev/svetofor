import asyncio


async def red_svetofor():
    print('красный')
    await asyncio.sleep(0, 2)
    print('светит')


async def yellow_svetofor():
    print('желтый')
    await asyncio.sleep(0, 1)
    print('светит')


async def green_svetofor():
    print('зеленый')
    await asyncio.sleep(0, 1)
    print('светит')


async def start():
    task1 = asyncio.create_task(red_svetofor())
    task2 = asyncio.create_task(yellow_svetofor())
    task3 = asyncio.create_task(green_svetofor())
    await task1, task2, task3


asyncio.run(start())

import threading
import time


def print_red():
    for i in range(5):
        time.sleep(1)  #
        print("красный светит")


def print_yellow():
    for i in range(5):
        time.sleep(1)  #
        print("желтый светит")


def print_green():
    for i in range(5):
        time.sleep(1)  #
        print("зеленый светит")


thread1 = threading.Thread(target=print_red)
thread2 = threading.Thread(target=print_yellow())
thread3 = threading.Thread(target=print_green())
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
