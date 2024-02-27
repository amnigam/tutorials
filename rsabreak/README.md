# Web App with Vulnerable RSA Implementation 

This repository contains a web application that is deliberately vulnerable to **CVE-2022-26320**. 
In a nutshell, if the algorithm used to select the prime numbers (p, q) responsible for generating the RSA key are not sufficiently spaced apart then it is possible 
to identify them with Fermat's Factorization algorithm (Factorizing publicly declared n). This would result in the compromise of the private key and thus in the complete breakdown of the algorithm's implementation. 

## What is the vulnerability in this application?

This repository contains a very simple, Hello World, kind of a Flask application. However, the application is TLS enabled and contains a self signed certificate. 
The problem lies in the fact that, the certificate contains the Public Key which can be easily factorized into its prime factors. Once, that is done it is trivial to generate the Private Key for the certificate. 

To drive home the vulnerability's impact, there is an SSH service as well. 
And it allows ROOT access (SSH) to the container via the private key that has been reconstructed from the factorization of the public key available in the certificate. 

## How to use this vulnerable application?

You can spin up the container from the Dockerfile. 

> docker build -t <appname> . 

Once it has been build, one can launch it. The application listens on port 8080 and so you will have to map it before launching.

> docker run --rm -it -p 3000:8080 <appname> 

This will get us inside the folder containing the python Flask application. You can run the application,

> python3 app.py 

And then you can try to access it on [localhost:3000] https://localhost:3000 
