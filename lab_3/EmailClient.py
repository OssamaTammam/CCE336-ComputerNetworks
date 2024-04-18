import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
import smtplib
import imaplib
import email


class EmailClient:
    def __init__(self, master):
        self.master = master
        master.title("Email Client")

        self.labelEmail = tk.Label(master, text="Email:")
        self.labelEmail.grid(row=0, column=0)

        self.entryEmail = tk.Entry(master)
        self.entryEmail.grid(row=0, column=1)

        self.labelPassword = tk.Label(master, text="Password:")
        self.labelPassword.grid(row=1, column=0)

        self.entryPassword = tk.Entry(master, show="*")
        self.entryPassword.grid(row=1, column=1)

        self.labelTo = tk.Label(master, text="To:")
        self.labelTo.grid(row=2, column=0)

        self.entryTo = tk.Entry(master)
        self.entryTo.grid(row=2, column=1)

        self.labelSubject = tk.Label(master, text="Subject:")
        self.labelSubject.grid(row=3, column=0)

        self.entrySubject = tk.Entry(master)
        self.entrySubject.grid(row=3, column=1)

        self.labelMessage = tk.Label(master, text="Message:")
        self.labelMessage.grid(row=4, column=0)

        self.entryMessage = tk.Text(master, height=5, width=30)
        self.entryMessage.grid(row=4, column=1)

        self.sendButton = tk.Button(master, text="Send Email", command=self.sendEmail)
        self.sendButton.grid(row=5, columnspan=2)

        self.receiveButton = tk.Button(
            master, text="Receive Email", command=self.receiveEmail
        )
        self.receiveButton.grid(row=6, columnspan=2)

        self.labelResult = tk.Label(master, text="")
        self.labelResult.grid(row=7, column=1)

    def sendEmail(self):
        email = self.entryEmail.get()
        password = self.entryPassword.get()
        to = self.entryTo.get()
        subject = self.entrySubject.get()
        message = self.entryMessage.get("1.0", tk.END)

        emailMessage = MIMEText(message)
        emailMessage["Subject"] = subject
        emailMessage["From"] = email
        emailMessage["To"] = to

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(email, password)
                text = emailMessage.as_string()
                server.sendmail(email, to, text)
            messagebox.showinfo("Success", "Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror(
                "Authentication Error",
                "Authentication failed. Please check your email and password.",
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def receiveEmail(self):
        clientEmail = self.entryEmail.get()
        password = self.entryPassword.get()

        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(clientEmail, password)
            mail.select("inbox")
            result, data = mail.search(None, "ALL")
            ids = data[0]  # data is a list.
            idList = ids.split()  # ids is a space separated string
            latestId = idList[-1]  # get the latest
            result, data = mail.fetch(
                latestId, "(RFC822)"
            )  # fetch the email body (RFC822) for the given ID

            for responsePart in data:
                if isinstance(responsePart, tuple):
                    msg = email.message_from_bytes(responsePart[1])
                    emailSubject = msg["subject"]
                    emailFrom = msg["from"]
                    payload = msg.get_payload(decode=True)
                    if payload is None:
                        emailBody = ""
                    else:
                        emailBody = payload.decode()
                    self.labelResult.config(
                        text=f"From: {emailFrom}\nSubject: {emailSubject}\nBody: {emailBody[:100]}..."
                    )

            mail.close()
            mail.logout()

        except Exception as e:
            self.labelResult.config(text=f"Failed to read email: {e}")


root = tk.Tk()
app = EmailClient(root)
root.mainloop()
