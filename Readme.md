# PDF to text API

This is an API made in Python 3, using [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) principles, and following libraries outside Python core:
* Flask
* uwsgi 
* textract
* pytest

It is dockerized to make it available to be deployed easily and everywhere.

## Installation

If you don't have Docker installed in your system, please go to [Docker installation web](https://www.docker.com/products/docker-desktop) and follow the setup guide for your machine.

## How to run the API

1. Run the following command:
```
docker-compose up
```

2. Open your terminal windows and run the following command to call the API:
```
curl --location --request POST 'localhost:5000/pdf2text' \
--form 'file=@<absolute_path_to_a_pdf_file>'
```
3. You'll see the response as a json formatted output:
```
{
    "patient_id": "hash_of_patient_id",
    "document_text":"text"
}
```

## How to run tests

As an example, tests are just made for domain model.

To pass tests, run the following commands:
```
pip install -r requirements/test.txt 
pytest tests
``` 
