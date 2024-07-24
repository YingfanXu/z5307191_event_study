import pandas as pd

# 
data = {
    'Company': ['Google', 'Google', 'Facebook', 'Facebook', 'Amazon', 'Amazon'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}
df = pd.DataFrame(data)

# Group by company and calculate the sum and average of sales
grouped = df.groupby('Company')
agg_df = grouped.agg({
    'Sales': ['sum', 'mean']
})

print(agg_df)
