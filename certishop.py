import requests

class WalliD:
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token

    def _headers(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response):
        """Handles the API response and raises exceptions for error status codes."""
        if response.status_code != 200:
            try:
                error_message = response.json().get('message', 'An error occurred.')
            except ValueError:
                error_message = response.text
            raise Exception(f"API Error: {response.status_code} - {error_message}")
        return response.json()

    def create_ca(self, wallet_address, admin_email):
        url = f'{self.api_url}/ca'
        data = {
            'wa': wallet_address,
            'admin_email': admin_email
        }
        response = requests.post(url, json=data, headers=self._headers())
        return self._handle_response(response)

    def create_template(self, cid, name, wa, frontend_props):
        url = f"{self.api_url}/template/"
        data = {
            "cid": cid,
            "name": name,
            "wa": wa,
            "frontendProps": frontend_props
        }
        response = requests.post(url, json=data, headers=self._headers())
        return self._handle_response(response)

    def fetch_template(self, tid):
        url = f"{self.api_url}/template/{tid}"
        response = requests.get(url, headers=self._headers())
        return self._handle_response(response)

    def delete_template(self, tid):
        url = f"{self.api_url}/template/{tid}"
        response = requests.delete(url, headers=self._headers())
        return self._handle_response(response)

    def issue_credential(self, cid, tid, waAdmin, data, email):
        url = f"{self.api_url}/credential/create"
        payload = {
            "cid": cid,
            "tid": tid,
            "waAdmin": waAdmin,
            "data": data,
            "email": email
        }
        response = requests.post(url, json=payload, headers=self._headers())
        return self._handle_response(response)

    def verify_credential(self, credential_id, template_id, guid):
        url = f"{self.api_url}/credential/create-verify-url"
        payload = {
            "id": credential_id,
            "tid": template_id,
            "guid": guid
        }
        response = requests.post(url, json=payload, headers=self._headers())
        return self._handle_response(response)

    # Example usage
    if __name__ == "__main__":
        api_url = "https://demo.eidcmp.wallid.io/api/v1"
        api_token = "your_api_token"

        wallid = WalliD(api_url, api_token)

        # Create a template
        frontend_props = {
            "components": [
                {"id": "component_id", "type": "text"}
            ],
            "currentLayout": "current_layout"
        }
        try:
            template_response = wallid.create_template("cid_value", "template_name", "waAdmin_value", frontend_props)
            print("Template Response:", template_response)
        except Exception as e:
            print(e)

        # Issue a credential
        try:
            credential_response = wallid.issue_credential(
                "cid_value",
                "tid_value",
                "waAdmin_value",
                [{"key": "value"}],
                "user@domain.com"
            )
            print("Credential Response:", credential_response)
        except Exception as e:
            print(e)

        # Verify a credential
        try:
            verification_response = wallid.verify_credential("id_value", "tid_value", "guid_value")
            print("Verification Response:", verification_response)
        except Exception as e:
            print(e)
