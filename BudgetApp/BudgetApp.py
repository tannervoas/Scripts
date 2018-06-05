import sys

class date:
    def __init__(self,date):
        date = date.split('/')
        self.m = int(date[0])
        self.d = int(date[1])
        self.y = int(date[2])
        self.record = []
        self.total = 0
        self.amount = 0

    def add(self,amount,des):
        amount = float(amount)
        if amount >= 0:
            return
        if len(self.record) == 0:
            self.record += [[amount,des]]
        elif self.record[-1][0] <= amount:
            self.record += [[amount,des]]
        else:
            i = 0
            while self.record[i][0] < amount:
                i += 1
            self.record = self.record[:i] + [[amount,des]] + self.record[i:]
        self.total += amount
        self.amount += 1

    def __repr__(self):
        st = ''
        if self.amount > 0:
            st = '{0:0>2}/{1:0>2}/{2:0>4}: TOTAL = {3:9.2f} | QUANTITY = {4:4} | AVERAGE = {5:9.2f}'.format(self.m,self.d,self.y,self.total,self.amount,self.total/self.amount)

        return st

class setting:
    def __init__(self,source):
        pass

class record:
    def __init__(self,source):
        self.dates = {}
        for line in source:
            line = clean(line.strip(),['"','*']).split(',')
            if not line[0] in self.dates:
                self.dates[line[0]] = date(line[0])
            self.dates[line[0]].add(line[1],line[4])
        dates = list(self.dates.keys())
        self.keys = dateOrder(dates)
        self.organize()

    def organize(self):
        self.timeline = {}
        for key in self.keys:
            date = key.split('/')
            if not date[2] in self.timeline:
                self.timeline[date[2]] = {}
            if not date[0] in self.timeline[date[2]]:
                self.timeline[date[2]][date[0]] = {}
            if not date[1] in self.timeline[date[2]][date[0]]:
                self.timeline[date[2]][date[0]][date[1]] = []
            self.timeline[date[2]][date[0]][date[1]] += [self.dates[key]]


    def __repr__(self):
        st = ''
        total = 0
        amount = 0
        years = list(self.timeline.keys())
        years.sort()
        lead = 0
        st_y = ''
        for year in years:
            y_total = 0
            y_amount = 0
            st_y += '- {0:0>4}'.format(year)
            months = list(self.timeline[year].keys())
            months.sort()
            st_m = ''
            for month in months:
                m_total = 0
                m_amount = 0
                st_m += '   - {0:0>2}'.format(month)
                days = list(self.timeline[year][month].keys())
                days.sort()
                st_d = ''
                for day in days:
                    tmp = '      - {0}\n'.format(self.timeline[year][month][day][0])
                    m_total += self.timeline[year][month][day][0].total
                    m_amount += self.timeline[year][month][day][0].amount
                    if len(tmp) > lead:
                        lead = len(tmp)
                    if len(tmp) > 9:
                        st_d += tmp
                if m_amount > 0:
                    st_m += ':........... TOTAL = {0:.>9.2f} | QUANTITY = {1:.>4} | AVERAGE = {2:.>9.2f}\n'.format(m_total,m_amount,m_total/m_amount)
                else:
                    st_m += '\n'
                st_m += st_d
                y_total += m_total
                y_amount += m_amount
            if y_amount > 0:
                st_y += ':............ TOTAL = {0:.>9.2f} | QUANTITY = {1:.>4} | AVERAGE = {2:.>9.2f}\n'.format(y_total,y_amount,y_total/y_amount)
            else:
                st_y += '\n'
            st_y += st_m
            total += y_total
            amount += y_amount
        if amount > 0:
            st += '................... TOTAL = {0:.>9.2f} | QUANTITY = {1:.>4} | AVERAGE = {2:.>9.2f}\n'.format(total,amount,total/amount)
        st += st_y
        lead = lead - 1
        return '-'*lead + '\n' + st + '-'*lead

def dateOrder(dates):
    new = []
    for date in dates:
        if len(new) == 0:
            new += [date]
        elif dateComp(new[-1],date) <= 0:
            new += [date]
        else:
            i = 0
            while dateComp(new[i],date) == -1:
                i += 1
            new = new[:i] + [date] + new[i:]
    return new

def dateComp(ld,rd):
    ld = ld.split('/')
    rd = rd.split('/')
    if int(ld[2]) < int(rd[2]):
        return -1
    elif int(ld[2]) > int(rd[2]):
        return 1
    else:
        if int(ld[0]) < int(rd[0]):
            return -1
        elif int(ld[0]) > int(rd[0]):
            return 1
        else:
            if int(ld[1]) < int(rd[1]):
                return -1
            elif int(ld[1]) > int(rd[1]):
                return 1
            else:
                return 0

def clean(line,rem):
    if type(rem) == str:
        rem = [rem]
    cleaned = ''
    for char in line:
        if not char in rem:
            cleaned += char
    return cleaned

def main():
    argv = sys.argv[1:]
    settings = open('settings.csv')
    checking = open('checking.csv')
    savings  = open('savings.csv')
    setting(settings)
    ch = record(checking)
    sa = record(savings)
    print(ch)
    print(sa)


if __name__ == '__main__':
    main()
