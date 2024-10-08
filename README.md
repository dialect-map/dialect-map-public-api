# Dialect map public API

[![CI/CD Status][ci-status-badge]][ci-status-link]
[![Coverage Status][cov-status-badge]][cov-status-link]
[![MIT license][mit-license-badge]][mit-license-link]
[![Code style][code-style-badge]][code-style-link]


### About
This repository contains the web server to access the database information.

It will be used in combination with the original PaperScape server, in order to
construct colored areas over the [Dialect map UI][dialect-map-ui] interface,
given the papers categorization over a pair of user specified jargon words frequencies.


### Dependencies
Python dependencies are specified on the multiple files within the `reqs` directory.

In order to install all the development packages, as long as the defined commit hooks:

```shell
make install-dev
```


### Formatting
All Python files are formatted using [Black][web-black], and the custom properties defined
in the `pyproject.toml` file.

```shell
make check
```


### Testing
Project testing is performed using [Pytest][web-pytest]. In order to run the tests:

```shell
make test
```


### Docker
The project is currently designed to be deployed in a Google Cloud Platform project,
so the initial step involves using [gcloud][docs-gcloud-cli] CLI tool to log into it:

```shell
gcloud login
gcloud auth configure-docker
```

In addition, macOS requires developers to have their identity keys added to the SSH agent
in order for Docker to pick up those keys when building the image with the `--ssh default` flag.

```shell
ssh-add -K
```

To build a Docker image out of the project:

```shell
make build
```

To push a Docker image to the GCP registry:

```shell
export GCP_PROJECT="ds3-dialect-map"
export GCP_REGISTRY="us.gcr.io"
make push
```


### Deployment
This project uses a set of env. variables to configure certain aspects of the API:

| ENV VARIABLE             | DEFAULT            | REQUIRED | DESCRIPTION                                   |
|--------------------------|--------------------|----------|-----------------------------------------------|
| DIALECT_MAP_DB_URL       | ...                | No       | Database connection URL                       |
| DIALECT_MAP_LOG_LEVEL    | INFO               | No       | Log messages level                            |


[ci-status-badge]: https://github.com/dialect-map/dialect-map-public-api/actions/workflows/ci.yml/badge.svg?branch=main
[ci-status-link]: https://github.com/dialect-map/dialect-map-public-api/actions/workflows/ci.yml?query=branch%3Amain
[code-style-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[code-style-link]: https://github.com/psf/black
[cov-status-badge]: https://codecov.io/gh/dialect-map/dialect-map-public-api/branch/main/graph/badge.svg
[cov-status-link]: https://codecov.io/gh/dialect-map/dialect-map-public-api
[mit-license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[mit-license-link]: https://github.com/dialect-map/dialect-map-public-api/blob/main/LICENSE

[dialect-map-ui]: https://github.com/dialect-map/dialect-map-ui
[docs-gcloud-cli]: https://cloud.google.com/sdk/docs/install
[web-black]: https://black.readthedocs.io/en/stable/
[web-pytest]: https://docs.pytest.org/en/latest/#
