from kivy.app import App
from kivy.uix.widget import Widget

#fullscreen
#from kivy.core.window import Window
#Window.fullscreen = True

class CalcWidget(Widget):
    def __init__(self):
        super().__init__()
        #allow only one operand & other magic variables
        self.operandUsed = False
        self.separatorUsed = False
        self.precision = 0
        self.highPrecision = 0

    #laskimen toiminnot tänne
    def btn_exit(self):
        exit()

    def btn_num(self, value):
        #if separator used use precision in calc
        if self.separatorUsed:
            self.precision += 1
        #use highest precision
        if self.precision > self.highPrecision:
            self.highPrecision = self.precision
        if self.ids.calc_input.text == "0" or "=" in self.ids.calc_input.text:
            self.ids.calc_input.text = str(value)
        else:
            self.ids.calc_input.text += str(value)

    #insert separator
    #TODO: , or . based on locale
    def btn_dot(self):
        self.separatorUsed = True
        #use highest precision
        if self.precision > self.highPrecision:
            self.highPrecision = self.precision
        #only one dot at time
        if self.ids.calc_input.text[-1] != ".":
            self.ids.calc_input.text += "."

    #insert operand for calculation
    def btn_operand(self, value):
        if not self.operandUsed:
            self.ids.calc_input.text += str(value)
            self.operandUsed = True

    #clear input
    def btn_c(self):
        self.resetMagic()
        #reset input field
        self.ids.calc_input.text = ""

    #delete last added char
    def btn_ce(self):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]

    #negate number
    def btn_negate(self):        
        if not self.operandUsed:
            self.ids.calc_input.text = str(int(self.ids.calc_input.text)*-1)

    def btn_calculate(self):
        try:
            res = eval(self.ids.calc_input.text)
            if res:
                if self.highPrecision > 0:
                    res = round(res, self.highPrecision)

            self.ids.calc_input.text += " = " + str(res)
        except SyntaxError:
            self.ids.calc_input.text = "err"
        except NameError:
            self.ids.calc_input.text = "errkele!"
        self.resetMagic()
    
    #reset magic
    def resetMagic(self):
        self.operandUsed = False
        self.separatorUsed = False
        self.precision = 0
        self.highPrecision = 0

#main class same ass apps filename
class Calculator(App):
    def build(self):
        return CalcWidget()


if __name__ == '__main__':
    Calculator().run()