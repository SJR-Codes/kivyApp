from kivy.app import App
from kivy.uix.widget import Widget

class CalcWidget(Widget):
    def __init__(self):
        super().__init__()
        #allow only one operand
        self.operandUsed = False

    #laskimen toiminnot tänne
    def btn_exit(self):
        exit()

    def btn_num(self, value):
        if self.ids.calc_input.text == "0" or "=" in self.ids.calc_input.text:
            self.ids.calc_input.text = str(value)
        else:
            self.ids.calc_input.text += str(value)

    def btn_dot(self):
        if self.ids.calc_input.text[-1] != ".":
            self.ids.calc_input.text += "."

    def btn_operand(self, value):
        if not self.operandUsed:
            self.ids.calc_input.text += str(value)
            self.operandUsed = True

    def btn_c(self):
        self.ids.calc_input.text = ""

    def btn_negate(self):        
        if not self.operandUsed:
            self.ids.calc_input.text = str(int(self.ids.calc_input.text)*-1)

    def btn_calculate(self):
        self.operandUsed = False
        try:
            res = eval(self.ids.calc_input.text)
            self.ids.calc_input.text += " = " + str(res)
        except SyntaxError:
            self.ids.calc_input.text = "err"
    

#main class same ass apps filename
class Calculator(App):
    def build(self):
        return CalcWidget()


if __name__ == '__main__':
    Calculator().run()