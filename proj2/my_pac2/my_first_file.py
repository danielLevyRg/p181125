class coures:
    def __init__(self):
        self.study_meterials = "Rules of conduct on campus"

    def info(self):
        print("my meterials books is : {}".format(self.study_meterials))

class QA_automation(coures):
    def __init__(self):
        super().__init__()
        self.study_meterials = "Automation books"
        self.management_tools = "QC"

    def info(self):
        print(f"my meterials books is : {self.study_meterials}")

s1 = QA_automation()
s1.info()  # מדפיס "my meterials books is : Automation books"

# להפעיל את הפונקציה info() של coures
s2 = coures()
s2.info()  # מדפיס "my meterials books is : Rules of conduct on campus"
