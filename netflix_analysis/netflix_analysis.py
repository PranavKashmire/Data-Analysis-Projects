import pandas as pd

# Load the Excel file
file_path = '/home/ubuntu/upload/_IN__Data_Support_Specialist_NFLX_Exercise_Data_File(1).xlsx'
xls = pd.ExcelFile(file_path)

# Load the 'NFLX Top 10' sheet
df_top10 = pd.read_excel(xls, sheet_name='NFLX Top 10')

# Filter for 'Films (Non-English)' category
non_english_films = df_top10[df_top10['category'] == 'Films (Non-English)']

# Find the film with the most weeks in the top 10
# We should look at the maximum 'cumulative_weeks_in_top_10' for each film
top_film = non_english_films.groupby('show_title')['cumulative_weeks_in_top_10'].max().sort_values(ascending=False).head(1)

print("Top Film in 'Films (Non-English)' by weeks in Top 10:")
print(top_film)

# Get details for this top film to help with estimation assumptions
top_film_name = top_film.index[0]
top_film_data = non_english_films[non_english_films['show_title'] == top_film_name]
print(f"\nDetails for {top_film_name}:")
print(top_film_data[['week', 'weekly_hours_viewed', 'cumulative_weeks_in_top_10']])

# Check the data for the week of May 22nd
print("\nData for the week of 2022-05-22:")
may_22_data = df_top10[df_top10['week'] == '2022-05-22']
print(may_22_data.head(20))

# Check if there are any 0 or missing values in weekly_hours_viewed for that week
print("\nSummary of weekly_hours_viewed for week 2022-05-22:")
print(may_22_data['weekly_hours_viewed'].describe())
print(f"Number of zeros: {(may_22_data['weekly_hours_viewed'] == 0).sum()}")

# Load Runtime sheet to help with user estimation
df_runtime = pd.read_excel(xls, sheet_name='Runtime')
film_runtime = df_runtime[df_runtime['title'] == top_film_name]
print(f"\nRuntime for {top_film_name}:")
print(film_runtime)
