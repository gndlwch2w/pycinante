"""This module provides functions to access and manipulate files.
"""
from __future__ import annotations
import glob
import os
import re
import shutil
import archive
from typing import *
from pycinante.list import listify
from system import get_default_encoding

__all__ = [
    'exists',
    'isfile',
    'isdir',
    'mkdir',
    'drive',
    'parent',
    'basename',
    'filename',
    'extension',
    'ext_aware',
    'absolute_path',
    'canonical_path',
    'relative_path',
    'normalize_path',
    'sanitize_path',
    'join',
    'list_files',
    'copy',
    'move',
    'remove',
    'PathBuilder',
    'load_pickle',
    'dump_pickle',
    'load_numpy',
    'dump_numpy',
    'load_tensor',
    'dump_tensor',
    'load_json',
    'dump_json',
    'load_yaml',
    'extract_archive'
]

exists = os.path.exists
isfile = os.path.isfile
isdir = os.path.isdir

def mkdir(pathname: str, parent: bool = False, **kwargs) -> str:
    """Create a directory. The argument `exist_ok` default is True.

    >>> mkdir('./a/b/c', parent=True)
    >>> assert not exists('./a/b/c')
    >>> shutil.rmtree('./a')
    """
    t = (parent and os.path.dirname(pathname)) or pathname
    os.makedirs(t, exist_ok=kwargs.pop('exist_ok', True), **kwargs)
    return pathname

def drive(pathname: str) -> str:
    """Return the drive of the pathname, where drive is either a mount point or the
    empty string.

    >>> drive('/usr/etc/bin/pycinante')
    ''
    """
    return os.path.splitdrive(pathname)[0]

def parent(pathname: str) -> str:
    """Return the parent directory of the file or directory `pathname`.

    >>> parent('/usr/etc/bin/pycinante')
    '/usr/etc/bin'
    """
    return os.path.dirname(pathname)

def basename(pathname: str) -> str:
    """Return the full name (included the extension) of the file on the `pathname`.

    >>> basename('/usr/etc/bin/pycinante.json')
    'pycinante.json'
    """
    return os.path.basename(pathname)

def filename(pathname: str) -> str:
    """Return the name (excluded the extension) of the file on the `pathname`.

    >>> filename('/usr/etc/bin/pycinante.json')
    'pycinante'
    """
    return os.path.basename(os.path.splitext(pathname)[0])

def extension(pathname: str) -> str:
    """Return the file extension of the file `pathname`.

    >>> extension('/usr/etc/bin/pycinante.json')
    '.json'
    """
    return os.path.splitext(pathname)[1]

def ext_aware(pathname: str, ext: str) -> str:
    """Automatically append the given extension to the pathname if the pathname
    not a suffix.

    >>> ext_aware('/usr/etc/bin/pycinante.json', '.jsoup')
    '/usr/etc/bin/pycinante.json'
    >>> ext_aware('/usr/etc/bin/pycinante', '.json')
    '/usr/etc/bin/pycinante.json'
    """
    if extension(pathname) is not None:
        return pathname
    ext = (ext.startswith('.') and ext) or ('.' + ext)
    pathname = (pathname.endswith('.') and pathname[:-1]) or pathname
    if not pathname.endswith(ext):
        pathname = pathname + ext
    return pathname

def absolute_path(pathname: str) -> str:
    """Return the absolute pathname of the file or directory `pathname`.

    >>> absolute_path('.')
    '/Volumes/User/home/chishengchen/Codespace/toy/pycinante/pycinante'
    """
    return os.path.abspath(pathname)

def canonical_path(pathname: str) -> str:
    """Return the canonical path of the specified filename, eliminating any symbolic
    links encountered in the path.

    >>> canonical_path('~/Codespace/toy/pycinante/./pycinante')
    '~/Codespace/toy/pycinante/pycinante'
    """
    return os.path.relpath(pathname)

def relative_path(pathname: str, start=None) -> str:
    """Return a relative filepath to path either from the current directory or from
    an optional start directory.

    >>> relative_path('/Volumes/User/home/chishengchen/Codespace/toy', '.')
    '../..'
    """
    return os.path.relpath(pathname, start=start or os.curdir)

def normalize_path(pathname: str) -> str:
    """Normalize a pathname by collapsing redundant separators.

    >>> normalize_path('~/Codespace/toy/./pycinante//.//pycinante')
    '~/Codespace/toy/pycinante/pycinante'
    """
    return os.path.normpath(pathname)

