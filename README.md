# example-pytest

This is sample repo for using pytest and pytest-env.

## Setup

Create virtualenv.

```$xslt
$ virtualenv virtualenv
$ source virtualenv/bin/activate
```

Install dependencies.

```$xslt
$ pip install -r requements.txt
```

## Run Test

```$xslt
$ pytest
$ pytest --ignore=tests/A/
```
