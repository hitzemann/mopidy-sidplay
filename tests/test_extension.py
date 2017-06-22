from __future__ import unicode_literals

from mopidy_sidplay import SidplayExtension


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert '[sidplay]' in config
    assert 'enabled = true' in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    assert 'sidplayfp' in schema
    assert 'media_dir' in schema


# TODO Write more tests