def sanitize_path(pathname: str, rep: str = None) -> str:
    """Replace all the invalid characters from a pathname with a char `rep`.

    >>> sanitize_path('A survey: Code is cheap, show me the code.pdf')
    'A survey Code is cheap, show me the code.pdf'
    """
    return re.sub(re.compile(r'[<>:"/\\|?*\x00-\x1F\x7F]'), rep or '', pathname)

def join(pathname: str, *pathnames: str) -> str:
    """Join one or more pathname segments intelligently. The return value is the
    concatenation of pathname and all members of `*pathnames`, with exactly one directory
    separator following each non-empty part, except the last.

    >>> join('/path/', 'etc', 'bin/', 'starting.conf')
    '/path/etc/bin/starting.conf'
    """
    return os.path.join(pathname, *pathnames)

def list_files(pathname: str, exts: str | list[str] | None = None, **kwargs) -> list[str]:
    """Return a list of pathname matching a pathname pattern.

    >>> assert list_files('./', exts=['.py'])
    """
    files = []
    for ext in listify(exts or ['*']):
        files.extend(glob.glob(os.path.join(pathname, f'*{ext}'), **kwargs))
    return files

def copy(src: str, dest: str) -> str:
    """Copy data and mode bits ("cp src dst"). Return the file's destination.

    >>> import tempfile
    >>> os.remove(copy(tempfile.mkstemp('.txt', text=True)[1], '.'))
    """
    return shutil.copy(src, dest)

def move(src: str, dest: str) -> str:
    """Recursively move a file or directory to another location. This is similar to the
    Unix "mv" command. Return the file or directory's destination.

    >>> import tempfile
    >>> os.remove(copy(tempfile.mkstemp('.txt', text=True)[1], '.'))
    """
    return shutil.move(src, dest)

def remove(pathname: str) -> None:
    """Recursively delete all files or folders in the pathname.

    >>> mkdir('./a/b/c/d/e/f/g')
    >>> remove('./a')
    >>> shutil.rmtree('./a')
    >>> assert os.system('touch tmp.txt') == 0
    >>> remove('tmp.txt')
    """
    if os.path.isdir(pathname):
        shutil.rmtree(pathname, ignore_errors=True)
        os.mkdir(pathname)
    else:
        os.remove(pathname)

class PathBuilder(object):
    """A pathname builder for easily constructing a pathname by the operation `/` and `+`.

    >>> p = PathBuilder('.', 'a', 'b', mkdir=False)
    >>> p / 'c' / 'd' / 'e' + 'f.json'
    './a/b/c/d/e/f.json'
    """

    def __init__(self, *pathnames, mkdir: bool = True):
        self.path = str(os.path.join(*(pathnames or ('.',))))
        self.mkdir = mkdir
        if self.mkdir:
            os.makedirs(self.path, exist_ok=True)

    def __truediv__(self, pathname: str) -> 'PathBuilder':
        """Append a sub-pathname to the original pathname and return a new pathname
        instance with the added sub-pathname.
        """
        return PathBuilder(join(self.path, pathname), mkdir=self.mkdir)

    def __add__(self, basename: str) -> str:
        """Append a basename to the original pathname and return the full pathname string
        after adding the basename.
        """
        return join(self.path, basename)

class text_editor(object):
    def __init__(self, pathname: str, mode='r+', encoding: str = 'utf-8'):
        self.pathname = pathname
        self.mode = mode
        self.encoding = encoding

        # TODO:
        raise NotImplementedError('not implemented')

    def clear(self) -> int:
        return self.fp.truncate()

    def write(self, s: AnyStr) -> int:
        return self.fp.write(s)

    def writeline(self, s: AnyStr) -> int:
        text = s if s.endswith(os.linesep) else s + os.linesep
        return self.fp.write(text)

    def read(self) -> AnyStr:
        return self.fp.read()

    def readline(self) -> AnyStr:
        return self.fp.readline()

    def seek(self, offset: int, whence: int = 0) -> int:
        return self.fp.seek(offset, whence)

    def __enter__(self) -> None:
        self.fp = open(self.pathname, mode=self.mode, encoding=self.encoding)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.fp.close()

def load_pickle(pathname: str, ext: str = '.pkl', **kwargs) -> ...:
    """Read a pickled object representation from the `.pkl` file.

    >>> dump_pickle({'name': 'Pycinante'}, 'test')
    >>> load_pickle('test')
    {'name': 'Pycinante'}
    >>> remove('test.pkl')
    """
    import pickle
    with open(ext_aware(pathname, ext), 'rb') as fp:
        return pickle.load(fp, **kwargs)

