from app import sample


def test_sample1():
    text = sample.sample_func()
    assert 'Env is "env1-for-test"' == text

