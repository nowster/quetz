![quetz header image](docs/assets/quetz_header.png)

<table>
<thead align="center" cellspacing="10">
  <tr>
    <th colspan="3" align="center" border="">part of snakepit</th>
  </tr>
</thead>
<tbody>
  <tr background="#FFF">
    <td align="center">Package Manager <a href="https://github.com/thesnakepit/mamba">mamba</a></td>
    <td align="center">Package Server <a href="https://github.com/thesnakepit/quetz">quetz</a></td>
    <td align="center">Package Builder <a href="https://github.com/thesnakepit/boa">boa</a></td>
  </tr>
</tbody>
</table>

# Quetz

The quetz project is an open source server for conda packages.
It is built upon FastAPI with an API-first approach.
A quetz server can have many users, channels and packages.
With quetz, fine-grained permissions on channel and package-name level will be possible.

Quetz also comes with the `quetz-client` that can be used to upload packages to a quetz server instance.

## Usage

You should have [mamba](https://github.com/thesnakepit/mamba) or conda installed.

Then create an environment:

```
mamba create -n quetz -c conda-forge 'python>=3.7' fastapi typer authlib httpx=0.12.0 sqlalchemy sqlite \
python-multipart uvicorn zstandard conda-build appdirs toml quetz-client fsspec

conda activate quetz
```

Get `Quetz` sources:

```
mkdir quetz
git clone https://github.com/TheSnakePit/quetz.git quetz
```

Install `Quetz`:

> Use the editable mode `-e` if you are developer and want to take advantage of the `reload` option of `Quetz`

```
pip install -e quetz 
```

Use the CLI to create a `Quetz` instance:

```
quetz run test_quetz --create-conf --dev --reload
```

Links:
 * http://localhost:8000/ - Login with your github account
 * http://localhost:8000/api/dummylogin/[ alice | bob | carol | dave] - Login with test user
 * http://localhost:8000/docs - Swagger UI for this REST service

Download `xtensor` as test package:
```
./download-test-package.sh
```

Run test upload using quetz-client:

```
export QUETZ_API_KEY=E_KaBFstCKI9hTdPM7DQq56GglRHf2HW7tQtq6si370
quetz-client http://localhost:8000/api/channels/channel0 xtensor/linux-64/xtensor-0.16.1-0.tar.bz2 xtensor/osx-64/xtensor-0.16.1-0.tar.bz2
```

Install the test package with conda:

```
mamba install --strict-channel-priority -c http://localhost:8000/channels/channel0 -c conda-forge xtensor
```

Output:

```
...
  Package  Version  Build          Channel                                                     Size
─────────────────────────────────────────────────────────────────────────────────────────────────────
  Install:
─────────────────────────────────────────────────────────────────────────────────────────────────────

  xtensor   0.16.1  0              http://localhost:8000/channels/channel0/osx-64            109 KB
  xtl       0.4.16  h04f5b5a_1000  conda-forge/osx-64                                         47 KB

  Summary:

  Install: 2 packages

  Total download: 156 KB

─────────────────────────────────────────────────────────────────────────────────────────────────────
...
```

Browse channels:

```
http://localhost:8000/channels/channel0/
```

## S3 Backend

To enable the S3 backend, you will first require the s3fs library:

    mamba install s3fs

Then add your access and secret keys to the `s3` section with your
`config.toml`, like so:

```
[s3]
access_key = "AKIAIOSFODNN7EXAMPLE"
secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
url = "https://..."
```

Be sure to set the url field if not using AWS.

## Frontend

Quetz comes with a initial frontend implementation. It can be found in quetz_frontend.
To build it, one needs to install:

```
mamba install 'nodejs>=14'
cd quetz_frontend
npm install
npm run build
# for development
npm run watch
```

This will build the javascript files and place them in `/quetz_frontend/dist/` from where they are automatically picked up by the quetz server.

## License

We use a shared copyright model that enables all contributors to maintain the copyright on their contributions.

This software is licensed under the BSD-3-Clause license. See the [LICENSE](LICENSE) file for details.
