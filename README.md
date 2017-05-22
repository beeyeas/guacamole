# guacamole
Python flask application for simple REST API exposing host metrics

# gucomole - a simple python flask REST API monitoring server
## Author : Bharath - beeyeas@gmail.com

## How to setup this (python Flask) application steps
### 1. Install python , pip

### 2. Install Flask ( http://flask.pocoo.org/docs/0.10/installation/ )
``` 
sudo pip install Flask
```
### 3. Install virtual env
``` 
sudo easy_install virtualenv
```
### 4. Configure virtual env
``` 
virtualenv env
``` 
### 5. Activate virtual env
```
. venv/bin/activate
```
### 6. Install psutil
``` 
pip install psutil
```
### 7. Run gucomole service to expose REST APIs
``` 
sudo python guacomole.py 
```

#Example
```
sudo python guacomole.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [19/May/2017 16:28:15] "GET /v1/network HTTP/1.1" 200 -
```

## From another terminal curl the REST APIs
```
curl http://127.0.0.1:5000/v1/network
```

#REST APIs


##
```
/v1/cpu
curl http://127.0.0.1:5000/v1/cpu
{
  "cpu_count": 8, 
  "cpu_freq": {
    "current": 2200, 
    "max": 2200, 
    "min": 2200
  }, 
  "cpu_stats": {
    "ctx_switches": 462210, 
    "interrupts": 1049941, 
    "soft_interrupts": 1671485213, 
    "syscalls": 835373
  }, 
  "cpu_times": {
    "idle": 9160542.37, 
    "nice": 0.0, 
    "system": 127796.7, 
    "user": 216585.51
  }
}
```


