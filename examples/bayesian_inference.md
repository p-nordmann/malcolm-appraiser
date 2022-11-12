# Bayesian Inference

We try to quickly cover the basics about Bayesian Inference in the next paragraphs.
Please refer to litterature for a more complete overview.


## A reminder about theory


### Problem setup

We make an observation about a random variable $Y$. Let's write it $y_0$.

$Y$ can represent some physical quantity, like a seismic wave travel-time, or even more abstract quantities,
like the function that outputs a classification label to an input vector in a machine learning task, or even pretty much anything else...

We are provided with a *forward model* $f$.
A forward model is a function that sends a latent variable $X$ to the observable variable $Y$.

In other words,
$$Y = f(X)$$

So we consider that there exists a value $x_0$ such that $y_0 = f(x_0)$.

One might want to find out what value $x_0$ led to observing $y_0$, which commonly leads to solving an optimization problem.
However, often times, the forward model is an artificial model that we use to *explain* what we observe in the real world. Which means there is no *actual* $x_0$ value in the real world.
On top of that, our observations are never perfect, there is usually noise, or random quantities at play.

In fact, we observe a $y_1$ value, which is close to $y_0$ with some added noise:
$$y_1 = y_0 + \nu$$
where $\nu$ is some random noise. In what follows, we will consider $\nu$ to be gaussian of mean $0$, that is
$$ \nu \sim \mathcal{N}(0,\,\sigma^2) $$

but the same reasoning can really be applied to measurements with any kind of noise.

Going back to our forward model and latent variable, this means that we don't actually want to find a single $x_0$ value, but instead gather as much information about $X$ as we can.
In other words, we want to be able to answer questions like: *how likely* is $X$ to be equal to some value, to fall in some range or even to have some specific analytical properties.


### Bayesian formulation

In what follows, we will write $p_Z$ for the distribution of a random variable $Z$.
Given a random event $A$, we will write $p_Z( \cdot | A)$ the conditional distribution of $Z$, knowing $A$.
We will also write $\mathbb{E}(Z | A)$ the conditional expectation of $Z$ knowing $A$.

In the problem above, we know that $Y + \nu = y_1$ and we want to know information about $X$.
That is, we are interested in knowing the conditional distribution:
$$p_X( \cdot | Y+\nu = y_1)$$

We rewrite this distribution using Bayes' formula:
$$p_X( \cdot | Y+\nu = y_1) = \frac{p_{Y+\nu}(y_1 | X=\cdot)p_X(\cdot)}{p_{Y+\nu}(y_1)}$$

We note the following:
- the right term in the numerator represents what we already know about $X$
- the left term in the numerator represents, for a value $x_0$, how likely we are to observe $y_1$
- the denominator $p_{Y+\nu}(y_1)$ is a constant

$p_X(\cdot)$ is called *prior distribution* and $p_{Y+\nu}(y_1 | X=\cdot)$ is called *likelihood*.

$p_X( \cdot | Y+\nu = y_1)$ is called *posterior distribution*.

Intuitively, given an observation, we update our prior knowledge about $X$ using the likelihood of the observation
and get the posterior distribution of $X$.

The last point about the denominator being constant is useful in practice.
We will usually want to sample from the posterior distribution and most sampling techniques are
not sensitive to multiplicative constants. It means that we will not have to bother computing the integral.


### An important remark

From the remark above, we just need to know that:
$$p_X( \cdot | Y+\nu = y_1) \propto p_{Y+\nu}(y_1 | X=\cdot) p_X(\cdot)$$

On top of that, in the case where we do not have prior knowledge about $X$, we usually choose $p_X$
to be the density of the uniform distribution, *i.e.* a constant function.
In that case, we can further simplify the equation above to:
$$p_X( \cdot | Y+\nu = y_1) \propto p_{Y+\nu}(y_1 | X=\cdot)$$


## A simple example

We give a synthetic example, taken from [Example 0 - Working with a simple function](./simple_function.ipynb).


### The problem

We are given a forward model $f$:
$$f(x_0,x_1,x_2) = x_0 x_1 x_2 + 2 x_1 x_2 - 3x_0 x_2 + 2$$

We assume the noise $\nu$ to be gaussian with standard deviation $\sigma = 2$ and mean $\mu = 0$
and observe the value $y_1 = 0$.

We want to know the probability of $x_0$ being greater than $2$:
$$\mathbb{P}(x_0 > 2 | Y + \nu = 0)$$


### The likelihood

We have $Y=f(X)$, hence for some values $u,v,w$, we can write the likelihood as:

$$
\begin{aligned}
p_{Y+\nu}(y_1 | X=(u,v,w)) & = p_{\nu}(y_1 - f(u,v,w))\\
& = p_{\nu}(0 - f(u,v,w))\\
& = \exp(-\frac{f(u,v,w)^2}{8})
\end{aligned}
$$


### The prior distribution

We did not assume any prior knowledge about $X$. We choose the prior distribution to be constant.


### The posterior distribution

We intend to sample values from the posterior distribution using a sampler which is not sensitive to
multiplicative constants. We reduce the posterior distribution to:
$$p_X( u,v,w | Y+\nu = 0) \propto \exp(-\frac{f(u,v,w)^2}{8})$$


### Appraisal

Once we know how to compute the posterior distribution, we want to compute the desired quantity.

We remind that:

$$
\begin{aligned}
\mathbb{P}(x_0 > 2 | Y + \nu = 0) & = \mathbb{E}( \mathbb{1}_{x_0 > 2} | Y+ \nu = 0)\\
& = \iiint_{u,v,w} \mathbb{1}_{u > 2} \cdot p_X( u,v,w | Y+\nu = 0) \,du\,dv\,dw
\end{aligned}
$$

The `malcolm-appraiser` package offers to approximate such expectations using importance sampling.
To have an overview of the Python API, have a look at [Example 0 - Working with a simple function](./simple_function.ipynb).

