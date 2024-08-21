import msal
from flask import Flask, request

# MS Entra ID Credentials
CLIENT_ID = ""
TENANT_ID = ""
REDIRECT_URI = "http://localhost:5000/callback"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Please ensure that your App Registration has the following permissions.
SCOPE = ["User.Read", "GroupMember.Read.All",  "email"]

# ID of Group to validate
valid_group_id = ""

# Initialize the Flask app
app = Flask(__name__)

# Initialize MSAL application object
msal_app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID, authority=AUTHORITY
)

# Flask route to handle the callback from Azure AD
@app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    token_response = msal_app.acquire_token_by_authorization_code(
        code=auth_code, scopes=SCOPE, redirect_uri=REDIRECT_URI
    )
    # Decode the ID token
    claims = token_response.get('id_token_claims')

    # Check for group claims and display them
    if 'groups' in claims:
        print(claims["groups"])

        if valid_group_id in claims["groups"]:
            return "<html><body><h1>Login Successful!</h1></body></html>"
        
        if valid_group_id not in claims["groups"]:
            return "<html><body><h1>Not Valid Group. Login Failed.</h1></body></html>"
    
    if 'groups' not in claims:
        return "<html><body><h1>Group Claim Not Found.</h1></body></html>"

if __name__ == '__main__':
    app.run(port=5000)
