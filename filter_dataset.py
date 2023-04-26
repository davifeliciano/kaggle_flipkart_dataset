import re
import csv
import pandas as pd

root_category_re = re.compile(r"\[\"(.*?)[(?:\s+(?:>>)*)|(?:\")]")


def parse_root_category(category_tree: str) -> str:
    re_match = root_category_re.match(category_tree)
    return re_match.group(1)


df = pd.read_csv(
    "flipkart_dataset.csv",
    usecols=[
        "product_name",
        "product_category_tree",
        "retail_price",
        "discounted_price",
        "image",
        "description",
        "brand",
    ],
)

product_category = df.loc[:, "product_category_tree"]
product_root_category = product_category.map(parse_root_category)
column_to_insert = 1 + df.columns.get_loc("product_category_tree")
df.insert(column_to_insert, "product_root_category", product_root_category)
df.to_csv("filtered_flipkart_dataset.csv", index=False, quoting=csv.QUOTE_ALL)
