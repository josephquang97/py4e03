# Assignment 03 - Functions


## Tiếng Việt

### Yêu cầu:

Viết một **chương trình con** để tính tiền chi trả cho nhân viên với hai thông số đầu vào là số giờ công (*hours*) và số tiền phải trả cho mỗi giờ (*rate*). Với điều kiện nếu nhân viên làm việc trên 40 tiếng thì 40 tiếng đầu chi phí sẽ giống như quy định, những giờ sau đó sẽ tăng lên gấp rưỡi. Tên chương trình con phải đặt theo quy ước là `calculate_price`.

```python
def calculate_price(hours: float, rate: float) -> float:
    price = 0
    ...
    return price
```

### Ví dụ:

```
Nhập số giờ: 45
Nhập số tiền mỗi giờ: 3

Số tiền phải trả là: 142.5
```

### Chú ý:

- Học sinh chỉ được phép chỉnh sửa trên file main.py để hoàn thành yêu cầu của bài tập
- Học sinh không được phép thay đổi tên file
- Tên biến phải đặt theo quy ước là (*hours*, *rate* và *price*)
- Học sinh phải tự làm bài tập này

## English version

### Requirement:

Rewrite your pay computation with time-and-a-half for overtime and create a function called `calculate_price()` which takes two parameters ( *hours* and *rate*) as the following.

```python
def calculate_price(hours: float, rate: float) -> float:
    price = 0
    ...
    return price
```

### For example:

```
Enter hours: 45
Enter rate: 3

The price: 142.5
```

### Note:

- Only edit the main.py file to complete the requirements of the exercise
- Do not change change the file name
- Variable names must be set by convention (hours, rate and price)
- Must do this exercise by yourself
