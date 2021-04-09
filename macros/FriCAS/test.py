textArea = view.getTextArea()
caret = textArea.getCaretPosition()
lines = textArea.getText().split('\n')
textArea.goToBufferEnd(0)
endcaret = textArea.getCaretPosition()
textArea.getBuffer().insert(endcaret, "na sowas ...")
#Go back to the original cursor position:
textArea.setCaretPosition(caret)
