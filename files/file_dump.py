import json
from csv import DictWriter


def csv_dump(data: dict):
    """
    Gets zillow data as parameters and Creates a csv file

    args: json/dict object

    returns None
    """

    if not isinstance(data, dict):
        raise TypeError("data should be dictionary. " + str(type(data)) + " given")

    location = data.get('location', "")
    with open('files/csv/zillowInsight-' + location + '.csv', 'w') as f:
        csv_writer = DictWriter(f, fieldnames=['location', 'url', 'zillow_value', 'one_year_change', 'one_year_forcast',
                                               'market_temperature', 'price_sqft', 'median_listing_price',
                                               'median_sale_price', 'avg-days_on_market', 'negative_equity',
                                               'delinquency', 'rent_list_price', 'rent_sqft'])
        csv_writer.writeheader()
        csv_writer.writerow(data)
    print("created file : " + "zillowInsight-" + location + ".csv")


def json_dump(data: dict):
    """
    Gets Zillow data as parameter and creates a json file

    args: dictionary object

    returns : None
    """

    if not isinstance(data, dict):
        raise TypeError("data should be dictionary. " + str(type(data)) + " given")

    json_object = json.dumps(data, indent=4)
    location = data["location"]

    with open("files/json/zillowInsight-" + location + ".json", "w") as outfile:
        outfile.write(json_object)

    print("created file : " + "zillowInsight-" + location + ".json")


if __name__ == '__main__':
    print("You are trying to run a module.")
    print("Please run main.py or read README.md")
