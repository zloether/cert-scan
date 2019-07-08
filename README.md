# Cert Scan
Downloads and parses TLS/SSL (X.509) certificates

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: The `cert-scan.py` script has not been tested with Python 2 and may not work without changing some things.*

## Installation
Download the latest version from GitHub using Git:
```
git clone https://github.com/zloether/cert-scan
```
This will create a directory called *cert-scan* and all the code will be in it.

Switch to the *cert-scan* directory:
```
cd cert-scan
```

Install the required packages:
```
pip install -r requirements.txt
```

## Usage
The root signing certificate for the website your are trying to scan must be added to the `ca_chain.crt` file.


```
python cert-scan.py www.google.com
Subject:
        C: US
        ST: California
        L: Mountain View
        O: Google LLC
        CN: www.google.com
Version: 3
Serial Number:  1975C725003848CCDCE48E924E39A29D
Valid from:     Jun 11 12:41:09 2019 GMT
Valid to:       Sep  3 12:21:00 2019 GMT
SAN:
        DNS: www.google.com
OCSP:
        http://ocsp.pki.goog/GTSGIAG3
Issuer:
        http://pki.goog/gsr2/GTSGIAG3.crt
CRL:
        http://crl.pki.goog/GTSGIAG3.crl
```