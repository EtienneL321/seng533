#!/usr/bin/env python3

import argparse
import re
import os

def parse_args():
  parser = argparse.ArgumentParser(
      prog='parse results',
  )
  parser.add_argument('f1', help='file to parse')
  return parser.parse_args()

def main():
  args = parse_args()

  f1 = open(args.f1, "r")
  
  f2 = open('textfiles/http_req_duration.txt', "a")
  f3 = open('textfiles/web_vital_cls.txt', "a")
  f4 = open('textfiles/web_vital_fcp.txt', "a")
  f5 = open('textfiles/web_vital_fid.txt', "a")
  f6 = open('textfiles/web_vital_inp.txt', "a")
  f7 = open('textfiles/web_vital_lcp.txt', "a")
  f8 = open('textfiles/web_vital_ttfb.txt', "a")
  f9 = open('textfiles/iteration_duration.txt', "a")

  header = f1.read(600)
  f2.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f3.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f4.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f5.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f6.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f7.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f8.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")
  f9.write("VUs: " + header.split(":")[4].split()[3] + " and Iterations: " + header.split(":")[6].split()[0] + " -->  ")

  while block := f1.read(4096):
    if block.find("userAddedSuccessfully"):
      break

  data = block.split('browser_data_received')[1]
  if block := f1.read(4096):
    data += block

  measured_data = data.split(":")

  # print(measured_data)

  # Get http_req_duration
  http_req_duration = measured_data[3]
  # Get only number with two sig digs
  # avg = re.findall(r'(\d+\.?\d+?\d+?)', http_req_duration.split()[0])
  # min = re.findall(r'(\d+\.?\d+?\d+?)', http_req_duration.split()[1])
  # med = re.findall(r'(\d+\.?\d+?\d+?)', http_req_duration.split()[2])
  # max = re.findall(r'(\d+\.?\d+?\d+?)', http_req_duration.split()[3])

  split = http_req_duration.split()
  f2.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_cls
  web_vital_cls = measured_data[5]
  split = web_vital_cls.split()
  f3.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_fcp
  web_vital_fcp = measured_data[6]
  split = web_vital_fcp.split()
  f4.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_fid
  web_vital_fid = measured_data[7]
  split = web_vital_fid.split()
  f5.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_inp
  web_vital_inp = measured_data[8]
  split = web_vital_inp.split()
  f6.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_lcp
  web_vital_lcp = measured_data[9]
  split = web_vital_lcp.split()
  f7.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get web_vital_ttfb
  web_vital_ttfb = measured_data[10]
  split = web_vital_ttfb.split()
  f8.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")

  # Get iteration_duration
  iteration_duration = measured_data[14]
  split = iteration_duration.split()
  f9.write(split[0] + " " + split[1] + " " + split[2] + " " + split[3] + "\n")


  f1.close()
  f2.close()
  f3.close()
  f4.close()
  f5.close()
  f6.close()
  f7.close()
  f8.close()
  f9.close()


if __name__ == "__main__":
  main()