def dump_pickle(obj: ..., pathname: str, ext: str = '.pkl', **kwargs) -> None:
    """Write a pickled representation of obj to the `.pkl` file.

    >>> dump_pickle({'name': 'Pycinante'}, 'test')
    >>> load_pickle('test')
    {'name': 'Pycinante'}
    >>> remove('test.pkl')
    """
    import pickle
    with open(ext_aware(pathname, ext), 'wb') as fp:
        pickle.dump(obj, fp, **kwargs)

# noinspection PyUnresolvedReferences
def load_numpy(pathname: str, ext: str = '.npy', **kwargs) -> 'np.ndarray':
    """Load arrays or pickled objects from `.npz` or pickled files.

    >>> import numpy as np
    >>> dump_numpy(np.array([7, 8, 9]), 'test')
    >>> load_numpy('test')
    array([7, 8, 9])
    >>> remove('test.npy')
    """
    import numpy as np
    return np.load(ext_aware(pathname, ext), **kwargs)

# noinspection PyUnresolvedReferences
def dump_numpy(obj: 'np.ndarray', pathname: str, ext: str = '.npy', **kwargs) -> None:
    """Save an array to a binary file in NumPy ``.npz`` format.

    >>> import numpy as np
    >>> dump_numpy(np.array([7, 8, 9]), 'test')
    >>> load_numpy('test')
    array([7, 8, 9])
    >>> remove('test.npy')
    """
    import numpy as np
    np.save(ext_aware(pathname, ext), obj, **kwargs)

# noinspection PyPackageRequirements, PyUnresolvedReferences
def load_tensor(pathname: str, ext: str = '.pth', **kwargs) -> 'torch.Tensor':
    """Loads an object saved with `torch.save` from a `.pth` file.

    >>> import torch
    >>> dump_tensor(torch.tensor([7, 8, 9]), 'test')
    >>> load_tensor('test')
    tensor([7, 8, 9])
    >>> remove('test.pth')
    """
    import torch
    return torch.load(ext_aware(pathname, ext), **kwargs)

# noinspection PyPackageRequirements,PyUnresolvedReferences
def dump_tensor(obj: 'torch.Tensor', pathname: str, ext: str = '.pth', **kwargs) -> None:
    """Saves an object to a `.pth` disk file.

    >>> import torch
    >>> dump_tensor(torch.tensor([7, 8, 9]), 'test')
    >>> load_tensor('test')
    tensor([7, 8, 9])
    >>> remove('test.pth')
    """
    import torch
    torch.save(obj, ext_aware(pathname, ext), **kwargs)

def load_json(pathname: str, ext: str = '.json', **kwargs) -> ...:
    """Deserialize a file-like object containing a JSON document to a Python object.

    >>> dump_json({'name': 'Pycinante'}, 'test')
    >>> load_json('test')
    {'name': 'Pycinante'}
    >>> remove('test.json')
    """
    import json
    encoding = get_default_encoding(kwargs.pop('encoding', None))
    with open(ext_aware(pathname, ext), 'r', encoding=encoding) as fp:
        return json.load(fp, **kwargs)

def dump_json(obj: ..., pathname: str, ext: str = '.json', **kwargs) -> None:
    """Serialize the Python object `obj` into a json file.

    >>> dump_json({'name': 'Pycinante'}, 'test')
    >>> load_json('test')
    {'name': 'Pycinante'}
    >>> remove('test.json')
    """
    import json
    encoding = get_default_encoding(kwargs.pop('encoding', None))
    with open(ext_aware(pathname, ext), 'w', encoding=encoding) as fp:
        json.dump(obj, fp, **kwargs)

# noinspection PyUnresolvedReferences,PyPackageRequirements
def load_yaml(
        pathname: str,
        ext: str = '.yaml',
        loader: Optional['yaml.Loader'] = None,
        encoding: str | None = None
) -> dict:
    """Parse the YAML document in a file and produce the corresponding Python object."""
    import yaml
    pathname = ext_aware(pathname, ext)
    with open(pathname, 'r', encoding=get_default_encoding(encoding)) as fp:
        return (loader or yaml.safe_load)(fp)

def extract_archive(src: str, dest: str) -> None:
    """Unpack the tar or zip file at the specified path to the directory specified by to_path.

    Ref: [1] https://flaggo.github.io/pydu/#/zh-cn/archive
         [2] https://pypi.org/project/python-archive/
    """
    assert extension(src).lower() in archive.extension_map.keys(), \
        f'unsupported compression format for the file {src}'
    archive.extract(src, dest)
