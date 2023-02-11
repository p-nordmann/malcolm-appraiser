# malcolm-appraiser
A simple appraiser for bayesian inference.

## State of the repository

The current repository is in an early stage of development.

A lot of features are missing and no release is yet provided. It is, however, possible to
install the Python package from sources and try running the examples, but we cannot
guarantee that everything will work correctly.

## Installation instructions

If you still wish to install the package and try the API out, here is what you need to do.

### Prerequisites

Some pieces of software are necessary for running malcolm-sampler and malcolm-appraiser.

- Go v1.19 or later: installation instructions can be found at https://go.dev/doc/install.
Once you are done with those instructions, we suggest you set `GOPATH` environment variable
and add `$GOPATH/bin` to your `PATH`. If not done, you could have trouble installing or running malcolm-sampler.
For instance on linux:
```
export GOPATH=$(go env GOPATH)
export PATH=$PATH:$GOPATH/bin
```
- Python 3.7 or later: you can use your prefered installation  method.
- Pip: it comes with most Python distributions, however you might miss in some cases.
For instance, if you use conda, you can install pip with:
```
conda install -c anaconda pip
```
- Jupyter and IPython kernel (optional): if you wish to run notebooks from the `examples`
directory, you will need a working installation of Jupyter and IPython kernel (which is the
backend for Jupyter). Installation instructions can vary, dependending of your distribution of
Python. With pip for instance, you can use (from https://jupyter.org/install):
```
pip install notebook
```

### Install and run malcolm-sampler

It is necessary to install the Go worker, malcolm-sampler, in order to use
malcolm-appraiser's Python API.

The current version of the code is compatible with `v0.1` of malcolm-sampler. Because there is no
guarantee that the API stays stable from one minor version to another, it is required to install
this version of malcolm-sampler.

If you have a correct version of Go and your environment variables set correctly, you can install
malcolm-sampler with the following command:
```
go install github.com/p-nordmann/malcolm-sampler/cmd/malcolms@v0.1
```

After installation, it can be run locally with:
```
malcolms serve --port 7352
```
When `malcolms serve` is running, it will listen to incoming rpc calls dispatched by
malcolm-appraiser.

### Install malcolm-appraiser from sources

In what follows, we assume that you have a working Python installation with pip installed.

malcolm-appraiser can be installed from sources using pip:
```
git clone https://github.com/p-nordmann/malcolm-appraiser
cd malcolm-appraiser
pip install .
```

Once installed, you can check that the API works by running an instance of malcolm-sampler and
trying a notebook from the `examples` directory. You might need to install additionnal Python
packages in order to be able to run the notebook.

## References

1. Sambridge, M. (1999). Geophysical inversion with a neighbourhood algorithm -
   I. Searching a parameter space. Geophysical Journal International, 138(2),
   479–494. http://doi.org/10.1046/j.1365-246X.1999.00876.x

2. Sambridge, M. (1999). Geophysical inversion with a neighborhood algorithm -
   II. Appraising the ensemble. Geophys, J. Int., 138, 727–746.
   http://doi.org/10.1046/j.1365-246x.1999.00900.x

## Acknowledgement

This work is based on code developed in 2019 during an internship at SINTEF.

The original work came with the following acknowledgement:

> This work has been produced with support from the SINTEF-coordinated Pre-ACT project
> (Project No. 271497) funded by RCN (Norway), Gassnova (Norway), BEIS (UK), RVO (Netherlands), and BMWi (Germany) and
> co-funded by the European Commission under the Horizon 2020 programme, ACT Grant Agreement No 691712. We also
> acknowledge the industry partners for their contributions: Total, Equinor, Shell, TAQA.

## Licensing

This work is distributed under the MIT license.

See the `LICENSE` file for more information.
