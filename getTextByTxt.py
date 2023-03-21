from pathlib import Path
#def getTextFromTxt(txtFile):
#    txt = Path(txtFile).read_text()
#    return txt

def getTextFromTxt(txtFile):
    try:
        with open(txtFile, encoding='utf8') as f:
            allText = []
            for line in f:
                allText.append(line)
            return "".join(allText)
    except:
        txt = Path(txtFile).read_text()
        return txt


