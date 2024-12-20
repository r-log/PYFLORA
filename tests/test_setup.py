def test_imports():
    """Test if all required packages are installed correctly."""
    try:
        import PyQt6
        import serial
        import sqlalchemy
        import pandas
        import numpy
        import matplotlib
        from PyQt6.QtCore import QT_VERSION_STR
        print("All core packages imported successfully!")

        # Print versions
        print("\nPackage versions:")
        print(f"PyQt6 (Qt version): {QT_VERSION_STR}")
        print(f"Serial: {serial.VERSION}")
        print(f"SQLAlchemy: {sqlalchemy.__version__}")
        print(f"Pandas: {pandas.__version__}")
        print(f"Numpy: {numpy.__version__}")
        print(f"Matplotlib: {matplotlib.__version__}")

    except ImportError as e:
        print(f"Error importing packages: {e}")
    except AttributeError as e:
        print(f"Error getting version: {e}")


if __name__ == "__main__":
    test_imports()
