#!/bin/bash

source .env
mongoimport --uri=$DATABASE_URL \
            --collection="products" \
            --file="filtered_flipkart_dataset.json" \
            --jsonArray