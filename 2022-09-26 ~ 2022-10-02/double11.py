from datetime import datetime, timedelta


class ChannelStat:

    @property
    def begin_time(self):
        now = datetime.now() + timedelta(hours=8)
        if now.hour > 20:
            begin_time = datetime(now.year, now.month, now.day, 20).timestamp()
        else:
            begin_time = datetime(now.year, now.month, now.day, 20).timestamp() - 86400
        return begin_time

    def __init__(self):
        self.stat_time_list = [(self.begin_time - 3600, self.begin_time)] + [
            (self.begin_time, self.begin_time + 60)] + [(self.begin_time + i, self.begin_time + i + 1800) for i in
                                                        range(0, 7200, 1800)] + [
                                  (self.begin_time + i, self.begin_time + i + 3600) for i in
                                  range(7200, 86400, 3600)]
        self.delay = 120

    def get_stat_time_list(self):
        now = datetime.now()
        max_stat_time = self.stat_time_list[0][1] - 60
        for k in range(0, 40):
            pivot = datetime(2022, 9, 29, 20, k, 30).timestamp()
            stated_time_list = []
            to_stat = []
            for i in self.stat_time_list:
                if max_stat_time < i[1] <= pivot - self.delay:
                    to_stat.append(i)
                elif max_stat_time == i[1] and max_stat_time >= pivot - 600:
                    to_stat.append(i)
                elif i[1] > pivot - self.delay:
                    break
            if to_stat:
                max_stat_time = to_stat[-1][1]
            print('max_stat', datetime.fromtimestamp(max_stat_time))
            print('pivot', datetime.fromtimestamp(pivot))
            print(to_stat)


if __name__ == '__main__':
    s = ChannelStat()
    l = s.get_stat_time_list()

