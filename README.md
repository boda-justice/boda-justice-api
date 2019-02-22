# boda-justice-api
The API for the Boda Justice Application

### Setting up the application

#### Dependencies

What was used to set up the application:

| **Version**     | **Packages/Languages/Frameworks**                              |
|-----------------|----------------------------------------------------------------|
|`3.7`            | [Python](https://www.python.org/downloads/release/python-370/) |
|`18.1`           | [Pip](https://pip.pypa.io/en/stable/)                          |
|`2.1.7`          | [Django](https://www.djangoproject.com/)                       |

1. Clone the repository

```
mkdir Hackathon
cd Hackathon
git clone https://github.com/boda-justice/boda-justice-api.git
```

2. Create a virtual environment for the application and activate it.

```
cd boda-justice-api
virtualenv --python=python3 venv
source venv/bin/activate
```

3. Install requirements for the application

```
pip install -r requirements.txt
```

4. Run the application

```
cd src/core/
python manage.py runserver
```
