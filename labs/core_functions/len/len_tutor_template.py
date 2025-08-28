    """
    len() — Python Tutor template

    1) Otvori https://pythontutor.com/python-visualize.html, nalepi kod i klikni RUN.
    2) Pomiči korak-po-korak i prati kako vrednosti teku.
    3) Zabeleži opažanja u *_analysis_notes.md.
    """

    print(len('hello'))
print(len([1,2,3]))

class Box:
    def __init__(self, n): self.n = n
    def __len__(self): return self.n
print(len(Box(4)))

