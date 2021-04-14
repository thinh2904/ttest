import numpy as np
import random
import scipy
from scipy import stats



#Sinh ngẫu nhiên 20 mẫu tuân theo phân phối chuẩn có trung bình mẫu là 1 và độ lệch chuẩn là 0.1
mean = 1
std = 0.1
N = 20
samples = np.random.normal(mean, std, N)
print(samples)


#Kiểm định 2 đuôi
t_test_score1, p_value1 = scipy.stats.ttest_1samp(samples, 1, axis=0, nan_policy='propagate', alternative='two-sided')
print('t_test_score1=', t_test_score1)
print('p_value1=', p_value1)
if(p_value1<0.05):
  print("Có bằng chứng để bác bỏ giả thuyết H0")
else:
  print("Chưa có bằng chứng để bác bỏ giả thuyết H0")


#Kiểm định 1 đuôi với điều kiện lớn hơn
t_test_score2, p_value2 = scipy.stats.ttest_1samp(samples, 1, axis=0, nan_policy='propagate', alternative='greater')
print('t_test_score2 = ', t_test_score2)
print('p_value2 = ', p_value2)
if(p_value2<0.05):
  print("Có bằng chứng để bác bỏ giả thuyết H0")
else:
  print("Chưa có bằng chứng để bác bỏ giả thuyết H0")


#Kiểm định 1 đuôi với điều kiện nhỏ hơn cũng tương tự, chỉ thay thế greater thành less
