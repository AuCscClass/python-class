from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTimeEdit, QComboBox, QListWidget, QHBoxLayout, QCalendarWidget, QMessageBox
from PyQt5.QtCore import QTime, QTimer, Qt, QDate
from PyQt5.QtGui import QFont
import sys 
import pygame

#this defines the whole funtions to be used in the program
class Alarm:
    def __init__(self, time, sound, category, days):
        self.time = time
        self.sound = sound
        self.category = category
        self.days = days
        self.snooze_duration =  10 * 1000  # Default snooze duration is 10 seconds

#this defines the code funtions and the GUI system and how it works with the main class which is alarm.
class AlarmApp(QWidget):
    def __init__(self):
        super().__init__()
#
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_alarms)

        self.alarmTime = QTimeEdit(self)
        self.alarmTime.setDisplayFormat("hh:mm A")
        self.alarmTime.setTime(QTime.currentTime())
#Dropbox menu for the alarm osund
        self.soundSelection = QComboBox(self)
        self.soundSelection.addItems(["homecoming.mp3", "default_iphone_alarm.mp3", "samsung_ringtone.mp3"])  # Add your sound options here
#Dropbox menu for category
        self.categorySelection = QComboBox(self)
        self.categorySelection.setEditable(True)
        self.categorySelection.addItems(["Work", "Personal", "Reminder", "Sleep"])  # Add your category options here

        self.calendar = QCalendarWidget(self)
#the button display and titles
        self.alarmButton = QPushButton('Set Alarm', self)
        self.alarmButton.clicked.connect(self.add_alarm)

        self.stopButton = QPushButton('Stop Alarm', self)
        self.stopButton.clicked.connect(self.stop_alarm)
        self.stopButton.setEnabled(False)

        self.snoozeButton = QPushButton('Snooze Alarm', self)
        self.snoozeButton.clicked.connect(self.snooze_alarm)
        self.snoozeButton.setEnabled(False)
#The display menu or the empty box down used for display
        self.alarmList = QListWidget(self)
        self.alarmList.setFixedHeight(100)

        self.alarmLabel = QLabel("Set Alarms...")

#the GUI layout for widgets [vertical buttons]
        vbox = QVBoxLayout()
        vbox.addWidget(self.alarmTime)
        vbox.addWidget(self.soundSelection)
        vbox.addWidget(self.categorySelection)
        vbox.addWidget(self.calendar)
        vbox.addWidget(self.alarmButton)
        vbox.addWidget(self.stopButton)
        vbox.addWidget(self.snoozeButton)
        vbox.addWidget(self.alarmLabel)
        vbox.addWidget(self.alarmList)

        self.setLayout(vbox)

        self.alarms = []
        pygame.mixer.init()

        self.setWindowOpacity(1.0)
#the add_alarm fucntion for most of the program to set up the alarm functions.
    def add_alarm(self):
        alarm_time = self.alarmTime.time()
        alarm_time.setHMS(alarm_time.hour(), alarm_time.minute(), 0, 0)
        sound = self.soundSelection.currentText()  # Get the selected sound
        category = self.categorySelection.currentText()  # Get the selected category
        selected_date = self.calendar.selectedDate()
        alarm_days = [selected_date.dayOfWeek()]
        self.alarms.append(Alarm(alarm_time, sound, category, alarm_days))
        alarm_info = f"Alarm set for {alarm_time.toString()} for {category} on {selected_date.longDayName(selected_date.dayOfWeek())}"
        self.alarmList.addItem(alarm_info)
        self.timer.start(12000)  #Alarm sound duration in milliseconds

#The stop button function
    def stop_alarm(self):
        pygame.mixer.music.stop()
        self.timer.stop()
        self.stopButton.setEnabled(False)
        self.snoozeButton.setEnabled(False)
        self.alarmLabel.setText("")
#check alarm fucntion check the time and date and also works as the sound trigger if the set alarm matches the current time and date
    def check_alarms(self):
        current_time = QTime.currentTime()
        current_day = QDate.currentDate().dayOfWeek()
        for alarm in self.alarms:
            if current_time >= alarm.time and current_day in alarm.days:
                pygame.mixer.music.load(alarm.sound)  # Load the selected sound file
                pygame.mixer.music.play()  # Play the sound file
                self.stopButton.setEnabled(True)
                self.snoozeButton.setEnabled(True)
#snoozes the alarm for 10 seconds
    def snooze_alarm(self):
        pygame.mixer.music.stop()
        self.alarmLabel.setText("Snoozing...")
        QTimer.singleShot(self.alarms[0].snooze_duration, self.check_alarms)  # Snooze for specified duration

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AlarmApp()
    main.show()
    sys.exit(app.exec_())