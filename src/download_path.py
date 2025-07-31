ROOT = (
    "simplecache::zip::https://git.geo.tuwien.ac.at/api/v4/projects/1266"
    + "/repository/files/"
)


def make_url(file, lfs="true"):
    return ROOT + file + f"/raw?ref=main&lfs={lfs}"
