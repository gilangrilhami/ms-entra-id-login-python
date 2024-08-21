import webview
import msal

CLIENT_ID = ""
TENANT_ID = ""
REDIRECT_URI = "http://localhost:5000/callback"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Please ensure that your App Registration has the following permissions.
SCOPE = ["User.Read", "GroupMember.Read.All",  "email"]

# Initialize MSAL application object
print("MSAL App Setup ...")
msal_app = msal.ConfidentialClientApplication(
    client_id=CLIENT_ID, authority=AUTHORITY
)

# Authorization URL to start the OAuth flow
print("Retrieveing Auth URL ...")
auth_url = msal_app.get_authorization_request_url(scopes=SCOPE, redirect_uri=REDIRECT_URI)

# Function to start the webview
def start_webview():
    print("Creating Webview Window ...")
    webview.create_window('Login with Azure AD', auth_url)
    print("Starting Webview Window ...")
    webview.start()

if __name__ == '__main__':
    start_webview()
