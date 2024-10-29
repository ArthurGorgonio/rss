#  RSS
This repository scans urls (rss-feeds) to find some interesting news to the user

[toc]

## Installation

In this repository, we use Python 3.7+. 


```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

After this you must create a file called `urls.txt` with the links of the feeds that you are interested in.

## Usage

In the virtual environment (previous created) and with the `urls.txt` file created, you just run the following command to get all news that are posted or updated in time interval below a day

```sh
$ python main.py
```
