#!/usr/bin/env python3
import os, sys
import json
import requests

url = "http://localhost/fruits/"
p = os.listdir("supplier-data/descriptions/")
for file in p:
  if file.endswith("txt"):
    with open("supplier-data/descriptions/" + file, 'r') as f:
      fruit_name = os.path.splitext(file)[0]
      line = f.read()
      data = line.split("\n")
      fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
      res = requests.post(url, json=fruit_dic)
      res.raise_for_status()
      print(res.status_code)