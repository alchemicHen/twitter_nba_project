Repo for twitter sports data analysis comparing the accuracy of non-verified users to verified users in predicting NBA games.

Analysis notebooks: 
- [twitter_games_analysis](twitter_games_analysis.ipynb) contains the main analysis and visualizations for the project, including the sentiment differences between verified and non-verified users.
- [twitter_games_sentiment](twitter_games_sentiment.ipynb) contains additional cleaning and also performs sentiment analysis on the cleaned text of tweets.

Main datasets used:
- [mavs_games_tweets_merged](https://github.com/alchemicHen/twitter_nba_project/blob/main/Datasets/mavs_games_tweets_merged.csv): contains the joined and cleaned dataset to be used for analysis
- [tweets_games_final](https://github.com/alchemicHen/twitter_nba_project/blob/main/Datasets/tweets_games_final.csv): the final joined, cleaned, and processed dataset used in the `twitter_games_analysis` notebook and produced by the `twitter_games_sentiment` notebook.
