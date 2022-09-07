from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split #นำเข้าเครื่องมือที่จำเป็น

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0) #แบ่งข้อมูลโดยให้test_size เป็น 25%
