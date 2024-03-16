#!/usr/bin/env python3

def main():
  f2 = open('http_req_duration.txt', "w")
  f3 = open('web_vital_cls.txt', "w")
  f4 = open('web_vital_fcp.txt', "w")
  f5 = open('web_vital_fid.txt', "w")
  f6 = open('web_vital_inp.txt', "w")
  f7 = open('web_vital_lcp.txt', "w")
  f8 = open('web_vital_ttfb.txt', "w")
  f9 = open('iteration_duration.txt', "w")

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