text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
lpos = text.find('5')
fval = float(text[pos:lpos+1])
print(fval)
