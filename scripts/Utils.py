import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

# normalize the copy of old dataframe, and return the new dataframe, as well as the mean and standard deviation
def normalization(df):
    mean = df.mean()
    std = df.std()
    new = df.copy()
    new = (new - mean) / std
    return new, mean, std


# normalize the whole dataframe (value type) using a certain mu and sigma
def normalization2(df, mu, sigma):
    new = df.copy()
    new = (new - mu) / sigma
    return new

# apply johnson transformation
def johnson_transform(x):
    gamma, eta, epsilon, lbda = st.johnsonsu.fit(x)
    yt = gamma + eta * np.arcsinh((x - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


# apply inverse of johnson transformation
def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon
	
def lognormal_transform(y):
    shape, loc, scale = st.lognorm.fit(y, floc=0)
    yt = np.log(y)
    return yt, shape, loc, scale
	
def lognormal_inverse(yt):
    y = np.exp(y)
    return y

def check_dist(x, fs=(20, 3), xlab="Dist", ylab="Freq", titlefont=20, axisfont=15, hspace=0.4, wspace=0.2):
    fig = plt.figure(figsize=fs)
    fig.tight_layout()
    
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_title("Johnson SU", fontsize=titlefont)
    ax = sns.distplot(x, kde=False, fit=st.johnsonsu)
    ax.set(xlabel=xlab, ylabel=ylab)
    ax.set_xlabel(xlab, fontsize=axisfont)
    ax.set_ylabel(ylab, fontsize=axisfont)

    ax2 = fig.add_subplot(1, 3, 2, sharey=ax1)
    ax2.set_title("Log Normal", fontsize=titlefont)
    ax = sns.distplot(x, kde=False, fit=st.lognorm)
    ax.set(xlabel=xlab, ylabel=ylab)
    ax.set_xlabel(xlab, fontsize=axisfont)
    ax.set_ylabel(ylab, fontsize=axisfont)

    ax3 = fig.add_subplot(1, 3, 3, sharey=ax1)
    ax3.set_title("Normal", fontsize=titlefont)
    ax = sns.distplot(x, kde=False, fit=st.norm)
    ax.set(xlabel=xlab, ylabel=ylab)
    ax.set_xlabel(xlab, fontsize=axisfont)
    ax.set_ylabel(ylab, fontsize=axisfont)
    
    fig.subplots_adjust(wspace=wspace)
    plt.show()

def customized_heatmap(X, ax, annot=True, trim=True, cmap=sns.diverging_palette(240, 10, as_cmap=True),
                       title='', title_size=20, xticklab=[], ylab='', label_size=15):
    mask = np.zeros_like(X)
    mask[np.triu_indices_from(mask)] = True
    if trim:
        sns.heatmap(X, mask=mask, cmap=cmap, annot=annot, square=True, ax=ax)
    else:
        sns.heatmap(X, cmap=cmap, annot=annot, ax=ax)
    ax.set_title(title, fontsize=title_size)
    ax.set_xticklabels(xticklab)
    ax.set_ylabel(ylab, fontsize=label_size)

