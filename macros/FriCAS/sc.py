import console.Console as cc
s=cc(view)
l=s.getOutput().getDocument().getLength()
txt=s.getOutput().getDocument().getText(1,l)

textArea = view.getTextArea()
caret = textArea.getCaretPosition()
#lines = textArea.getText().split('\n')
textArea.goToBufferEnd(0)
endcaret = textArea.getCaretPosition()
textArea.getBuffer().insert(endcaret, txt)
#Go back to the original cursor position:
textArea.setCaretPosition(caret)



