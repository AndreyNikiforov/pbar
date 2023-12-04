# Running

Install deps
```shell
pip3 install -e .
```

Run
```shell
python3 test.py --help
```
```shell
python3 test_no_click.py --help
```

# Things to check

## Resizing TTY

Should not break the flow

## Aborting

Should not report threading/multi process errors

## Scope

- Lin/Win/Mac
- src/packaged in binary

## TODO

`icloudpd` fails and throws exceptions on ctrl-c, while this test does not. Adding http calls may be needed to repro

# Trials

## No_click with freeze & warnings

Shows on ctrl-c - most likely from `sleep`, not tqdm
```shell
Traceback (most recent call last):                                                                                                                                                                                                 
  File "/workspaces/pbar/test_no_click.py", line 33, in <module>
    tqdm_main()
  File "/workspaces/pbar/test_no_click.py", line 29, in tqdm_main
    time.sleep(1)
KeyboardInterrupt
```