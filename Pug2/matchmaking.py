def calculate_average(team: list):
    avg = 0
    for i in team:
        avg += i[1].ratings.highest_sr
    return round(float(avg) / len(team))


class MatchMaking:
    def __init__(self, ow_members, members):
        self.members = members
        tup = []
        for i in range(0, len(members)):
            tup.append((members[i], ow_members[i]))
        tup.sort(key=lambda x: x[1].ratings.highest_sr)
        self.tup = tuple(tup)
        self.red = [self.tup[0]]
        self.blue = [self.tup[1]]
        self.red_cap = self.red[0]
        self.blue_cap = self.blue[0]
        self.red_avg = calculate_average(self.red)
        self.blue_avg = calculate_average(self.blue)
