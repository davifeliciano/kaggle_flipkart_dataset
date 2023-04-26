import re
import json
import pandas as pd

root_category_re = re.compile(r"\[\"(.*?)[(?:\s+(?:>>)*)|(?:\")]")


def parse_root_category(category_tree: str) -> str:
    re_match = root_category_re.match(category_tree)
    return re_match.group(1)


def parse_image_list(image_list: str) -> list | None:
    try:
        return json.loads(image_list)
    except json.decoder.JSONDecodeError:
        return []


df = pd.read_csv(
    "flipkart_dataset.csv",
    converters={
        "product_category_tree": parse_root_category,
        "image": parse_image_list,
    },
    index_col=None,
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

df.rename(columns={"product_category_tree": "category"}, inplace=True)
df.to_json("filtered_flipkart_dataset.json", orient="records")
