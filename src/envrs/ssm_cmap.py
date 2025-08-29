import matplotlib
import pandas as pd
from download_path import make_url


def load_cmap():
    def to_hex_str(x):
        return f"#{int(x.R):02x}{int(x.G):02x}{int(x.B):02x}"

    path = r"colour-tables%2Fssm-continuous.ct"
    df = pd.read_fwf(
        make_url(path, lfs="false", verbose=False), names=["R", "G", "B"], nrows=200
    )
    brn_yl_bu_colors = df.apply(to_hex_str, axis=1).to_list()
    return matplotlib.colors.LinearSegmentedColormap.from_list("", brn_yl_bu_colors)


SSM_CMAP = load_cmap()
