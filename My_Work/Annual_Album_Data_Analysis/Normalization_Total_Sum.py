import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Individual album data.xlsx'
data = pd.read_excel(file_path)

# 아티스트 이름 정리 (양쪽 공백 제거)
data['artist'] = data['artist'].str.strip()

# artist별 행의 개수 세기
artist_counts = data['artist'].value_counts().to_dict()

# artist별 sales_amount 합계 계산
df_sum = data.groupby(['artist']).agg({'sales_amount': 'sum'}).reset_index()

# artist별 앨범 개수 계산
df_count = data.groupby(['artist']).agg({'sales_amount': 'count'}).reset_index()
df_count = df_count.rename(columns={'sales_amount': 'album_count'})

# 합계와 개수를 병합하여 평균 계산
df = pd.merge(df_sum, df_count, on='artist')
df['average_sales_amount'] = (df['sales_amount'] / df['album_count']).round(0)

# 결과 출력
print(df[['artist', 'average_sales_amount']])

df.to_excel(r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\new.xlsx')

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the 'sales_amount' column
df['normalized_sales_amount'] = scaler.fit_transform(df[['average_sales_amount']])

# Assign 1 if normalized_sales_amount > 0.5, else 0
df['above_normalized_0.5'] = df['normalized_sales_amount'].apply(lambda x: 1 if x > 0.5 else 0)

# Assign 1 if normalized_sales_amount > 0.3, else 0
df['above_normalized_0.3'] = df['normalized_sales_amount'].apply(lambda x: 1 if x > 0.3 else 0)

# Assign 1 if normalized_sales_amount > 0.1, else 0
df['above_normalized_0.1'] = df['normalized_sales_amount'].apply(lambda x: 1 if x > 0.1 else 0)

# Calculate the median of 'sales_amount'
median_sales_amount = df['sales_amount'].median()

# Assign 1 if sales_amount > median, else 0
df['above_median'] = df['sales_amount'].apply(lambda x: 1 if x > median_sales_amount else 0)
# df = df.drop(columns=['title'])

# Save the updated dataframe to a new Excel file
output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Normalization_total_album_sum.xlsx'
df.to_excel(output_file_path)

print(f'Updated data with new columns saved to {output_file_path}')