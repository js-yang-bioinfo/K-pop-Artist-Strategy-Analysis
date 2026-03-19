import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\rank data.xlsx'
df = pd.read_excel(file_path)

font_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\BMJUA_ttf.ttf'  # 사용 가능한 한글 폰트 경로로 변경
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())

# 'Unnamed: 0'을 인덱스로 설정
df.set_index('Unnamed: 0', inplace=True)

# 각 행에 대해 최빈값, 중앙값, 평균값 계산
mode = df.apply(lambda x: x.mode().iloc[0], axis=1)  # 최빈값이 여러 개일 경우 첫 번째 값을 사용
median = df.median(axis=1)
mean = df.mean(axis=1).round(0)

# distribution 값을 설정하는 함수
def set_distribution(row):
    if row['Mode'] < row['Median'] < row['Mean']:
        return 1
    elif row['Mode'] > row['Median'] > row['Mean']:
        return 0
    else:
        return 2

# 왜도값 계산
skewness = df.apply(lambda x: skew(x.dropna()), axis=1)

# 결과를 담을 데이터프레임 생성
data = pd.DataFrame({
    'Artist': df.index,
    'Mode': mode,
    'Median': median,
    'Mean': mean,
    'Skewness': skewness
})

# distribution 컬럼 추가
data['distribution'] = data.apply(set_distribution, axis=1)

# skewness_label 컬럼 추가
def skewness_label(value):
    if pd.isna(value) or value == 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

data['skewness_label'] = data['Skewness'].apply(skewness_label)

# scatter plot 생성
colors = {1: 'orange', 0: 'skyblue', -1: 'violet'}
plt.figure(figsize=(15, 8))
plt.scatter(data.index, data['Skewness'], c=data['skewness_label'].apply(lambda x: colors[x]), s=50)
plt.xlabel('아티스트명', fontsize=12)
plt.ylabel('왜도', fontsize=12)
plt.title('왜도 그래프', fontsize=15)
plt.xticks(rotation=90, fontsize=8)  # x축 레이블 회전 및 글꼴 크기 조정

# x축 레이블 간격 설정
n = len(data.index)
plt.xticks(range(0, n, max(1, n // 20)), data['Artist'][::max(1, n // 20)], rotation=90, fontsize=8)

plt.grid(True)
plt.tight_layout()  # 레이아웃 자동 조정
plt.show()

# 데이터프레임 확인

new = pd.DataFrame()

new['음원 분포 1단계'] = data[data['skewness_label'] == -1]['Artist'].reset_index(drop=True)
new['음원 분포 2단계'] = data[data['skewness_label'] == 0]['Artist'].reset_index(drop=True)
new['음원 분포 3단계'] = data[data['skewness_label'] == 1]['Artist'].reset_index(drop=True)

# 새로운 엑셀 파일로 저장
new_output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\skewness_classification2.xlsx'
new.to_excel(new_output_file_path, index=False)

# 엑셀 파일로 저장
output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\avg_mode_median_skewness2.xlsx'
data.to_excel(output_file_path, index=False)
