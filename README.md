# World-soccer-data-feed
Soccer matches around the world 24/7 in real-time

This is a unique live data stream on Github providing a simple yet rich source of all soccer matches around the world 24/7 in real-time.

- What makes it unique compared to other datasets?

- Unlike “Churn rate” datasets you do not have to wait months to evaluate your predictions; simply check the match’s outcome in a couple of hours

- you can use your predictions/analysis for your own benefit instead of spending your time and resources on helping a company maximizing its profit

- A Five year old laptop can do the calculations and you do not need high-end GPUs

- You can’t get accurate results on all samples? Do not worry, just filter out the hard ones (e.g. ignore international friendly) and simply choose the ones you are sure of.

- Need help from human experts for each sample? Every sample comes with at least two opinions from experts

- You wish you could add your complementary data? Just contact us and we will try to facilitate it.

- Simply train your algorithm on the first version of training dataset of approximately 11.5k matches and predict the data provided in the following data feed.

# How to fetch the data stream

The CSV file is updated every 30 minutes at minutes 20’ and 50’ of every hour. I kindly request not to download it more than twice per hour as it incurs additional cost.

Simply run the **"fetch_live_data.ipynb"** to get the csv on your device in python or do as below,

You may download the csv data file from the following link from Amazon S3 server by changing the FOLDER_NAME as below,

https://s3.amazonaws.com/FOLDER_NAME/amasters.csv

*. Substitute the FOLDER_NAME with "analyst-masters"

# Please refer to [wiki](https://github.com/Analystmasters/World-soccer-data-feed/wiki) for more information
