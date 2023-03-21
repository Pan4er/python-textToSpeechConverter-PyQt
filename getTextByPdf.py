import PyPDF2

def getTextFromPdf(pdf):
    allText = []
    with open(pdf, "rb") as f:
        pdfReader = PyPDF2.PdfReader(f, strict=False)
        for page in pdfReader.pages:
            tmp = page.extract_text()
            allText.append(tmp)

    return "".join(allText)


