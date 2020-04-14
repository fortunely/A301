# -*- coding: utf-8 -*-
from CanFrameInfo import CanFrameInfo
from Signal import Signal

output_file_name1 = "BCM_288_turnleftlight.txt"
output_file_name2 = "BCM_288_turnrightlight.txt"

#BcmTurnIndcrLe	左转向灯信号	288	40ms	startbit = 14	length = 2
#BcmTurnIndcrRi	右转向灯信号	288	40ms	startbit = 12	length = 2
class BCM(object):

    def __init__(self, canList):
        self.canList = canList
        self.signlList = []

    def GetSignalLineNumber(self, i):
        if i < len(self.canList):
            return self.canList[i].line_number
        return -100000000

    def GetSignalValue(self, i, signalType):
        if i < len(self.canList):
            if signalType == 0:
                return (self.canList[i].can_data[1] >> 6) & 0x3
            elif signalType == 1:
                return (self.canList[i].can_data[1] >> 4) & 0x3

        return -100000000

    def ParaseTurnIndcr(self):
        self.ParseTurnIndcrByType(0)
        self.PrintSignalListToFile(output_file_name1, "===turn left light===")
        self.signlList.clear()

        self.ParseTurnIndcrByType(1)
        self.PrintSignalListToFile(output_file_name2, "===turn right light===")
        self.signlList.clear()

    def ParseTurnIndcrByType(self, type):
        signal = Signal()
        signal.start = 0
        signal.line_number = self.GetSignalLineNumber(signal.start)
        signal.value = self.GetSignalValue(signal.start, type)
        signal.num += 1

        for i in range(1, len(self.canList)):
            if self.GetSignalValue(i, type) == self.GetSignalValue(i-1, type):
                signal.num += 1
            else:
                self.signlList.append(signal)
                # new signal
                signal = Signal()
                signal.line_number = self.GetSignalLineNumber(i)
                signal.start = i
                signal.value = self.GetSignalValue(i, type)
                signal.num += 1

        if (self.GetSignalValue(i, type) == self.GetSignalValue(i-1, type)) and signal:
            self.signlList.append(signal)

    def PrintSignalListToFile(self, fileName, title):
        if not fileName:
            print("file %s cant be null"%fileName)
            return

        f = open(fileName, "w")
        f.write(title)
        f.write("\n")
        for signal in self.signlList:
            if signal.num != 9:
                f.write("line number = %d \tstart id = %d \tvalue = %d \t num = %d \tduration = %dms\n"%(signal.line_number, signal.start, signal.value, signal.num, signal.num*40))

        f.close()

    def PrintSignalList(self):
        for signal in self.signlList:
            print("start id = %d value = %d num = %d"%(signal.start, signal.value, signal.num))