#! /usr/bin/env python

###############################################################################################
# NAME: cert-scan.py
# 
# Website: https://github.com/zloether/cert-scan
#
# Description: Downloads and parses TLS/SSL (X.509) certificates 
###############################################################################################


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from socket import socket
import ssl
from sys import argv



# -----------------------------------------------------------------------------
# variables
# -----------------------------------------------------------------------------
default_port = 443
ca_chain = 'ca_chain.crt'
subject_elements = {
    'businessCategory': 'Category',
    'jurisdictionCountryName': 'Jurisdiction',
    'serialNumber': 'Serial Number',
    'countryName': 'C',
    'stateOrProvinceName': 'ST',
    'localityName': 'L',
    'organizationName': 'O',
    'organizationalUnitName': 'OU',
    'commonName': 'CN'
}



# -----------------------------------------------------------------------------
# connect
# -----------------------------------------------------------------------------
def connect(host, port=default_port):
    s = socket() # create socket

    # wrap socket
    c = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED, ca_certs=ca_chain)
    
    # connect to host
    c.connect((host, port))

    # get json reponse
    j = c.getpeercert()
    
    subject = j['subject']
    version = j['version']
    serial = j['serialNumber']
    valid_from = j['notBefore']
    valid_to = j['notAfter']
    san = j['subjectAltName']
    ocsp = j['OCSP']
    issuer = j['caIssuers']
    crl = j['crlDistributionPoints']
    

    print('Subject:')
    parse_subject(subject)
    print('Version: ' + str(version))
    print('Serial Number:\t' + str(serial))
    print('Valid from:\t' + str(valid_from))
    print('Valid to:\t' + str(valid_to))
    print('SAN:')
    parse_san(san)
    print('OCSP:')
    parse_element(ocsp)
    print('Issuer:')
    parse_element(issuer)
    print('CRL:')
    parse_element(crl)



# -----------------------------------------------------------------------------
# parse subject
# -----------------------------------------------------------------------------
def parse_subject(subject):
    for i in subject:
        for element, value in i:
            if element in subject_elements:
                print('\t' + str(subject_elements[element]) + ': ' + str(value))



# -----------------------------------------------------------------------------
# parse san
# -----------------------------------------------------------------------------
def parse_san(san):
    for element, value in san:
        print('\t' + str(element) + ': ' + str(value))



# -----------------------------------------------------------------------------
# parse ocsp
# -----------------------------------------------------------------------------
def parse_element(element):
    for element in element:
        print('\t' + str(element))



# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    if len(argv) > 1:
        host = argv[1]
    else:
        print('Error: must provide hostname as input')
        exit(1)
    
    if len(argv) > 2:
        port = int(argv[2])
    else:
        port = default_port

    connect(host, port)