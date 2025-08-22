import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.tsa.stattools as smt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def plot_predicted_values(df, variables, suffix=None, **kwargs):
    fig, axes = plt.subplots(1, len(variables), **kwargs)
    fig.suptitle("R-squared Plot", fontsize=14)
    if suffix is None:
        suffix = [""] * len(variables)
    for i, key in enumerate(variables):
        _plot_predicted_values(axes[i], df, key, variables[key], suffix[i])
    plt.close()
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


def plot_step_corr(df, var1, var2="copy", length=72):
    p = _plot_step_corr(df, var1, var2, length)
    plt.close()
    return p


def _plot_step_corr(df, var1, var2="copy", length=72):
    def step_corr(x):
        # clear frame
        fig.clear()
        # original and shifted time series
        ax1 = plt.subplot(1, 2, 1)
        if var2 == "copy":
            y = df[var1]
            y.plot(y=var1, ax=ax1)
            y.shift(x).plot(y=var1, c="orange", ax=ax1)
            res = pd.Series(
                smt.acf(y.values, nlags=length), index=df.index[: length + 1]
            )
            plt.title(f"{var1} and copy at lag={x}")
        else:
            y1 = df[var1]
            y2 = df[var2]
            y1.plot(y=var1, ax=ax1)
            y2.shift(x).plot(y=var2, c="orange", ax=ax1)
            res = pd.Series(
                smt.ccf(y1.values, y2.values, nlags=length), index=df.index[:length]
            )
            plt.title(f"{var1} and {var2} at lag={x}")

        ax1.set_ylabel("")
        plt.legend([var1, var2])

        # correlation of time series at step #
        ax2 = plt.subplot(1, 2, 2)
        res.iloc[:x].plot(ax=ax2)
        ax2.set_ylabel("")
        plt.title("Correlation result")

    fig = plt.figure(figsize=(12, 5))
    frames = np.arange(1, length, 1)
    anim = FuncAnimation(fig, step_corr, frames, interval=500)
    return HTML(anim.to_html5_video())
