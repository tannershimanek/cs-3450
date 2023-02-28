import factory


def main():
    producer = factory.FactoryProducer()

    lowRes_factory = producer.get_factory('LowRes')
    highRes_factory = producer.get_factory('HighRes')

    lowResPrintDriver = lowRes_factory.get_driver('Document')
    lowResDisplayDriver = lowRes_factory.get_driver('Widget')
    lowResPrintDriver.print_()
    lowResDisplayDriver.draw()

    highResPrintDriver = highRes_factory.get_driver('Document')
    highResDisplayDriver = highRes_factory.get_driver('Widget')

    highResPrintDriver.print_()
    highResDisplayDriver.draw()


if __name__ == "__main__":
    main()
