import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QComboBox, QTextEdit, QVBoxLayout, QWidget, \
    QAbstractItemView
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    people = [{"name": "John", "age": 32, "address": "ABC"},
              {"name": "Maria", "age": 54, "address": "DEF"}]
    data = [
        ("AA", "BB", "CC"),
        ("DD", "EE", "FF")
    ]
    # Initialize an empty list
    objects_list = []

    def __init__(self):
        super(MainWindow, self).__init__()
        # loadUi("tablesample.ui", self)
        loadUi("simulator.ui", self)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 500)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color:gray}")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section { background-color:gray}")
        # Set selection mode to allow selecting entire rows
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Set fixed height for the QTableWidget
        self.tableWidget.setFixedHeight(600)  # Set the desired height in pixels
        self.loaddata()
        self.pushButton_2.clicked.connect(self.run_now)
        self.pushButton.clicked.connect(self.resched)
        self.pushButton_3.clicked.connect(self.add_row)

    def loaddata(self):
        # row = 0

        self.tableWidget.setRowCount(len(self.data))
        # Iterate over the data and populate the table widget
        for row, (recoveryId, payload, messageId) in enumerate(self.data):
            # Create an instance of DTOTableWidgetItem
            dto_item = DTOTableWidgetItem(recoveryId, payload, messageId)
            # Set data in QTableWidgetItem
            text_edit0 = QTextEdit(dto_item.recoveryId)
            text_edit0.setFixedWidth(200)  # Set fixed width
            text_edit1 = QTextEdit(dto_item.payload)
            text_edit1.setFixedWidth(500)  # Set fixed width
            text_edit2 = QTextEdit(dto_item.messageId)
            text_edit2.setFixedWidth(200)  # Set fixed width

            self.tableWidget.setCellWidget(row, 0, text_edit0)
            self.tableWidget.setCellWidget(row, 1, text_edit1)
            self.tableWidget.setCellWidget(row, 2, text_edit2)
            # self.tableWidget.resizeRowsToContents()
            # self.tableWidget.setItem(row, 2, text_edit)
            # Auto resize rows to fit contents

        # self.tableWidget.setRowCount(len(self.people))

        '''
        for person in self.people:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["age"])))
            self.tableWidget.setCellWidget(row, 2, comboBoxStatus(self.tableWidget))
            #self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person["address"]))
            #self.tableWidget.setItem(row, 2, QtWidgets.QComboBox)
            row += 1
        '''

        # updated_text = "Updated Data"
        # updated_item = QTableWidgetItem(updated_text)

        # Set the new item at the specified row and column
        # self.tableWidget.setItem(0, 1, updated_item)

    def run_now(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        print("selected rows:", selected_rows)
        cell_widget0 = self.tableWidget.cellWidget(selected_rows[0].row(), 0)
        cell_widget1 = self.tableWidget.cellWidget(selected_rows[0].row(), 1)
        cell_widget2 = self.tableWidget.cellWidget(selected_rows[0].row(), 2)
        print("cell widget0:", cell_widget0.toPlainText(),
              ", cell widget1:", cell_widget1.toPlainText(),
              ", cell widget2:", cell_widget2.toPlainText())


        '''        
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        print(selected_rows)
        print(f"SelectRows: ", type(selected_rows))
        if selected_rows:
            for row in selected_rows:
                row_index = row.row()
                row_items = []
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row_index, col)
                    print(item)
                    #if item is not None:
                    #    row_items.append(item.text())
                    #else:
                    #    row_items.append("")  # If cell is empty
                print(f"Data of selected row {row_index}: {item}")
        else:
            print("No items selected.")
        '''

    def resched(self):
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        print("Shortcut to get Selected Row:", selected_rows[0].row())
        if selected_rows:
            for row in selected_rows:
                print(f"Selected row: {row.row()}")
        else:
            print("No items selected.")

    def add_row(self):
        line_edit_0 = QTextEdit()
        line_edit_0.setFixedWidth(200)  # Set fixed width
        line_edit_1 = QTextEdit()
        line_edit_0.setFixedWidth(200)  # Set fixed width

        # Determine the current row count
        current_row_count = self.tableWidget.rowCount()

        # Insert a new row at the end of the table
        self.tableWidget.insertRow(current_row_count)

        # Populate the new row with empty items or default values
        for col in range(2):
            self.tableWidget.setCellWidget(current_row_count, 0, line_edit_0)
            self.tableWidget.setCellWidget(current_row_count, 1, line_edit_1)
            text_edit = QTextEdit("")
            text_edit.setFixedWidth(200)  # Set fixed width
            self.tableWidget.setCellWidget(current_row_count, 2, text_edit)


class comboBoxStatus(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 15px')
        self.addItems(['Scheduled', 'Cancelled', 'Triggered'])
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())


class DTOTableWidgetItem:
    def __init__(self, recoveryId, payload, messageId):
        self.recoveryId = recoveryId
        self.payload = payload
        self.messageId = messageId


# renames the instances of the model
# with their title name
def __str__(self):
    return self.title


# main
app = QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
