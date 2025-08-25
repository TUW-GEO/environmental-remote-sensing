ROOT = "https://git.geo.tuwien.ac.at/api/v4/projects/1266/repository/files/"


def make_url(file, lfs=True, zip=False, cache=False, verbose=True):
    url = f"{ROOT}{file}/raw?ref=main&lfs={str(lfs).lower()}"
    if verbose:
        print(url)
    if zip:
        url = f"zip::{url}"
    if cache:
        url = f"simplecache::{url}"
    return url
