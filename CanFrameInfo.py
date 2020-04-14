class CanFrameInfo:
    def __init__(self):
        self.recevie_time = 0 # unit: s
        self.duration = self.recevie_time  # unit: s
        self.can_id = 0
        self.can_length = 0
        self.can_data = []
        self.can_type = "Rx"
        self.line_number = 0


    def show(self):
        print("------------------------"),
        print(self.__class__.__name__)
        print("------------------------")
        print("received time: %f"%self.recevie_time, end=", ")
        print("duration: %fS"%self.duration, end=", ")
        print("can id: %x"%self.can_id, end=", "),
        print("can type: %s"%self.can_type, end=", ")
        print("can length: %d"%self.can_length, end=", ")
        print("can data: [", end="")
        for data in self.can_data:
            print(data, end=" ")
        print("]")


    def filter_duration(self, filterValue):
        if self.duration >= filterValue:
            print("can received time: %f"%self.recevie_time, end=", ")
            print("duration: %fS" % self.duration, end=", ")