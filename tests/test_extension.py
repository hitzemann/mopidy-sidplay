from __future__ import unicode_literals

from mopidy_sidplay import Extension


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert '[sidplay]' in config
    assert 'enabled = true' in config
    assert 'player = sidplayfp' in config
    assert 'media_dir = /media/C64Music' in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    print(schema)

# TODO Write more tests
