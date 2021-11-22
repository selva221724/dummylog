from subprocess import Popen, PIPE


def addressProcessor(collatedAddress):
    collatedAddress = collatedAddress.split('Result:\n\n')[1].split('\n\n> ')[0].replace('\n', '')
    collatedAddress = eval(collatedAddress)
    return collatedAddress


def removeSpecialChars(address):
    tags = {'≈': '', '≠': '', '>': '', '<': '', '+': '', '≥': '', '≤': '', '±': '', '*': '', '÷': '', '√': '',
            '°': '', '⊥': '', '~': '', 'Δ': '', 'π': '', '≡': '', '≜': '', '∝': '', '∞': '', '≪': '', '≫': '',
            '⌈': '', '⌉': '', '⌋': '', '⌊': '', '∑': '', '∏': '', 'γ': '', 'φ': '', '⊃': '', '⋂': '', '⋃': '',
            'μ': '', 'σ': '', 'ρ': '', 'λ': '', 'χ': '', '⊄': '', '⊆': '', '⊂': '', '⊇': '', '⊅': '', '⊖': '',
            '∈': '', '∉': '', '⊕': '', '⇒': '', '⇔': '', '↔': '', '∀': '', '∃': '', '∄': '', '∴': '', '∵': '',
            'ε': '', '∫': '', '∮': '', '∯': '', '∰': '', 'δ': '', 'ψ': '', 'Θ': '', 'θ': '', 'α': '', 'β': '',
            'ζ': '', 'η': '', 'ι': '', 'κ': '', 'ξ': '', 'τ': '', 'ω': '', '∇': ''}
    for i, j in tags.items():
        address = address.replace(i, j)
    return address


class AddressParser:

    def __init__(self):
        self.exePath = r"C:\Workbench\libpostal\src\address_parser.exe"
        self.process = Popen(self.exePath, shell=False, universal_newlines=True,
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)
        pass

    def runParser(self, address):
        address = removeSpecialChars(address)
        address = address + ' \n'
        self.process.stdin.write(address)
        self.process.stdin.flush()

        result = ''
        for line in self.process.stdout:
            if line == '}\n':
                result += line
                break
            result += line
        return addressProcessor(result)

    def terminateParser(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait(timeout=0.2)

# lp = AddressParser()
# parsedAddress = lp.runParser('number 2 , flat 3 , kunju rd, Mumbai, India')

# parser = pypostalwin.AddressParser()
# parser.runParser("Input Your Address Here")
