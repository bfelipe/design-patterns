class CommandRunner:
    _instance = None

    def __new__(cls, *args, **kwargs):
        '''
            __new__ method overrides control creation of instance
            using _istance attribute.
        '''
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def run(self, command:str):
        print(f'Running command: {command}')


cmdA = CommandRunner()
cmdB = CommandRunner()

cmdA.run('echo hello')
print(cmdA)

cmdB.run('cat poem.txt')
print(cmdB)

print(f'cmdA and cmdB is same obj: {id(cmdA)== id(cmdB)}')