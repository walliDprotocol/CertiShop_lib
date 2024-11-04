## Overview

The WalliD CertiShop lib provides an interface for interacting with the WalliD API. It allows users to create Certificate Authorities, manage templates, issue verifiable certificates, and verify certificates through a simplified and structured approach.

## Features

- Create and manage Certificate Authorities (CAs)
- Create and manage templates
- Issue verifiable credentials
- Verify credentials
- Error handling for API requests

## Installation

To use the WalliD library, clone the repository and install the required dependencies.

```bash
git clone https://github.com/WalliD/your-repository-name.git
cd your-repository-name
````

Ensure you have Python and requests library installed. You can install the required packages using:

```bash
pip install requests
```

## Usage

### Initialize the WalliD Client

```bash
from certishop import WalliD

api_url = "https://demo.eidcmp.wallid.io/api/v1"
api_token = "your_api_token"

wallid = WalliD(api_url, api_token)

```

### Create a Certificate Authority

```bash
wallet_address = "0xYourWalletAddress"
admin_email = "admin@example.com"
response = wallid.create_ca(wallet_address, admin_email)
print(response)
```

### Create a Template

```bash
cid = "cid_value"
name = "template_name"
wa = "0xYourWalletAddress"
frontend_props = {
    "components": [
        {"id": "component_id", "type": "text"}
    ],
    "currentLayout": "current_layout"
}
response = wallid.create_template(cid, name, wa, frontend_props)
print(response)

```

### Issue a Certificate

```bash
cid = "cid_value"
tid = "tid_value"
waAdmin = "0xYourWalletAddress"
data = [{"key": "value"}]
email = "user@example.com"
response = wallid.issue_credential(cid, tid, waAdmin, data, email)
print(response)
```

### Verify a Certificate

```bash
credential_id = "credential_id"
tid = "tid_value"
guid = "guid_value"
response = wallid.verify_credential(credential_id, tid, guid)
print(response)
```

## Error Handling

The library includes error handling to manage API response errors gracefully. When an error occurs, it raises an exception with a descriptive error message.

## Tests

The library includes a suite of unit tests to verify functionality. You can run the tests using:
```bash
python -m unittest discover
```
## Contributing

Contributions are welcome! If you would like to contribute to the WalliD library, please create a pull request or open an issue for discussion.

## License

### Instructions

1. **Update Links and Tokens:** Make sure to replace any placeholder text (like `your-repository-name`, `your_api_token`, etc.) with actual values relevant to your project.
2. **Add any additional sections:** You may want to include additional sections, such as "Known Issues," "Future Improvements," or "FAQ," depending on your project's complexity.


