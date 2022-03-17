from tkinter import *
from tkinter.font import Font


root = Tk()
root.title('Calculator')
root.resizable(False, False)

font = Font(family='Helvetica', size=15)
root.option_add("*Font", font)

entry = Entry(
    root,
    width=40,
    highlightbackground='#FFAF33',
    borderwidth=1,
    highlightthickness=0,
    justify='right'
)
entry.grid(row=0, column=0, columnspan=4, pady=13)
entry.configure(font=font)

_operand_1 = str()
_operand_2 = str()
_operator = str()
_result = str()

def operand(number):
    global _operator
    if _result == 0.0:
        entry.delete(0, END)
    if not _operator:
        root.clipboard_append(number)
        entry.insert(END, number)
        return 0
    root.clipboard_append(number)
    entry.insert(END, number)
    return 0

def operator(input_operator):
    global _operator
    global _operand_1
    if _result:
        _operand_1 = _result
    elif _result == 0.0:
        _operand_1 = _result
    elif not _result:
        _operand_1 = root.clipboard_get()
    root.clipboard_clear()
    entry.delete(0, END)
    _operator = input_operator

def operation():
    global _operand_1
    global _operand_2
    global _operator
    global _result
    _operand_2 = float(root.clipboard_get())
    _operand_1 = float(_operand_1)
    result = float()
    if _operator == '+':
        result = _operand_1 + _operand_2
    elif _operator == '-':
        result = _operand_1 - _operand_2
    elif _operator == 'x':
        result = _operand_1 * _operand_2
    elif _operator == '÷':
        if _operand_2 > 0.0:
            result = _operand_1 / _operand_2
        else:
            result = '0.0'
    elif _operator == '%':
        if _operand_2 > 0.0:
            result = _operand_1 % _operand_2
        else:
            result = '0.0'
    clear()
    _result = result
    entry.insert(0, result)

def clear():
    entry.delete(0, END)
    global _operand_1
    global _operand_2
    global _operator
    global _result
    _operand_1 = str()
    _operand_2 = str()
    _operator = str()
    _result = str()
    root.clipboard_clear()

btn_1 = Button(root, text='1', padx=25, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('1'))
btn_2 = Button(root, text='2', padx=27, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('2'))
btn_3 = Button(root, text='3', padx=23, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('3'))
btn_5 = Button(root, text='5', padx=27, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('5'))
btn_4 = Button(root, text='4', padx=25, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('4'))
btn_6 = Button(root, text='6', padx=23, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('6'))
btn_7 = Button(root, text='7', padx=25, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('7'))
btn_8 = Button(root, text='8', padx=27, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('8'))
btn_9 = Button(root, text='9', padx=23, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('9'))
btn_0 = Button(root, text='0', padx=78, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operand('0'))
btn_decimal = Button(root, text='.', padx=27, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda :operand('.'))

btn_plus = Button(root, text='+', padx=17, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operator('+'))
btn_minus = Button(root, text='−', padx=17, pady=17, highlightbackground='#FFAF33', fg='black', command=lambda: operator('-'))
btn_multiply = Button(root, text='x', padx=17, pady=15, highlightbackground='#FFAF33', fg='black', command=lambda: operator('x'))
btn_divide = Button(root, text='÷', padx=23, pady=15, highlightbackground='#FFAF33', fg='black', command=lambda: operator('÷'))
btn_modulo = Button(root, text='%', padx=25, pady=15, highlightbackground='#FFAF33', fg='black', command=lambda: operator('%'))
btn_clear = Button(root, text='AC', padx=19, pady=15, highlightbackground='#FFAF33', fg='black', command=clear)
btn_equal_to = Button(root, text='=', padx=17, pady=48, highlightbackground='#FFAF33', fg='black', command=operation)

btn_clear.grid(row=1, column=0)
btn_modulo.grid(row=1, column=1)
btn_divide.grid(row=1, column=2)
btn_multiply.grid(row=1, column=3)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_minus.grid(row=2, column=3)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_plus.grid(row=3, column=3)

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_equal_to.grid(row=4, column=3, rowspan=2)

btn_0.grid(row=5, column=0, columnspan=2)
btn_decimal.grid(row=5, column=2)

root.mainloop()