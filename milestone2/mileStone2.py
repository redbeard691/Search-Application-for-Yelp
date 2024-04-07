import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon, QPixmap
import psycopg2

qtCreatorFile = "milestone2App.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class milestone2(QMainWindow):
    def __init__(self):
        super(milestone2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStateList()
        self.ui.stateList.currentTextChanged.connect(self.stateChanged)
        self.ui.cityList.itemSelectionChanged.connect(self.cityChanged)
        self.ui.bname.textChanged.connect(self.getBusinessNames)
        self.ui.businesses.itemSelectionChanged.connect(self.displayBusinessCity)
        self.ui.zipList.itemSelectionChanged.connect(self.zipcodeChanged)
        self.ui.categoryList.itemSelectionChanged.connect(self.CategoryChanged)
    def executeQuery(self, sql_str):
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')

        cur = conn.cursor()
        cur.execute(sql_str)
        conn.commit()
        result = cur.fetchall()
        conn.close()
        return result

    def loadStateList(self):
        self.ui.stateList.clear()
        sql_str = "SELECT distinct state FROM business ORDER BY state;"
        try:
            result = self.executeQuery(sql_str)
            for row in result:
                self.ui.stateList.addItem(row[0])
        except:
            print("Query Failed1!")

        self.ui.stateList.setCurrentIndex(-1)
        self.ui.stateList.clearEditText()

    def stateChanged(self):
        self.ui.cityList.clear()
        state = self.ui.stateList.currentText()

        if self.ui.stateList.currentIndex() >= 0:
            sql_str = "SELECT distinct city FROM business WHERE state = '" + state + "' ORDER BY city;"
            try:
                result = self.executeQuery(sql_str)
                for row in result:
                    self.ui.cityList.addItem(row[0])

            except:
                print("Query Failed2!")

            for i in reversed(range(self.ui.businessTable.rowCount())):
                self.ui.businessTable.removeRow(i)
            sql_str = "SELECT name, city, state FROM business WHERE state = '" + state + "' ORDER BY name;"
            try:
                result = self.executeQuery(sql_str)
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(result[0]))
                self.ui.businessTable.setRowCount(len(result))
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'City', 'State'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 300)
                self.ui.businessTable.setColumnWidth(1, 100)
                self.ui.businessTable.setColumnWidth(2, 50)
                currentRowCount = 0
                for row in result:
                    for colCount in range(0, len(result[0])):
                        self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query has failed3!")

    def cityChanged(self):
        self.ui.zipList.clear()
        if (self.ui.stateList.currentIndex() >= 0) and (len(self.ui.cityList.selectedItems()) > 0):
            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            sql_str = ("SELECT DISTINCT name, city, state FROM business WHERE state ='" + state + "' AND city='" + city +
                       "' ORDER BY name;")
            sql_str2 = ("SELECT DISTINCT postal_code FROM business WHERE state ='" + state + "' AND city='" + city +
                        "' ORDER BY postal_code;")
            try:
                result = self.executeQuery(sql_str)
                zipCodes = self.executeQuery(sql_str2)
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(result[0]))
                self.ui.businessTable.setRowCount(len(result))
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'City', 'State'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 300)
                self.ui.businessTable.setColumnWidth(1, 100)
                self.ui.businessTable.setColumnWidth(2, 50)
                currentRowCount = 0
                for row in result:
                    for colCount in range(0, len(result[0])):
                        self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
                for row in zipCodes:
                    self.ui.zipList.addItem(row[0])
            except:
                print("Query has failed4!")

    def zipcodeChanged(self):
        self.ui.categoryList.clear()
        if (len(self.ui.cityList.selectedItems()) > 0) and (len(self.ui.zipList.selectedItems()) > 0):
            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            zip = self.ui.zipList.selectedItems()[0].text()
            sql_str = ("SELECT DISTINCT postal_code FROM business WHERE state ='" + state + "' AND city='" + city +
                       "' ORDER BY postal_code;")
            sql_str2 = ("SELECT DISTINCT c.cat_name FROM categories AS c, business AS b WHERE b.business_id = c.business_id AND state ='"
                        + state + "' AND city='" + city + "' AND postal_code = '" + zip +"' ORDER BY c.cat_name;")
            try:
                result = self.executeQuery(sql_str)
                categories = self.executeQuery(sql_str2)

                currentRowCount = 0
                for row in result:
                    for colCount in range(0, len(result[0])):
                       self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
                for row in categories:
                    self.ui.categoryList.addItem(row[0])
            except:
                print("ZipCode error: Query has failed!")

    def CategoryChanged(self):

        self.ui.businessTable.clear()
        #self.ui.categoryList.clear()
        if (len(self.ui.zipList.selectedItems()) > 0) and (len(self.ui.categoryList.selectedItems()) > 0):

            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            zipcode = self.ui.zipList.selectedItems()[0].text()
            category = self.ui.categoryList.selectedItems()[0].text()

            sql_str2 = ("SELECT DISTINCT b.name, c.cat_name, b.city, b.state FROM categories AS c, business AS b WHERE b.business_id = c.business_id AND state ='"
                        + state + "' AND city='" + city + "' AND postal_code = '" + zipcode + "' AND c.cat_name = '"
                        + category + "' ORDER BY c.cat_name;")
            try:
                result = self.executeQuery(sql_str2)

                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(result[0]))
                self.ui.businessTable.setRowCount(len(result))
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'City', 'State'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 300)
                self.ui.businessTable.setColumnWidth(1, 100)
                self.ui.businessTable.setColumnWidth(2, 50)

                currentRowCount = 0
                for row in result:

                    for colCount in range(0, len(result[0])):
                       self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
                for row in result:
                    self.ui.categoryList.addItem(row[1])
            except:
                print("ZipCode error: Query has failed!")

    def getBusinessNames(self):
        self.ui.businesses.clear()
        business_name = self.ui.bname.text()
        sql_str = "SELECT name From business WHERE name LIKE '%" + business_name + "%' ORDER BY name;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.businesses.addItem(row[0])
        except:
            print("BusinessNames Query failed!")

    def displayBusinessCity(self):
        business_name = self.ui.businesses.selectedItems()[0].text()
        sql_str = "SELECT city FROM business WHERE name = '" + business_name + "';"
        try:
            results = self.executeQuery(sql_str)
            self.ui.bCity.setText(results[0][0])
        except:
            print("displayBusinessCity Query failed!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = milestone2()
    window.show()
    sys.exit(app.exec_())
