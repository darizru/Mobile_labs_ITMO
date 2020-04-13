class Tariffication:
    free_sms_number = 5
    free_call_in_min = 5
    sms_rate = 1
    call_in_rate = 1
    call_out_rate = 4

    def __init__(self, number):
        self._id = number
        self._call_in_durations = [0]
        self._call_out_durations = [0]
        self._total_sms_number = 0

    def getId(self):
        return self._id

    def addCallOutDuration(self, call_duration):
        self._call_out_durations.append(call_duration)

    def addCallInDuration(self, call_duration):
        self._call_in_durations.append(call_duration)

    def addSmsNumber(self, sms_number):
        self._total_sms_number += sms_number

    def userTariffication(self):
        total_call_out_bill = 0
        for i in self._call_out_durations:
            total_call_out_bill += i*self.call_out_rate

        total_call_in_bill = 0
        for i in self._call_in_durations:
            if self.free_call_in_min >= i:
                continue
            else:
                total_call_in_bill += (i-self.free_call_in_min)*self.call_in_rate

        if self.free_sms_number >= self._total_sms_number:
            total_sms_bill = 0
        else:
            total_sms_bill = (self._total_sms_number - self.free_sms_number) * self.sms_rate

        print("Исходящие:", round(total_call_out_bill, 2), "руб.")
        print("Входящие:", round(total_call_in_bill, 2), "руб.")
        print("СМС:", total_sms_bill, "руб.")
        print("Итого:", total_sms_bill + total_call_out_bill + total_call_in_bill, "руб.")
