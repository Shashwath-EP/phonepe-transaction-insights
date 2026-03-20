import os
import json
import pandas as pd

BASE_PATH = "data/pulse/data"


def get_transaction_df():
    path = os.path.join(BASE_PATH, "aggregated", "transaction", "country", "india", "state")
    data = []

    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):

                with open(os.path.join(path, state, year, file)) as f:
                    content = json.load(f)

                    for item in content["data"]["transactionData"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.strip(".json")),
                            "transaction_type": item["name"],
                            "count": item["paymentInstruments"][0]["count"],
                            "amount": item["paymentInstruments"][0]["amount"]
                        })

    return pd.DataFrame(data)


def get_user_df():
    path = os.path.join(BASE_PATH, "aggregated", "user", "country", "india", "state")
    data = []

    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):

                with open(os.path.join(path, state, year, file)) as f:
                    content = json.load(f)

                    users = content.get("data", {}).get("usersByDevice")

                    if users is None:
                        continue

                    for item in users:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.strip(".json")),
                            "brand": item.get("brand"),
                            "count": item.get("count"),
                            "percentage": item.get("percentage")
                        })

    return pd.DataFrame(data)


def get_top_df():
    path = os.path.join(BASE_PATH, "top", "transaction", "country", "india", "state")
    data = []

    for state in os.listdir(path):
        for year in os.listdir(os.path.join(path, state)):
            for file in os.listdir(os.path.join(path, state, year)):

                with open(os.path.join(path, state, year, file)) as f:
                    content = json.load(f)

                    for item in content["data"]["districts"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.strip(".json")),
                            "district": item["entityName"],
                            "count": item["metric"]["count"],
                            "amount": item["metric"]["amount"]
                        })

    return pd.DataFrame(data)