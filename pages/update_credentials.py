import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter.messagebox import showerror, showinfo

import dotenv
import os

import threading

import logging

dotenv.load_dotenv(dotenv.find_dotenv())

google_type_entry = None
google_project_id_entry = None
google_private_key_id_entry = None
google_private_key_entry = None
google_client_email_entry = None
google_client_id_entry = None
google_auth_uri_entry = None
google_token_uri_entry = None
google_auth_provider_x509_cert_url_entry = None
google_client_x509_cert_url_entry = None
google_universe_domain_entry = None
ims_api_key_entry = None
google_type_var = None
google_project_id_var = None
google_private_key_id_var = None
google_private_key_var = None
google_client_email_var = None
google_client_id_var = None
google_auth_uri_var = None
google_token_uri_var = None
google_auth_provider_x509_cert_url_var = None
google_client_x509_cert_url_var = None
google_universe_domain_var = None
ims_api_key_var = None


def update_credentials(notebook):
    """
    Update Google and IMS API credentials in the .env file based on the user input.

    This function is triggered by the 'Submit' button. It validates the provided values. If all values are valid, it updates the .env file with the entered credentials.

    Returns:
        None
    """
    # Disable buttons to avoid user interaction
    notebook.configure(state="disabled")
    # Alert if one of the fields are empty
    if (
        not google_type_var.get()
        or not google_project_id_var.get()
        or not google_private_key_id_var.get()
        or not google_private_key_var.get()
        or not google_client_email_var.get()
        or not google_client_id_var.get()
        or not google_auth_uri_var.get()
        or not google_token_uri_var.get()
        or not google_auth_provider_x509_cert_url_var.get()
        or not google_client_x509_cert_url_var.get()
        or not google_universe_domain_var.get()
        or not ims_api_key_var.get()
    ):
        showerror("Error in credentials", "One or more values are not valid.")
        logging.error("Error in credentials: One or more values are not valid.")
        return

    private_key_formmated = google_private_key_var.get().replace("\n", "\\n")

    # Write all the credentials to a .env file
    with open(".env", "w") as envfile:
        envfile.write(
            f"""# GOOGLE
type={google_type_var.get()}
project_id={google_project_id_var.get()}
private_key_id={google_private_key_id_var.get()}
private_key={private_key_formmated}
client_email={google_client_email_var.get()}
client_id={google_client_id_var.get()}
auth_uri={google_auth_uri_var.get()}
token_uri={google_token_uri_var.get()}
auth_provider_x509_cert_url={google_auth_provider_x509_cert_url_var.get()}
client_x509_cert_url={google_client_x509_cert_url_var.get()}
universe_domain={google_universe_domain_var.get()}

#IMS
API_KEY={ims_api_key_entry.get()}
"""
        )
    # Show a success message
    showinfo("Credentials updated", "The credentials has been updated successfully.")
    logging.info("The credentials has been updated successfully.")

    # Enable back all the buttons
    notebook.configure(state="normal")


def start_processing(notebook):
    """
    Start a new thread to update credentials asynchronously.

    This function is triggered by the 'Submit' button. It creates a new thread to execute the 'update_credentials'
    function asynchronously.

    Returns:
        None
    """
    threading.Thread(target=lambda: update_credentials(notebook)).start()


