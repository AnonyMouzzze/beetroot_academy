from functools import partial

class CalculatorControll:
    def __init__(self, view: 'MainWindow'):
        self._view = view
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == 'ERROR':
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for buttonText, button in self._view.buttons.items():
            if buttonText not in {'=', 'C'}:
                button.clicked.connect(partial(self._buildExpression, buttonText))
        
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

    def _evaluateExpression(self, expression):
        try:
            result = str(eval(expression))
        except Exception:
            result = 'ERROR'
        return result
    
    def _calculateResult(self):
        result = self._evaluateExpression(self._view.displayText())
        self._view.setDisplayText(result)