##
``` 
/v1/network

{
  "net_connections": [
    [
      3, 
      2, 
      1, 
      [
        "127.0.0.1", 
        58959
      ], 
      [
        "127.0.0.1", 
        5000
      ], 
      "ESTABLISHED", 
      96827
    ], 
    [
      3, 
      2, 
      1, 
      [
        "127.0.0.1", 
        5000
      ], 
      [], 
      "LISTEN", 
      96668
    ], 
    [
      4, 
      2, 
      1, 
      [
        "127.0.0.1", 
        5000
      ], 
      [
        "127.0.0.1", 
        58959
      ], 
      "ESTABLISHED", 
      96668
    ], 
    [
      3, 
      2, 
      2, 
      [
        "0.0.0.0", 
        137
      ], 
      [], 
      "NONE", 
      92546
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        138
      ], 
      [], 
      "NONE", 
      92546
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      92500
    ], 
    [
      50, 
      2, 
      1, 
      [
        "127.0.0.1", 
        30666
      ], 
      [], 
      "LISTEN", 
      79175
    ], 
    [
      62, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58628
      ], 
      [
        "52.0.252.204", 
        443
      ], 
      "ESTABLISHED", 
      79175
    ], 
    [
      100, 
      2, 
      1, 
      [
        "127.0.0.1", 
        45112
      ], 
      [], 
      "LISTEN", 
      79175
    ], 
    [
      13, 
      30, 
      1, 
      [
        "::", 
        0
      ], 
      [], 
      "CLOSE", 
      17655
    ], 
    [
      19, 
      2, 
      1, 
      [
        "127.0.0.1", 
        64912
      ], 
      [
        "127.0.0.1", 
        55282
      ], 
      "ESTABLISHED", 
      17655
    ], 
    [
      23, 
      30, 
      1, 
      [
        "::", 
        0
      ], 
      [], 
      "CLOSE", 
      17654
    ], 
    [
      28, 
      30, 
      1, 
      [
        "::", 
        64908
      ], 
      [], 
      "LISTEN", 
      17604
    ], 
    [
      32, 
      30, 
      1, 
      [
        "::", 
        55282
      ], 
      [], 
      "LISTEN", 
      17604
    ], 
    [
      36, 
      30, 
      1, 
      [
        "::127.0.0.1", 
        55282
      ], 
      [
        "::127.0.0.1", 
        64912
      ], 
      "ESTABLISHED", 
      17604
    ], 
    [
      64, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58635
      ], 
      [
        "68.140.248.50", 
        80
      ], 
      "CLOSE", 
      20697
    ], 
    [
      65, 
      2, 
      1, 
      [
        "10.69.34.106", 
        57571
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      20697
    ], 
    [
      69, 
      2, 
      1, 
      [
        "10.69.34.106", 
        57571
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      20697
    ], 
    [
      26, 
      2, 
      1, 
      [
        "10.69.0.210", 
        61130
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      22228
    ], 
    [
      30, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58885
      ], 
      [
        "153.114.128.62", 
        443
      ], 
      "CLOSE", 
      22228
    ], 
    [
      31, 
      2, 
      1, 
      [
        "10.69.0.210", 
        61131
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      22228
    ], 
    [
      32, 
      2, 
      1, 
      [
        "10.69.0.210", 
        61130
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      22228
    ], 
    [
      34, 
      2, 
      1, 
      [
        "10.69.0.210", 
        61131
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      22228
    ], 
    [
      42, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58786
      ], 
      [
        "153.114.128.62", 
        443
      ], 
      "ESTABLISHED", 
      22228
    ], 
    [
      28, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      94069
    ], 
    [
      17, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      31, 
      30, 
      1, 
      [
        "::", 
        62319
      ], 
      [], 
      "LISTEN", 
      69806
    ], 
    [
      32, 
      2, 
      1, 
      [
        "0.0.0.0", 
        62319
      ], 
      [], 
      "LISTEN", 
      69806
    ], 
    [
      61, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      62, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      63, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      64, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      65, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      66, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      68, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      72, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      73, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      74, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      75, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      76, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      77, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      78, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      79, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      80, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      81, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      69806
    ], 
    [
      81, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      21410
    ], 
    [
      95, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58892
      ], 
      [
        "192.30.255.112", 
        443
      ], 
      "CLOSE", 
      21410
    ], 
    [
      106, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58634
      ], 
      [
        "68.140.248.50", 
        80
      ], 
      "CLOSE", 
      21410
    ], 
    [
      162, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58893
      ], 
      [
        "151.101.40.133", 
        443
      ], 
      "ESTABLISHED", 
      21410
    ], 
    [
      166, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58895
      ], 
      [
        "151.101.40.133", 
        443
      ], 
      "ESTABLISHED", 
      21410
    ], 
    [
      167, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58894
      ], 
      [
        "151.101.40.133", 
        443
      ], 
      "ESTABLISHED", 
      21410
    ], 
    [
      169, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58896
      ], 
      [
        "151.101.40.133", 
        443
      ], 
      "ESTABLISHED", 
      21410
    ], 
    [
      182, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58897
      ], 
      [
        "52.0.185.180", 
        443
      ], 
      "CLOSE", 
      21410
    ], 
    [
      190, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58898
      ], 
      [
        "192.30.253.125", 
        443
      ], 
      "ESTABLISHED", 
      21410
    ], 
    [
      193, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58899
      ], 
      [
        "192.30.255.116", 
        443
      ], 
      "CLOSE", 
      21410
    ], 
    [
      8, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59848
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      26509
    ], 
    [
      9, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59848
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      26509
    ], 
    [
      11, 
      2, 
      1, 
      [
        "10.69.2.85", 
        51627
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      4381
    ], 
    [
      13, 
      2, 
      1, 
      [
        "10.69.2.85", 
        51627
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      4381
    ], 
    [
      6, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59844
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      1497
    ], 
    [
      7, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59844
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      1497
    ], 
    [
      17, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      922
    ], 
    [
      5, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59800
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      840
    ], 
    [
      9, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59800
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      840
    ], 
    [
      6, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59905
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      833
    ], 
    [
      7, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59905
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      833
    ], 
    [
      6, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      831
    ], 
    [
      7, 
      2, 
      1, 
      [
        "10.69.67.238", 
        54989
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      830
    ], 
    [
      8, 
      2, 
      1, 
      [
        "10.69.67.238", 
        54989
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      830
    ], 
    [
      11, 
      2, 
      1, 
      [
        "10.69.67.238", 
        54998
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      830
    ], 
    [
      13, 
      2, 
      1, 
      [
        "10.69.67.238", 
        54998
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      830
    ], 
    [
      9, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59871
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      813
    ], 
    [
      10, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59871
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      813
    ], 
    [
      7, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      802
    ], 
    [
      23, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59852
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      793
    ], 
    [
      28, 
      2, 
      1, 
      [
        "10.69.16.59", 
        59852
      ], 
      [
        "153.114.156.16", 
        5150
      ], 
      "CLOSE", 
      793
    ], 
    [
      9, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      767
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      766
    ], 
    [
      5, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      766
    ], 
    [
      9, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      750
    ], 
    [
      10, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      750
    ], 
    [
      13, 
      2, 
      2, 
      [
        "0.0.0.0", 
        54617
      ], 
      [], 
      "NONE", 
      750
    ], 
    [
      15, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      750
    ], 
    [
      17, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      750
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      738
    ], 
    [
      20, 
      2, 
      2, 
      [
        "0.0.0.0", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      21, 
      30, 
      2, 
      [
        "::", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      22, 
      30, 
      2, 
      [
        "::1", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      23, 
      2, 
      2, 
      [
        "127.0.0.1", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      24, 
      30, 
      2, 
      [
        "fe80:1::1", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      25, 
      30, 
      2, 
      [
        "fe80:8::20ce:9dff:fe18:a3e1", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      27, 
      30, 
      2, 
      [
        "fe80:4::3636:3bff:fecc:7aa8", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      28, 
      2, 
      2, 
      [
        "68.140.241.16", 
        123
      ], 
      [], 
      "NONE", 
      246
    ], 
    [
      13, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      196
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      118
    ], 
    [
      5, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      118
    ], 
    [
      9, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      118
    ], 
    [
      8, 
      2, 
      2, 
      [
        "0.0.0.0", 
        5353
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      9, 
      30, 
      2, 
      [
        "::", 
        5353
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      47, 
      2, 
      2, 
      [
        "0.0.0.0", 
        56202
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      48, 
      30, 
      2, 
      [
        "::", 
        56202
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      49, 
      2, 
      2, 
      [
        "0.0.0.0", 
        53884
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      51, 
      30, 
      2, 
      [
        "::", 
        53884
      ], 
      [], 
      "NONE", 
      109
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      102
    ], 
    [
      4, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      99
    ], 
    [
      15, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58653
      ], 
      [
        "17.249.28.97", 
        5223
      ], 
      "ESTABLISHED", 
      90
    ], 
    [
      17, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58653
      ], 
      [
        "17.249.28.97", 
        5223
      ], 
      "ESTABLISHED", 
      90
    ], 
    [
      9, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58949
      ], 
      [
        "159.161.168.246", 
        389
      ], 
      "ESTABLISHED", 
      87
    ], 
    [
      14, 
      2, 
      1, 
      [
        "68.140.241.16", 
        58954
      ], 
      [
        "159.161.168.246", 
        3268
      ], 
      "ESTABLISHED", 
      87
    ], 
    [
      10, 
      30, 
      2, 
      [
        "::", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      20, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      22, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      24, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      25, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      26, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      28, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      29, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      33, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      72
    ], 
    [
      9, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      63
    ], 
    [
      10, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      63
    ], 
    [
      5, 
      2, 
      1, 
      [
        "127.0.0.1", 
        29754
      ], 
      [], 
      "LISTEN", 
      59
    ], 
    [
      5, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      53
    ], 
    [
      25, 
      2, 
      2, 
      [
        "0.0.0.0", 
        0
      ], 
      [], 
      "NONE", 
      53
    ], 
    [
      19, 
      2, 
      2, 
      [
        "0.0.0.0", 
        138
      ], 
      [], 
      "NONE", 
      1
    ], 
    [
      28, 
      2, 
      2, 
      [
        "0.0.0.0", 
        137
      ], 
      [], 
      "NONE", 
      1
    ], 
    [
      35, 
      30, 
      1, 
      [
        "::", 
        22
      ], 
      [], 
      "LISTEN", 
      1
    ], 
    [
      37, 
      2, 
      1, 
      [
        "0.0.0.0", 
        22
      ], 
      [], 
      "LISTEN", 
      1
    ], 
    [
      42, 
      30, 
      1, 
      [
        "::", 
        22
      ], 
      [], 
      "LISTEN", 
      1
    ], 
    [
      43, 
      2, 
      1, 
      [
        "0.0.0.0", 
        22
      ], 
      [], 
      "LISTEN", 
      1
    ]
  ], 
  "net_io_counters": [
    {
      "gif0": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "en7": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "en2": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "en0": "{\"bytes_sent\": 1187973157, \"bytes_recv\": 8704926663, \"packets_sent\": 6966123, \"packets_recv\": 10817797, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "en1": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "lo0": "{\"bytes_sent\": 17805633, \"bytes_recv\": 17805633, \"packets_sent\": 155874, \"packets_recv\": 155874, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "bridge0": "{\"bytes_sent\": 342, \"bytes_recv\": 0, \"packets_sent\": 1, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "p2p0": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "stf0": "{\"bytes_sent\": 0, \"bytes_recv\": 0, \"packets_sent\": 0, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }, 
    {
      "awdl0": "{\"bytes_sent\": 459812, \"bytes_recv\": 0, \"packets_sent\": 919, \"packets_recv\": 0, \"errin\": 0, \"errout\": 0, \"dropin\": 0, \"dropout\": 0}"
    }
  ]
}
```
