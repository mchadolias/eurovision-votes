# TODO: Create several functions to apply different cuts to the data such as:
# # 1. Big 5
# # 2. Nordic countries
# # 3. Baltic countries
# # 4. Southern countries
# # 5. Balcan countries


def filter_big_5(df):
    """
    Filter the DataFrame for the Big 5 countries: France, Germany, Italy, Spain, and the United Kingdom.
    """
    big_5_countries = ["France", "Germany", "Italy", "Spain", "United Kingdom"]
    return df[df["to_country"].isin(big_5_countries)]


def filter_nordic_countries(df):
    """
    Filter the DataFrame for Nordic countries: Denmark, Finland, Iceland, Norway, and Sweden.
    """
    nordic_countries = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
    return df[df["to_country"].isin(nordic_countries)]


def filter_baltic_countries(df):
    """
    Filter the DataFrame for Baltic countries: Estonia, Latvia, and Lithuania.
    """
    baltic_countries = ["Estonia", "Latvia", "Lithuania"]
    return df[df["to_country"].isin(baltic_countries)]


def filter_southern_countries(df):
    """
    Filter the DataFrame for Southern European countries: Greece, Italy, Portugal, and Spain.
    """
    southern_countries = ["Greece", "Italy", "Portugal", "Spain"]
    return df[df["to_country"].isin(southern_countries)]


def filter_balkan_countries(df):
    """
    Filter the DataFrame for Balkan countries: Albania, Bosnia and Herzegovina, Bulgaria, Croatia, Kosovo, Montenegro, North Macedonia, Romania, Serbia, Slovenia, Greece, and Turkey.
    """

    balkan_countries = [
        "Albania",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Kosovo",
        "Montenegro",
        "North Macedonia",
        "Romania",
        "Serbia",
        "Slovenia",
        "Greece",
        "Turkey",
    ]
    return df[df["to_country"].isin(balkan_countries)]
