import csv
import os
from PyQt6.QtWidgets import QMainWindow
from gui import Ui_VotingApplication

CSV_FILE = "votes.csv"

def ensure_csv_exists():
    """Creates the CSV file with headers if it does not exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Candidate"])

def id_exists(voter_id: str) -> bool:
    """Returns True if the ID has already voted."""
    ensure_csv_exists()

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row and row[0] == voter_id:
                return True
    return False

def save_vote(voter_id: str, candidate: str):
    """Saves the vote to the CSV file."""
    ensure_csv_exists()

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, candidate])

class LogicWindow(QMainWindow, Ui_VotingApplication):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.submit_vote)

    def reset_radio_buttons(self):
        """Forcefully unselects both radio buttons after a successful vote."""
        self.buttonGroup.setExclusive(False)

        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)

        self.buttonGroup.setExclusive(True)

    def submit_vote(self):
        voter_id = self.lineEdit.text().strip()

        candidate = None
        if self.radioButton.isChecked():
            candidate = "John"
        elif self.radioButton_2.isChecked():
            candidate = "Jane"

        if not voter_id.isdigit():
            self.label.setText("Enter 5 Digit ID")
            self.label.setStyleSheet("color: red;")
            return

        if len(voter_id) != 5:
            self.label.setText("Enter 5 Digit ID")
            self.label.setStyleSheet("color: red;")
            return

        if candidate is None:
            self.label.setText("Select Candidate")
            self.label.setStyleSheet("color: red;")
            return

        if id_exists(voter_id):
            self.label.setText("Already Voted")
            self.label.setStyleSheet("color: red;")
            return

        save_vote(voter_id, candidate)

        self.label.setText("Enter 5 Digit ID")
        self.label.setStyleSheet("color: white;")

        self.lineEdit.clear()
        self.reset_radio_buttons()
