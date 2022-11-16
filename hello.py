import ui

def clear_text(sender):
	'@type sender: ui.Button'
	sender.superview['textfield1'].text = ''

v = ui.load_view()
v.present('sheet')
