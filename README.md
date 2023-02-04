# malcolm-appraiser
A simple appraiser for bayesian inference.

## State of the repository

The current repository is in an early stage of development.

A lot of features are missing and no release is yet provided. It is, however, possible to
install the Python package from sources and try running the examples, but we cannot
guarantee that everything will work correctly.

## Installation instructions

If you still wish to install the package and try the API out, here is what you need to do.

### Install and run malcolm-sampler

It is necessary to install the Go worker, `malcolm-sampler`, in order to use
`malcolm-appraiser`'s Python API.

The current version of the code is compatible with `v0.1` of `malcolm-sampler`. Because there is
no guarantee that the API stays stable from one minor version to another, it is required to install
this version of `malcolm-sampler`.

First make sure to have Go v1.19 or later installed. See https://go.dev/doc/install for installation
instructions.

You can then install `malcolm-sampler` with the following commands:

```
go install github.com/p-nordmann/malcolm-sampler/cmd/malcolms@v0.1
```

After installation, it can be run locally with the following command:

```
malcolms serve --port 7352
```

When `malcolm-sampler` is running, it will listen to incoming rpc calls which will be dispatched
by `malcolm-appraiser`.

### Install malcolm-appraiser from sources

In what follows, we assume that you have a working Python installation.

`malcolm-appraiser` can be installed from sources using pip:

```
git clone https://github.com/p-nordmann/malcolm-appraiser
cd malcolm-appraiser
pip install .
```

Once installed, you can check that the API works by running an instance of
`malcolm-sampler` and trying a notebook from the `examples` section. You might need to
install additionnal Python packages in order to be able to run the notebook.

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
