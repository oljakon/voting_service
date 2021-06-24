### POST /api/createPoll/

```
$ cat post_data.txt
{"poll": {"name": "Test"}, "choices": ["Test 1", "Test2"]}
$ ab -p post_data.txt -T application/json -c 10 -n 1000 http://127.0.0.1:8000/api/createPoll/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /api/createPoll/
Document Length:        26 bytes

Concurrency Level:      10
Time taken for tests:   7.905 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      307000 bytes
Total body sent:        210000
HTML transferred:       26000 bytes
Requests per second:    126.50 [#/sec] (mean)
Time per request:       79.054 [ms] (mean)
Time per request:       7.905 [ms] (mean, across all concurrent requests)
Transfer rate:          37.92 [Kbytes/sec] received
                        25.94 kb/s sent
                        63.87 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       2
Processing:    16   79  21.7     75     235
Waiting:       15   64  20.4     61     195
Total:         16   79  21.7     75     236

Percentage of the requests served within a certain time (ms)
  50%     75
  66%     82
  75%     88
  80%     91
  90%    101
  95%    116
  98%    145
  99%    165
 100%    236 (longest request)
```



### POST /api/poll/

```
$ cat post_poll.txt
{"poll_id": 1, "choice_id": 2}
$ ab -p post_poll.txt -T application/json -c 10 -n 1000 http://127.0.0.1:8000/api/poll/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /api/poll/
Document Length:        12 bytes

Concurrency Level:      10
Time taken for tests:   6.166 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      288000 bytes
Total body sent:        174000
HTML transferred:       12000 bytes
Requests per second:    162.19 [#/sec] (mean)
Time per request:       61.658 [ms] (mean)
Time per request:       6.166 [ms] (mean, across all concurrent requests)
Transfer rate:          45.61 [Kbytes/sec] received
                        27.56 kb/s sent
                        73.17 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:    15   61  11.4     60     118
Waiting:       14   53  10.6     52     101
Total:         15   61  11.4     60     118

Percentage of the requests served within a certain time (ms)
  50%     60
  66%     64
  75%     67
  80%     70
  90%     75
  95%     81
  98%     88
  99%     96
 100%    118 (longest request)
```

### POST /api/getResult/

```
$ cat post_res.txt
{"poll_id": 1}
$ ab -p post_res.txt -T application/json -c 10 -n 7.0.0.1:8000/api/getResult/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /api/getResult/
Document Length:        24 bytes

Concurrency Level:      10
Time taken for tests:   5.046 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      300000 bytes
Total body sent:        163000
HTML transferred:       24000 bytes
Requests per second:    198.19 [#/sec] (mean)
Time per request:       50.456 [ms] (mean)
Time per request:       5.046 [ms] (mean, across all concurrent requests)
Transfer rate:          58.06 [Kbytes/sec] received
                        31.55 kb/s sent
                        89.61 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       2
Processing:    13   50   8.6     49      96
Waiting:       12   44   7.8     44      87
Total:         13   50   8.6     49      97

Percentage of the requests served within a certain time (ms)
  50%     49
  66%     52
  75%     54
  80%     55
  90%     59
  95%     64
  98%     79
  99%     85
 100%     97 (longest request)
 ```