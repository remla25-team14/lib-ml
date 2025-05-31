from .data_preprocessing import preprocess_reviews

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

__all__ = ['preprocess_reviews', '__version__']