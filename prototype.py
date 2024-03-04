from uuid import uuid4

class Container:
    def __init__(self, mem='256mb', cores=1, app_lang='go', image='alphine'):
        self.container_id = str(uuid4())
        self.mem = mem
        self.cores = cores
        self.app_lang = app_lang
        self.image = image
    
    def clone(self):
        return Container(self.mem, self.cores, self.app_lang, self.image)

    def __repr__(self):
        return f'<Container {self.container_id} - {self.mem} - {self.cores} - {self.app_lang} - {self.image}>'
    
container_a = Container(mem='2gb', cores=2, app_lang='java')
print(container_a)
container_b = container_a.clone()
container_b.app_lang = 'scala'
print(container_b)
container_c = Container()
print(container_c)