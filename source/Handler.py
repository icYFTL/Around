from source.EventHandler import EventHandler
from source.StaticData import StaticData

import os
import signal


class Handler:
    @staticmethod
    def events_handler():
        while True:
            try:
                StaticData.trigger.wait()
                EH = EventHandler(StaticData.stack.pop())
                repl = EH.allocate()
                if repl:
                    print(repl)
                StaticData.trigger.clear()
            except KeyboardInterrupt:
                os.kill(os.getpid(), signal.SIGUSR1)
