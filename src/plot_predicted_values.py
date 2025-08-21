import matplotlib.pyplot as plt


def plot_predicted_values(df, variables, suffix=None, **kwargs):
    fig, axes = plt.subplots(1, len(variables), **kwargs)
    fig.suptitle("R-squared Plot", fontsize=14)
    if suffix is None:
        suffix = [""] * len(variables)
    for i, key in enumerate(variables):
        _plot_predicted_values(axes[i], df, key, variables[key], suffix[i])
    return fig


def _plot_predicted_values(ax, df, variable, res, suffix):
    pred_ols = res.get_prediction()
    iv_l = pred_ols.summary_frame()["obs_ci_lower"]
    iv_u = pred_ols.summary_frame()["obs_ci_upper"]
    fitted = res.fittedvalues
    x = df[variable].values
    y = df["ndvi"].values
    ax.set_title(f"{variable} {suffix}")
    ax.plot(x, y, "o", label="data", alpha=0.5)
    ax.plot(x, fitted, label="OLS")
    ax.plot(
        x,
        iv_u,
    )
    ax.plot(
        x,
        iv_l,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("actual")
    ax.set_ylabel("predicted")
    ax.legend(loc="best")
