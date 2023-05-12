# %%
import pandas as pd
# %%

# create a dictionary of data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 32, 18, 47],
    'gender': ['F', 'M', 'M', 'M'],
    'country': ['USA', 'Canada', 'USA', 'UK'],
    'score': [87, 91, 62, 77]
}

# create a Pandas dataframe from the dictionary
df = pd.DataFrame(data)

# %%
df.name
df.score
# %%
df['name']
