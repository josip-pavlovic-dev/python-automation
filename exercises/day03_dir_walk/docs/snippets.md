# 🧩 Code Snippets | _Kod primeri_

## 📌 Get current time | _Dobavi trenutno vreme_

```python
from datetime import datetime

now = datetime.now()
print(now)  # 2025-07-29 14:23:01
```

## 📌 Format timestamp | _Formatiraj vremensku oznaku_

```python
formatted = now.strftime("%Y-%m-%d_%H-%M-%S")
print(formatted)  # 2025-07-29_14-23-01
```

## 📌 Datetime from timestamp | _Datum iz vremenske oznake_

```python
from datetime import datetime
timestamp = 1627557890
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)
```

## 📌 Subtract N days | _Oduzmi N dana_

```python
from datetime import datetime, timedelta

seven_days_ago = datetime.now() - timedelta(days=7)
print(seven_days_ago)
```

## 📌 Parse date string | _Parsiranje stringa u datum_

```python
from datetime import datetime

date_string = "2025-07-29 10:30:00"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(dt)
```

---
