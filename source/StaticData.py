import threading


class StaticData:
    stack = []
    trigger = threading.Event()
