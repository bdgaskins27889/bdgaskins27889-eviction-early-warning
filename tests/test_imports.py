def test_import_package():
    import eviction_early_warning  # noqa: F401

def test_import_scoring():
    from eviction_early_warning.scoring import minmax  # noqa: F401
