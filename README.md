# videos-platform-backend

## environment
- [macOS 10.14.6](https://www.apple.com/tw/macos/mojave/)
- [PyCharm 2019.2.2](https://www.jetbrains.com/pycharm/)
- [Python 3.7.4](https://www.python.org/)
- [Flask 1.1.1](https://github.com/pallets/flask)

## install
```shell
$ pipenv install flask
```

## .env
```
FLASK_APP=main.py
FLASK_DEBUG=True
```

## db setup
```shell
$ flask db upgrade
```

## run
```shell
$ flask run
```

## test
```shell
$ flask test
```