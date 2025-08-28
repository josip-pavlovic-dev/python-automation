"""
float() — Python Tutor template

1) Otvori https://pythontutor.com/python-visualize.html, nalepi kod i klikni RUN.
2) Pomiči korak-po-korak i prati kako vrednosti teku.
3) Zabeleži opažanja u *_analysis_notes.md.
4) Eksperimentiši sa različitim ulazima u float() i zabeleži šta se dešava."""

import math

print(float(3))
print(float("2.5"))
print(float("inf"))


print(0.1 + 0.2)
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))
