try:
    from . import customer
    from . import meter
    from . import consumption
    from . import invoice
    from . import route
    from . import zone
    from . import ocr
    from . import report
except ImportError as e:
    import sys
    sys.stderr.write(f"Module import error: {e}\n")
