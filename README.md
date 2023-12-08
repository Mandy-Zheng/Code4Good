# Code4Good


# Requests 

Requests is a Python library that allows users to send and handle HTTP requests to specific websites. Our matching algorithm uses this Python library to send an HTTP request to a website containing zip code data for the United States. This process allows it to retrieve relevant zip code information, specifically latitude and longitude, for distance calculations performed by another Python library called Geopy.

## Installation 

To use Requests, follow these steps: 

1. Make sure you have Python and pip installed on your system. You can download them from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Run the following command in your terminal: 
```bash
pip install requests
```


# Geopy

Geopy is a Python library that provides easy access to geographical information. This Python library allows you to perform geocoding (finding the coordinates of addresses) and distance calculations. Our matching algorithm uses it to calculate the distance (in miles) between zip codes based on their latitudes and longtidues.

## Installation

To use Geopy, follow these steps to install the required packages.

1. Make sure you have Python and pip installed on your system. You can download them from the official Python website: [Python Downloads](https://www.python.org/downloads/)

2. Run the following command in your terminal:

```bash
pip install geopy
```


