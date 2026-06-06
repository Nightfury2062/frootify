import pandas as pd

df = pd.read_csv('Dataset.csv')


# # 1. Are there duplicate rows?

# if df.duplicated().any():
#     print("Duplicate rows exist")
# else:
#     print("No duplicate rows")S


# # 2. Number of duplicate rows
# print("\nDuplicate rows (excluding first occurrence):")
# print(df.duplicated().sum())


# # 3. Total rows involved in duplication
# print("\nTotal rows participating in duplicate groups:")
# print(df.duplicated(keep=False).sum())


# # 4. View duplicate rows
# duplicate_rows = df[df.duplicated(keep=False)]

# print("\nDuplicate rows preview:")
# print(duplicate_rows.head())


# # 5. Check which columns contribute to duplicates
# print("\nDuplicate count by individual column:")

# for col in df.columns:

#     duplicate_count = df[col].duplicated().sum()

#     print(f"{col}: {duplicate_count}")


# # 6. Decide whether action is required

# duplicate_percentage = (df.duplicated().sum()/len(df))*100

# print("\nDuplicate percentage:")
# print(round(duplicate_percentage,2),"%")

good_num = 0 
bad_num = 0
for i in df['Class']:
    if i == 'Good':
        good_num += 1
    else:
        bad_num += 1
print(good_num)
print(bad_num)