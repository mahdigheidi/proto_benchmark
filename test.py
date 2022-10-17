import json
import random
import list_item_pb2
import time
import os
from google.protobuf.json_format import Parse
from google.protobuf.internal import api_implementation

class MyClass:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.age = random.randint(10, 30)
    
    def represent(self):
        print(self.name + self.last_name)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)
    
    @staticmethod
    def load(self, dictionary):
        self.__dict__ = dictionary
    


if __name__=='__main__':

    TEST_SIZE = int(os.getenv('TEST_SIZE'))
    LIST_SIZE = 1
    print(api_implementation.Type())
    #serializing
    print(f'Test size is {TEST_SIZE}')
    print('starting to serialize items...')
    serialized_lists = []
    start_time = time.time()
    for _ in range(TEST_SIZE):
        tmp = []
        for _ in range(LIST_SIZE):
            list_item = list_item_pb2.ListItem()
            list_item.commodity_id = random.randint(1, 1000)
            list_item.has_video = random.choice([True, False])
            tmp.append(list_item)
        list = list_item_pb2.List()
        list.listItem.extend(tmp)
        serialized_lists.append(list.SerializeToString())
    print('finished creating items.')
    print(f'Total time {time.time() - start_time}')

    #deserializing
    print('starting deserializing items...')
    deserialized_lists = []
    start_time = time.time()
    for serialized_list in serialized_lists:
        list = list_item_pb2.List()
        list.ParseFromString(serialized_list)
        deserialized_lists.append(list)
    print('finished deserializing.')
    print(f'Total time {time.time() - start_time}')
    

