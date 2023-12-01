from simple_salesforce import Salesforce

# Define your Salesforce credentials
username = 'cfgpyd@gmail.com'
password = 'pydcfg23'
security_token = 'uSxqQfiYoyrY35vqPTCfyZD5'
sf_instance = 'na1'  # e.g., 'na1' for North America

# Create a Salesforce object
sf = Salesforce(username=username, password=password, security_token=security_token, instance=sf_instance)

# Example: Query records from a Salesforce object
result = sf.query("SELECT Id, Name, Email, MailingAddress FROM Contact")

# Print the results
print(len(result['records']))
for record in result['records']:
    print(f"Account ID: {record['Id']}, Name: {record['Name']}, Email: {record['Email']}, Ethnicity: {record['MailingAddress']}")