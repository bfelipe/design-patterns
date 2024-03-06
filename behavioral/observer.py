from uuid import uuid4
from enum import Enum

class Publisher:
    
    def register_observer(self, observer):
        pass
    
    def remove_observer(self, observer):
        pass

    def notify(self):
        pass

class Status:
    OPEN='OPEN'
    CLOSED='CLOSED'

# Observer
class Window:
    def __init__(self, label:str):
        self.win_id = str(uuid4())
        self.label = label
        self.status = Status.CLOSED
    
    def open(self):
        self.status = Status.OPEN

    def close(self):
        self.status = Status.CLOSED


class RainMonitor(Publisher):
    def __init__(self):
        self.observers = dict()
        self.is_raining = False
    
    def detect_rain(self, is_raining:bool):
        self.is_raining = is_raining
        self.notify()
    
    def register_observer(self, window:Window):
        self.observers[window.win_id] = window
        self.notify()
    
    def remove_observer(self, window:Window):
        if self.observers.get(window.win_id):
            del self.observers[window.win_id]

    def notify(self):
        if self.is_raining:
            for window in self.observers.values():
                window.close()
        else:
            for window in self.observers.values():
                window.open()

windows = [Window('bed room'), Window('kitchen'), Window('rest room')]
monitor = RainMonitor()

print('-- Not Raining --')
for window in windows:
    monitor.register_observer(window)

for window in monitor.observers.values():
    print(f'Window {window.label}:{window.win_id} is {window.status}')

print('\n-- Raining --')
monitor.detect_rain(True)

for window in monitor.observers.values():
    print(f'Window {window.label}:{window.win_id} is {window.status}')

print(f'\n-- Removed window {windows[1].label} --')
monitor.remove_observer(windows[1])

for window in monitor.observers.values():
    print(f'Window {window.label}:{window.win_id} is {window.status}')

print('\n-- Adding window children bed room while raining--')
monitor.register_observer(Window('children bed room'))

for window in monitor.observers.values():
    print(f'Window {window.label}:{window.win_id} is {window.status}')

print('\n-- Not Raining --')
monitor.detect_rain(False)

for window in monitor.observers.values():
    print(f'Window {window.label}:{window.win_id} is {window.status}')

