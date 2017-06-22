from __future__ import unicode_literals

from mopidy_sidplay import SidplayBackend


def test_get_default_config():
    back = SidplayBackend()

    config = back.get_default_config()

    assert '[sidplay]' in config
    assert 'enabled = true' in config


def test_get_config_schema():
    back = SidplayBackend()

    schema = back.get_config_schema()

    assert 'sidplayfp' in schema
    assert 'media_dir' in schema


# TODO Write more tests
