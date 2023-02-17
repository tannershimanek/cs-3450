# Subject
class LocalStock:
    """Represents what is being observered."""
   
    def __init__(self):
        """Create an empty observer list."""
        self._observers = []

    def notify(self, modifier=None):
        """Alter the observers."""
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
    
    def attach(self, observer):
        """If the observer is not in the list,
        append it into the list."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detatch(self, observer):
        """Remove the observer from the list."""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


# concrete subject
class Data(LocalStock):
    """Monitor the object."""
    def __init__(self, name=''):
        LocalStock.__init__(self)
        self.name = name
        self._data = []

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


# helper class for parsing data
class IndividualStockData:
    '''Represents the stock data for each company.'''
    def __init__(self, str):
        self.data = str.strip().split(' ')
        self.company_name = ' '.join(self.data[:-9])
        self.ticker_symbol = self.data[-9]
        self.current_price = self.data[-8]
        self.dollar_change = self.data[-7]
        self.percent_change = self.data[-5]
        self.ytd_percent_change = self.data[-4]
        self.fifty_two_week_high = self.data[-3]
        self.fifty_two_week_low = self.data[-2]
        self.p_e_ratio = self.data[-1]
    
    def stock_data(self):
        return ' '.join([
            self.company_name,
            self.ticker_symbol,
            self.current_price,
            self.dollar_change,
            self.percent_change,
            self.ytd_percent_change,
            self.fifty_two_week_high,
            self.fifty_two_week_low,
            self.p_e_ratio])
    
    def __repr__(self):
        repr = ' '.join([
            self.company_name,
            self.ticker_symbol,
            self.current_price,
            self.dollar_change,
            self.percent_change,
            self.ytd_percent_change,
            self.fifty_two_week_high,
            self.fifty_two_week_low,
            self.p_e_ratio])
        return f'{repr}'


# observers
class Average:
    def __init__(self):
        self.date = ''
        self.average = 0
    
    def __calc_average(self, data):
        sum_of_stocks = 0
        num_of_stocks = 0
        for stock in data:
            stock_data = IndividualStockData(stock)
            sum_of_stocks += float(stock_data.current_price)
            num_of_stocks += 1
        return sum_of_stocks / num_of_stocks

    def generate_report(self):
        f = open('./output/Average.dat', 'a')
        f.write(f'{self.date} Average price: {self.average}\n')
        f.close()

    def update(self, subject):
        self.date = ' '.join(subject.data[0].strip().split(' ')[2:])
        self.average = self.__calc_average(subject.data[1:])
        self.generate_report()

    def __repr__(self):
        return'average observer'


class Selections:
    def __init__(self, selections):
        self.date = ''
        self.selections = selections
        self.stock_data = ''

    def __selection_data(self, data):
        selections = ''
        for stock in data:
            stock_data = IndividualStockData(stock)
            symbol = stock_data.ticker_symbol
            if symbol in self.selections:
                selections += f'{stock_data.stock_data()}\n'
        return selections

    def generate_report(self):
        f = open('./output/Selections.dat', 'a')
        f.write(f'{self.date}\n{self.stock_data}\n')
        f.close()

    def update(self, subject):
        self.date = subject.data[0].strip()
        self.stock_data = self.__selection_data(subject.data[1:])
        self.generate_report()

    def __repr__(self):
        print('selections observer')


class HighLow:
    def __init__(self):
        self.date = ''
        self.highlow_data = ''

    def __highlow_data(self, data):
        within_one = ''
        for stock in data:
            stock_data = IndividualStockData(stock)
            close_price = float(stock_data.current_price)
            fifty_two_week_high = stock_data.fifty_two_week_high
            fifty_two_week_low = stock_data.fifty_two_week_low
            x_high = float(fifty_two_week_high)
            x_low = float(fifty_two_week_low)
            h_percentage = abs((close_price - x_high) / close_price) <= 0.010
            l_percentage = abs((close_price - x_low) / close_price) <= 0.010
            if h_percentage or l_percentage:
                symbol = stock_data.ticker_symbol
                dat = f'{symbol}: {close_price}, {fifty_two_week_high}, {fifty_two_week_low}'
                within_one += f'{dat}\n'
        return within_one

    def generate_report(self):
        f = open('./output/HighLow.dat', 'a')
        f.write(f'{self.date}\n{self.highlow_data}\n')
        f.close()

    def update(self, subject):
        self.date = subject.data[0].strip()
        self.highlow_data = self.__highlow_data(subject.data[1:])
        self.generate_report()
    
    def __str__(self):
        print('highlow observer')
