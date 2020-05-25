# Section 4 - Identifying States
df_today = df[df['date'] == datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')]
topfivestates_rate = list(df_today.sort_values(by='rate', ascending=False).head()['state'])
topfivestates_rate.append('California')
topfivestates_rate.append('Washington')

# Section 5 - Filtering our Dataset
df = df[df['state'].isin(topfivestates_rate)]
df = df[df['date'] >= '2020-03-01']
df = df.pivot(index = 'date', columns = 'state', values = 'rate')

# Section 6 - Preparing out Dataset for Graphing
df = df.reset_index()
df = df.reset_index(drop=True)
df = df.drop(columns = 'date')