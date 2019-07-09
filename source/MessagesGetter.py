from source.APIWorker import APIWorker
import asyncio
from threading import Thread


class MessagesGetter(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        vk = APIWorker()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.create_task(vk.get_events())
        loop.run_forever()
        loop.close()
