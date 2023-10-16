from __future__ import annotations

import gdown
import os
import os.path as osp
import tarfile
from typing import Optional
import zipfile



def unzip(file_path: str) -> None:
    if file_path.endswith(".zip"):
        zip_ref = zipfile.ZipFile(file_path, "r")
        zip_ref.extractall(osp.dirname(file_path))
        zip_ref.close()

    elif file_path.endswith(".tar"):
        tar = tarfile.open(file_path, "r:")
        tar.extractall(osp.dirname(file_path))
        tar.close()

    elif file_path.endswith(".tar.gz"):
        tar = tarfile.open(file_path, "r:gz")
        tar.extractall(osp.dirname(file_path))
        tar.close()


def download_from_gdrive(url: str, destination: str) -> Optional[str]:
    if not osp.exists(osp.dirname(destination)):
        os.mkdir(osp.dirname(destination))
        file_name = gdown.download(url, destination, quiet=False)
        if file_name is None:
            raise IOError("Couldn't download data from Gdrive.")
        return os.path.join(destination, file_name)
