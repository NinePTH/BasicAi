from sklearn import datasets #นำเข้าข้อมูลสำหรับสร้างโมเดล
digits = datasets.load_digits() #ดึงdigitsออกมา
x = digits.data #เอาข้อมูล(Features)ไปเก็บใน x
y = digits.target #เอาคำตอบ(Target)ไปเก็บใน y
print(digits.target_names)
print(digits.feature_names)
