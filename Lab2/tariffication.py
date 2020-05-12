class Tariffication:
    tarif_rate = 0.5

    def __init__(self, ip):
        self._ip = ip
        self._traffic_in = {}
        self._traffic_out = {}
        self._time_val = {}

    def getId(self):
        return self._ip

    def addTrafficOut(self, time, bytes):
        if time in self._traffic_out.keys():
            self._traffic_out[time].append(bytes)
        else:
            self._traffic_out[time] = [bytes]

    def addTrafficIn(self, time, bytes):
        if time in self._traffic_in.keys():
            self._traffic_in[time].append(bytes)
        else:
            self._traffic_in[time] = [bytes]

    def addTimeVal(self, time, bytes):

        time = time.split(" ")[1]
        if time in self._time_val.keys():
            self._time_val[time] = self._time_val[time] + bytes
        else:
            self._time_val[time] = bytes

    def userTariffication(self):

        k = self.tarif_rate
        total_traffic_out = 0
        for i in self._traffic_out.keys():
            for j in self._traffic_out[i]:
                total_traffic_out += j

        total_traffic_in = 0
        for i in self._traffic_in.keys():
            for j in self._traffic_in[i]:
                total_traffic_in += j

        total_traffic = total_traffic_out + total_traffic_in
        total_traffic_bill = 0

        k = self.tarif_rate
        while total_traffic >= 500*1000:
            total_traffic -= 500*1000
            total_traffic_bill += 500*k
            k += 0.5

        total_traffic_bill += (total_traffic/1000)*k

        print("Объем трафика:", round((total_traffic_out + total_traffic_in)/1000, 2), "Кб.")
        print("Итого:", round(total_traffic_bill, 2), "руб.")

