class SaveVariableInStorage(object):
    def __init__(self, storage):
        self.storage = storage

    def __call__(self, key, value):
        self.storage[key] = value
    
    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value
    
    def __delitem__(self, key):
        del self.storage[key]
    