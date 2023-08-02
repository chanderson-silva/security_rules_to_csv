# Create a CSV file from Security Rules Prisma Access Cloud Management
This Python script aims to generate a CSV file of security rules for a [Folder](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/create-prisma-access-policy/organizing-your-prisma-access-configurations#:~:text=Configuration%20Folders%20You%20can%20apply%20Prisma%20Access%20policy,be%20shared%20or%20are%20specific%20to%20deployment%20types.) Using the API, this task can be automated and completed quickly.


### Requirements
* Python 3.x installed on your system.
* Installed requests module. If you don't have it, you can install it using pip:
```python
pip install requests
```
* Installed csv module. If you don't have it, you can install it using pip:
```python
pip install csv
```
* Installed getpass module. If you don't have it, you can install it using pip:
```python
pip install getpass
```
### Usage
Ensure that Python 3.x is installed on your system, and the required basic modules are installed correctly.

Clone this repository or download the files to your computer.

### What You'll Need

* Your access_token for authentication
* The name of the source Folder
* Client ID
* Client Secret
* Execute the generate_csv_security_rules.py script:

```python
python generate_csv_security_rules.py
```
The script will generate a csv file the specified folder

Contribution
If you have suggestions for improvements or encounter any issues, feel free to open an issue or send a pull request to this repository.
