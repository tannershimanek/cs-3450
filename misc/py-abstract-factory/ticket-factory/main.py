from factory import FactoryProducer


def main():
    producer = FactoryProducer()
    jira_factory = producer.get_factory('jira')
    snow_factory = producer.get_factory('snow')

    print(snow_factory)
    jira_incident = jira_factory.create_ticket('incident')
    jira_problem = jira_factory.create_ticket('problem')
    snow_incident = snow_factory.create_ticket('incident')
    print(jira_incident.info())


if __name__ == "__main__":
    main()


# LowResDisplayDriver
# HighResDisplayDriver