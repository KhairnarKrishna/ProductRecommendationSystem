from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


# load data from csv using pandas
def load_data():
    df = pd.read_csv("./scripts/datasets/flipkart_laptop_cleaned_data.csv")
    data = []
    for l in range(len(df)):
        data.append(['/static/images/laptop.jpg', df.iloc[l]["Product"], df.iloc[l]["Price"], 'A16 Bionic Chip', '8 GB RAM', '512 GB SSD', 'NVIDIA GeForce RTX 2040', '13.6 Inch (2560 x 1664 Pixel)', '90 Hz refresh rate', 'Mac OS', 94])
    return data


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    data = load_data()
    # print(data)

    data = [['/static/images/laptop.jpg', 'MackBook Air 3', 200000, 'A16 Bionic Chip', '8 GB RAM', '512 GB SSD', 'NVIDIA GeForce RTX 2040', '13.6 Inch (2560 x 1664 Pixel)', '90 Hz refresh rate', 'Mac OS', 94],
            ['/static/images/hp-laptop.jpg', 'HP Elitebook Pro', 110000, 'Intel Core i5 12gen', '16 GB RAM', '512 GB SSD', 'Intel Integrated Iris Xe', '14 Inch (1920 x 1080 Pixels)', '60 Hz refresh rate', 'Windows 11', 72],
            ['/static/images/msi-laptop.jpeg', 'MSI Katana', 80000, 'AMD Ryzen 6700H', '16 GB RAM', '1 TB SSD', 'AMD Radeon AMD', '15.6 Inch (1920 x 1080 Pixels)', '144 Hz refresh rate', 'Windows 11', 80],
            ['/static/images/acer-laptop.jpg', 'ACER Aspire 7', 45000, 'Intel Core i5 11gen', '16 GB RAM', '512 GB SSD', 'NA', '15.6 Inch (1920 x 1080 Pixels)', '120 Hz refresh rate', 'Windows 11', 88],
            ['/static/images/lenevo-laptop.jpg', 'LENOVO Notebook 5', 67000, 'AMD Ryzen 4500P', '8 GB RAM', '1 TB HDD', 'NVIDIA GTX MX400', '15.6 Inch (1920 x 1080 Pixels)', '60 Hz refresh rate', 'DOS', 54],
            ['/static/images/asus-laptop.jpg', 'ASUS ROG Zephyrus', 140000, 'AMD Ryzen 7600H', '16 GB RAM', '512 GB SSD', 'NVIDIA GeForce RTX 3060', '14 Inch (1920 x 1080 Pixels)', '144 Hz refresh rate', 'Windows 11', 89],
            # {'7': ['MackBook Air 3']},
            # {'8': ['MackBook Air 3']}
            ]
    return render_template('layout.html', data=data)


@app.template_filter()
def numFormat(value):
    """
        Custom JINJA2 filter for adding "," seperator to numeric values.
    """
    return format(int(value), ',d')


if __name__ == '__main__':
    app.run(debug=True)
