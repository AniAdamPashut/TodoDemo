import common

class Database:
    def store(self, task: common.Task):
        raise NotImplementedError
    
    def load(self, name: str):
        raise NotImplementedError

    def delete(self, name: str):
        raise NotImplementedError