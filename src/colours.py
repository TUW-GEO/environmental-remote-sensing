from pathlib import Path

import matplotlib


def load_cmap(file: Path) -> matplotlib.colors.LinearSegmentedColormap:
    def to_hex_str(c_str: str) -> str:
        r_s, g_s, b_s = c_str.split()
        return f"#{int(r_s):02x}{int(g_s):02x}{int(b_s):02x}"

    ct_lines = Path(file).read_text().splitlines()
    brn_yl_bu_colors = [to_hex_str(clr_str) for clr_str in ct_lines[:200]]
    return matplotlib.colors.LinearSegmentedColormap.from_list("", brn_yl_bu_colors)


SSM_CMAP = load_cmap("data/colour-tables/ssm-continuous.ct")
