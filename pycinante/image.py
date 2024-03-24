"""This module provides functions to access and manipulate images.
"""
try:
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    import cv2
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    import numpy as np
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    from PIL import Image
except ImportError:
    ...

__all__ = [
    'cv2_loader',
    'pil_loader',
    'scale'
]

def cv2_loader(path: str) -> 'np.ndarray':
    """Load an image from the given path using the OpenCV."""
    return cv2.imread(path, cv2.COLOR_BGR2RGB)

def pil_loader(path: str) -> 'Image.Image':
    """Load an image from the given path using the PIL."""
    return Image.open(path)

def scale(image: 'Image.Image', width: int = None, height: int = None, resample: 'Image.Resampling' = None) -> 'Image.Image':
    """Scale the given PIL image. Given `width` or `height`, calculate another value in proportion;
    If both `width` and `height` are given, then scale to the specified size (not necessarily to maintain
    the scale, depending on the parameter).
    """
    assert width or height, 'width and height cannot both be None'
    height = (not height and int(image.size[1] * width / image.size[0])) or height
    width = (not width and int(image.size[0] * height / image.size[1])) or width
    resample = resample or getattr(Image, 'ANTIALIAS', getattr(Image, 'LANCZOS'))
    return image.resize((width, height), resample=resample)
