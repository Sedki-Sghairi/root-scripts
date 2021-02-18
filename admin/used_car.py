#!/usr/bin/env python3

import json
import locale
import sys
import emails
import os
import reports
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie



def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximum
  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sale = {"total_sales": 0}
  car_year_count = {}
  for item in data:
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: handles max sales
    if item["total_sales"] > max_sale["total_sales"]:
      max_sale = item
    # TODO: handles most popular car_year
    if item["car"]["car_year"] not in car_year_count:
      car_year_count[item["car"]["car_year"]] = 0
      car_year_count[item["car"]["car_year"]] += item["total_sales"]
    else:
      car_year_count[item["car"]["car_year"]] += item["total_sales"]

  best_year, best_year_sales = max(car_year_count.items(), key=lambda x:x[1])

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"])

  ]
  max_sale_format = "The {} generated the most sales: {}".format(format_car(max_sale["car"]), max_sale["total_sales"])
  best_year_format = "The most popular year was {} with {} sales.".format(best_year, best_year_sales)

  summary.append(max_sale_format)
  summary.append(best_year_format)
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data




def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  table = cars_dict_to_table(data)
  table_raw = table[1:]
  table_sorted = sorted(table_raw, key=lambda x:x[3], reverse=True)
  table_sorted.insert(0, ["ID", "Car", "Price", "Total Sales"])
  # pie = pie_chart(data)

  print(summary)
  report_summary = summary[0] + "<br/>" + summary[1] + "<br/>" + summary[2] + "<br/>"
  # TODO: turn this into a PDF report
  reports.generate("/tmp/cars.pdf", "Title", report_summary , table_sorted) #Sorting the table by Sales
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = summary[0] + "\n" + summary[1] + "\n" + summary[2] + "\n"
  package = "/tmp/cars.pdf"

  message = emails.generate(sender, receiver, subject, body, package)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)