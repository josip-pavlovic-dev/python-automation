# len_tutor.py — fokus: __len__ pravila i greške
print(len([]), bool([]))  # 0, False
print(len([0]), bool([0]))  # 1, True


class BadLen:
    def __len__(self):
        return -1


try:
    len(BadLen())
except Exception as e:
    print("BadLen:", type(e).__name__)  # ValueError
