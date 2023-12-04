# Running

Install deps
```shell
pip3 install -e .
```

Run
```shell
python3 test.py --help
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
