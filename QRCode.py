import qrcode
import PySimpleGUI as sg


layout = [
    [sg.Text('Enter the text to generate QR Code:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Generate QR Code'), sg.Button('Exit')]
]

window = sg.Window('QR Code Generator App', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Generate QR Code':
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(values['-INPUT-'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='blue', back_color='white')
        
        
        filename = 'qrcode.png'
        img.save(filename)
        
        

window.close()
