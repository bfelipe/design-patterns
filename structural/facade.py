from enum import Enum

class PowerMode(Enum):
    PERFORMANCE='PERFORMANCE'
    BALANCED='BALANCED'
    POWERSAVE='POWERSAVE'

class Switch(Enum):
    ON='ON'
    OFF='OFF'

class Network:
    def __init__(self):
        self.wifi = Switch.ON

    def set_wifi(self, switch:Switch):
        self.wifi = switch

    def __repr__(self):
        return f'wifi: {self.wifi}'

class CPUManager:
    def __init__(self):
        self.cores = 4
        self.cores_running = self.cores

    def set_cores_running(self, cores:int):
        self.cores_running = cores

    def reset_cores_running(self):
        self.cores_running = self.cores

    def __repr__(self):
        return f'cores: {self.cores} running: {self.cores_running}'

class SystemMode:

    def __init__(self):
        self.power_mode = PowerMode.BALANCED
        self.notifications = Switch.ON
        self.network = Network()
        self.cpu = CPUManager()

    def set_default_mode(self):
        self.power_mode = PowerMode.BALANCED
        self.notifications = Switch.ON
        self.network.set_wifi(Switch.ON)
        self.cpu.reset_cores_running()

    def set_game_mode(self):
        self.power_mode = PowerMode.PERFORMANCE
        self.notifications = Switch.OFF
        self.network.set_wifi(Switch.ON)
        self.cpu.reset_cores_running()

    def set_work_mode(self):
        self.power_mode = PowerMode.BALANCED
        self.notifications = Switch.OFF
        self.network.set_wifi(Switch.ON)
        self.cpu.set_cores_running(2)

    def set_travel_mode(self):
        self.power_mode = PowerMode.POWERSAVE
        self.notifications = Switch.OFF
        self.network.set_wifi(Switch.OFF)
        self.cpu.set_cores_running(2)

    def set_power_save_mode(self):
        self.power_mode = PowerMode.POWERSAVE
        self.notifications = Switch.OFF
        self.network.set_wifi(Switch.OFF)
        self.cpu.set_cores_running(1)

    def description(self):
        print(f'Power Mode {self.power_mode}')
        print(f'Notifications {self.notifications}')
        print(f'Network {self.network}')
        print(f'CPU {self.cpu}')

sm = SystemMode()
sm.set_default_mode()
sm.description()
print('---')
sm.set_game_mode()
sm.description()
print('---')
sm.set_work_mode()
sm.description()
print('---')
sm.set_travel_mode()
sm.description()
print('---')
sm.set_power_save_mode()
sm.description()