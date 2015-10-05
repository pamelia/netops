## subnet splitter

    $ ./split.py 2a01:babe::/32 48 4
    2a01:babe:0000:0000:0000:0000:0000:0000/48
    2a01:babe:0001:0000:0000:0000:0000:0000/48
    2a01:babe:0002:0000:0000:0000:0000:0000/48
    2a01:babe:0003:0000:0000:0000:0000:0000/48

    ## print junos device port status
    $ ./junos_port_status.py foo 10.255.1.100
    Interface   Description                             Status  Time since last flap
    --------------------------------------------------------------------------------
    ge-0/0/0    foo description                         up      2015-09-18 13:35:20 CEST (2w3d 09:50 a    go)
    ge-0/0/1    bar description                         up      2015-09-18 13:35:20 CEST (2w3d 09:50 a    go)
    ge-0/0/2                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/3                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/4                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/5                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/6                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/7                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/8                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/0/9                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/0                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/1                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/2                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/3                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/4                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/5                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/6                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/7                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/8                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)
    ge-0/1/9                                            down    2015-09-11 09:58:05 CEST (3w3d 13:27 a    go)

## abort pending rollback due to prior commit confirm by doing a commit check

    ./junos_commit_check.py foo 10.255.1.100
