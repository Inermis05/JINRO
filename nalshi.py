import numpy as np
import matplotlib.pyplot as plt

# 0.5시간 간격 시간 데이터 (0시 ~ 23.5시)
interp_hours = np.arange(0, 24, 0.5)
interp_temps = np.array([18. , 17.5, 17. , 17. , 17. , 17. , 17. , 16.5, 16. , 15.5, 15. ,
                         15. , 15. , 16. , 17. , 18. , 19. , 20. , 21. , 21.5, 22. , 23. ,
                         24. , 25. , 26. , 26.5, 27. , 27.5, 28. , 28. , 28. , 28. , 28. ,
                         28. , 28. , 27.5, 27. , 26. , 25. , 23.5, 22. , 21.5, 21. , 20. ,
                         19. , 18.5, 18. , 18. ])

# 중심 차분 함수
def central_diff(y, h=0.5):
    dydx = np.zeros_like(y)
    dydx[0] = (y[1] - y[0]) / h
    dydx[-1] = (y[-1] - y[-2]) / h
    for i in range(1, len(y)-1):
        dydx[i] = (y[i+1] - y[i-1]) / (2 * h)
    return dydx

# 1차, 2차, 3차 도함수
first = central_diff(interp_temps)
second = central_diff(first)
third = central_diff(second)

# 기준점: 정오 = 12시 (x=12.0)
x0 = 12.0
x0_idx = np.where(interp_hours == x0)[0][0]
y0 = interp_temps[x0_idx]
dy = first[x0_idx]
ddy = second[x0_idx]
dddx = third[x0_idx]

# 테일러 3차 근사 함수
def taylor_3rd(x, x0, y0, dy, ddy, dddx):
    return y0 + dy*(x - x0) + (ddy/2)*(x - x0)**2 + (dddx/6)*(x - x0)**3

# 근사 범위: 10시 ~ 14시
x_range = np.linspace(10, 14, 100)
actual_vals = np.interp(x_range, interp_hours, interp_temps)
taylor_vals = taylor_3rd(x_range, x0, y0, dy, ddy, dddx)

# 시각화
plt.figure(figsize=(10, 6))
plt.plot(x_range, actual_vals, label="실제 온도")
plt.plot(x_range, taylor_vals, '--', label="3차 테일러 근사 (12시 기준)")
plt.scatter([x0], [y0], color='red', label="정오 기준점")
plt.xlabel("시간")
plt.ylabel("기온 (°C)")
plt.title("기온의 3차 테일러 다항식 근사")
plt.legend()
plt.grid(True)
plt.show()
