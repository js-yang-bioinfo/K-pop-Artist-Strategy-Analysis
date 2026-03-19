import pandas as pd
from scipy.stats import skew

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\rank data.xlsx'
df = pd.read_excel(file_path)

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

# 데이터프레임 확인
print(data)

# 엑셀 파일로 저장
output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\avg_mode_median_skewness.xlsx'
data.to_excel(output_file_path, index=False)
