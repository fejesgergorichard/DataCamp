# The filter() method constructs an iterator from elements of an iterable for which a function returns true.
# Call: filter(function, iterable)
# Twitter dataframe is imported

# import pandas as pd
# tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda text: text[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)