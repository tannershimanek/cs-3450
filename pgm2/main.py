import Observer

def read_file(path):
    infile = open(path, 'r')
    data = infile.read()
    infile.close()
    return data


def parse_file(data):
    result = map(lambda x: 
        x.strip().split('\n'),
        data.strip().split('\n\n'))
    result = list(result)
    return result


def clear_files(paths):
    for path in paths:
        f = open(path, 'w')
        f.write('')
        f.close()


def main():
    ticker_data = read_file(TICKER_PATH)
    stock_data = parse_file(ticker_data)
    out_paths = [AVERAGE_PATH, SELECTECTIONS_PATH, HIGHLOW_PATH]
    clear_files(out_paths)
    companies = ['ALL', 'BA', 'BC', 'GBEL', 'KFT', 'MCD', 'TR', 'WAG']

    obj = Observer.Data('Local Stocks')

    obj.attach(Observer.Average())
    obj.attach(Observer.HighLow())
    obj.attach(Observer.Selections(companies))

    # update data
    for day_of_data in stock_data:
        obj.data = day_of_data

    print('[3] reports generated at ./output/')


if __name__ == '__main__':
    TICKER_PATH = './data/Ticker.dat'
    AVERAGE_PATH = './output/Average.dat'
    SELECTECTIONS_PATH = './output/Selections.dat'
    HIGHLOW_PATH = './output/HighLow.dat'
    main()
