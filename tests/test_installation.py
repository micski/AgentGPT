import sys
import torch
import transformers
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtWidgets import QApplication

def test_python_version():
    print(f"Python version: {sys.version}")
    assert sys.version_info >= (3, 8), "Python 3.8 lub nowszy jest wymagany."

def test_torch_installation():
    print(f"PyTorch version: {torch.__version__}")
    if torch.cuda.is_available():
        print(f"CUDA is available. GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA is not available. Running on CPU.")

def test_transformers_installation():
    print(f"Transformers version: {transformers.__version__}")
    from transformers import pipeline
    try:
        pipe = pipeline('text-generation')  # Domyślnie na CPU
        print("Pipeline 'text-generation' loaded successfully.")
    except Exception as e:
        print(f"Error loading pipeline: {e}")

def test_pyqt_installation():
    print(f"PyQt5 version: {QT_VERSION_STR}")
    try:
        app = QApplication([])
        print("PyQt5 QApplication initialized successfully.")
        app.quit()
    except Exception as e:
        print(f"Error initializing PyQt5: {e}")

if __name__ == "__main__":
    test_python_version()
    test_torch_installation()
    test_transformers_installation()
    test_pyqt_installation()
    print("All tests completed.")