def update_credentials_gui(root, notebook):
    """
    Create a GUI window for updating Elasticsearch and IMS API credentials.

    This function initializes a Tkinter window with entry fields for Cloud ID, user name, password, and API_KEY.
    It also provides a 'Submit' button to trigger the credential update process.

    Args:
        root (tk.Tk): The Tkinter root window.

    Returns:
        None
    """
    global google_type_entry, google_project_id_entry, google_private_key_id_entry, google_private_key_entry, google_client_email_entry, google_client_id_entry, google_auth_uri_entry, google_token_uri_entry, google_auth_provider_x509_cert_url_entry, google_client_x509_cert_url_entry, google_universe_domain_entry, ims_api_key_entry, google_type_var, google_project_id_var, google_private_key_id_var, google_private_key_var, google_client_email_var, google_client_id_var, google_auth_uri_var, google_token_uri_var, google_auth_provider_x509_cert_url_var, google_client_x509_cert_url_var, google_universe_domain_var, ims_api_key_var

    frame = ctk.CTkScrollableFrame(root, width=root.winfo_width(), height=root.winfo_height())

    title_label = ctk.CTkLabel(
        frame,
        text="Update Credentials",
        font=("Helvetica", 16, "bold"),
    )
    title_label.pack(pady=10, anchor="center")

    google_type_label = ctk.CTkLabel(
        frame,
        text="Enter the Google type:",
        font=("Helvetica", 12),
    )
    google_type_label.pack(pady=10)

    google_type_var = ctk.StringVar()
    google_type_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=google_type_var)
    google_type_entry.insert(
        0, os.environ.get("type") if "type" in os.environ.keys() else ""
    )
    google_type_entry.pack(pady=10)

    google_project_id_label = ctk.CTkLabel(
        frame,
        text="Enter the Google project id :",
        font=("Helvetica", 12),
    )
    google_project_id_label.pack(pady=10)

    google_project_id_var = ctk.StringVar()
    google_project_id_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=google_project_id_var)
    google_project_id_entry.insert(
        0, os.environ.get("project_id") if "project_id" in os.environ.keys() else ""
    )
    google_project_id_entry.pack(pady=10)

    google_private_key_id_label = ctk.CTkLabel(
        frame,
        text="Enter the Google private key id:",
        font=("Helvetica", 12)
    )
    google_private_key_id_label.pack(pady=10)

    google_private_key_id_var = ctk.StringVar()
    google_private_key_id_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_private_key_id_var
    )
    google_private_key_id_entry.insert(
        0,
        (
            os.environ.get("private_key_id")
            if "private_key_id" in os.environ.keys()
            else ""
        ),
    )
    google_private_key_id_entry.pack(pady=10)

    google_private_key_label = ctk.CTkLabel(
        frame,
        text="Enter the Google private key:",
        font=("Helvetica", 12),
    )
    google_private_key_label.pack(pady=10)

    google_private_key_var = ctk.StringVar()
    google_private_key_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_private_key_var
    )
    google_private_key_entry.insert(
        0,
        (
            os.environ.get("private_key").replace("\n", "\\n")
            if "private_key" in os.environ.keys()
            else ""
        ),
    )
    google_private_key_entry.pack(pady=10)

    google_client_email_label = ctk.CTkLabel(
        frame,
        text="Enter the Google client email:",
        font=("Helvetica", 12),
    )
    google_client_email_label.pack(pady=10)

    google_client_email_var = ctk.StringVar()
    google_client_email_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_client_email_var
    )
    google_client_email_entry.insert(
        0, os.environ.get("client_email") if "client_email" in os.environ.keys() else ""
    )
    google_client_email_entry.pack(pady=10)

    google_client_id_label = ctk.CTkLabel(
        frame,
        text="Enter the Google client id:",
        font=("Helvetica", 12),
    )
    google_client_id_label.pack(pady=10)

    google_client_id_var = ctk.StringVar()
    google_client_id_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=google_client_id_var)
    google_client_id_entry.insert(
        0, os.environ.get("client_id") if "client_id" in os.environ.keys() else ""
    )
    google_client_id_entry.pack(pady=10)

    google_auth_uri_label = ctk.CTkLabel(
        frame,
        text="Enter the Google auth uri:",
        font=("Helvetica", 12),
    )
    google_auth_uri_label.pack(pady=10)

    google_auth_uri_var = ctk.StringVar()
    google_auth_uri_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=google_auth_uri_var)
    google_auth_uri_entry.insert(
        0, os.environ.get("auth_uri") if "auth_uri" in os.environ.keys() else ""
    )
    google_auth_uri_entry.pack(pady=10)

    google_token_uri_label = ctk.CTkLabel(
        frame,
        text="Enter the Google token uri:",
        font=("Helvetica", 12),
    )
    google_token_uri_label.pack(pady=10)

    google_token_uri_var = ctk.StringVar()
    google_token_uri_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=google_token_uri_var)
    google_token_uri_entry.insert(
        0, os.environ.get("token_uri") if "token_uri" in os.environ.keys() else ""
    )
    google_token_uri_entry.pack(pady=10)

    google_auth_provider_x509_cert_url_label = ctk.CTkLabel(
        frame,
        text="Enter the Google auth provider x509 cert url:",
        font=("Helvetica", 12),
    )
    google_auth_provider_x509_cert_url_label.pack(pady=10)

    google_auth_provider_x509_cert_url_var = ctk.StringVar()
    google_auth_provider_x509_cert_url_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_auth_provider_x509_cert_url_var
    )
    google_auth_provider_x509_cert_url_entry.insert(
        0,
        (
            os.environ.get("auth_provider_x509_cert_url")
            if "auth_provider_x509_cert_url" in os.environ.keys()
            else ""
        ),
    )
    google_auth_provider_x509_cert_url_entry.pack(pady=10)

    google_client_x509_cert_url_label = ctk.CTkLabel(
        frame,
        text="Enter the Google client x509 cert url:",
        font=("Helvetica", 12),
    )
    google_client_x509_cert_url_label.pack(pady=10)

    google_client_x509_cert_url_var = ctk.StringVar()
    google_client_x509_cert_url_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_client_x509_cert_url_var
    )
    google_client_x509_cert_url_entry.insert(
        0,
        (
            os.environ.get("client_x509_cert_url")
            if "client_x509_cert_url" in os.environ.keys()
            else ""
        ),
    )
    google_client_x509_cert_url_entry.pack(pady=10)

    google_universe_domain_label = ctk.CTkLabel(
        frame,
        text="Enter the Google universe domain:",
        font=("Helvetica", 12),
    )
    google_universe_domain_label.pack(pady=10)

    google_universe_domain_var = ctk.StringVar()
    google_universe_domain_entry = ctk.CTkEntry(
        frame, width=300, font=("Helvetica", 12), textvariable=google_universe_domain_var
    )
    google_universe_domain_entry.insert(
        0,
        (
            os.environ.get("universe_domain")
            if "universe_domain" in os.environ.keys()
            else ""
        ),
    )
    google_universe_domain_entry.pack(pady=10)

    ims_api_key_label = ctk.CTkLabel(
        frame,
        text="Enter the IMS api key:",
        font=("Helvetica", 12),
    )
    ims_api_key_label.pack(pady=10)

    ims_api_key_var = ctk.StringVar()
    ims_api_key_entry = ctk.CTkEntry(frame, width=300, font=("Helvetica", 12), textvariable=ims_api_key_var)
    ims_api_key_entry.insert(
        0, os.environ.get("API_KEY") if "API_KEY" in os.environ.keys() else ""
    )
    ims_api_key_entry.pack(pady=10)

    submit_button = ctk.CTkButton(
        frame,
        text="Submit",
        command=lambda: start_processing(notebook),
        fg_color=("#4CAF50", "#4CAF50"),
        text_color=("white", "white"),
        font=("Helvetica", 12),
    )
    submit_button.pack(pady=10)

    frame.pack(fill="both", expand=True)
