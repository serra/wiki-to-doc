from sniffer.api import runnable


@runnable
def execute(*args):
    import pytest
    return pytest.main(['-x', 'tests', '-m', 'not slow']) == 0
