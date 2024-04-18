import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
import smtplib


class EmailClient:
    def __init__(self, master):
        self.master = master
        master.title("Email Client")

        self.label_email = tk.Label(master, text="Email:")
        self.label_email.grid(row=0, column=0)

        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=0, column=1)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=1, column=0)

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=1, column=1)

        self.label_to = tk.Label(master, text="To:")
        self.label_to.grid(row=2, column=0)

        self.entry_to = tk.Entry(master)
        self.entry_to.grid(row=2, column=1)

        self.label_subject = tk.Label(master, text="Subject:")
        self.label_subject.grid(row=3, column=0)

        self.entry_subject = tk.Entry(master)
        self.entry_subject.grid(row=3, column=1)

        self.label_message = tk.Label(master, text="Message:")
        self.label_message.grid(row=4, column=0)

        self.entry_message = tk.Text(master, height=5, width=30)
        self.entry_message.grid(row=4, column=1)

        self.send_button = tk.Button(master, text="Send Email", command=self.send_email)
        self.send_button.grid(row=5, columnspan=2)

    def send_email(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        to = self.entry_to.get()
        subject = self.entry_subject.get()
        message = self.entry_message.get("1.0", tk.END)

        emailMessage = MIMEText(message)
        emailMessage["Subject"] = subject
        emailMessage["From"] = email
        emailMessage["To"] = to

        try:
            with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
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


root = tk.Tk()
app = EmailClient(root)
root.mainloop()
