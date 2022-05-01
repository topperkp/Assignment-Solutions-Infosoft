class DataStream():
    time_str_map = {}

    def __init__(self):
        pass

    def should_output_data_str(self, timestamp: int , data_string: str):
        if data_string in self.time_str_map:
            if self.time_str_map[data_string] + 5 >= timestamp:
                return False
            else:
                self.time_str_map[data_string] = timestamp
                return True
        self.time_str_map[data_string] = timestamp
        return True

data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=8, data_string="world"))
