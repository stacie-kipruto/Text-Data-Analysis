# TEXT DATA ANALYSIS
## Extracting the .ipynb:
- The notebook is rather large as it contains multiple sentiments on a youtube video.
- The only option would be to:
  1. Clone the repository onto your github desktop to view the notebook on your local machine.
  2. View and click the .html file as a raw file.
  3. Press ctrl+s to save it as .ipynb (You would have to manually type ".ipynb" after the file name to make it work as files from GitHub are saved as text files by default.
  4. Open Jupyter notebook.
  5. Go to the location where you saved your .ipynb file.
  6. open the file and see the code.

## Libraries used: 
  1. Numpy (numpy as np)
  2. Pandas (pandas as pd)
  3. Matplotlib (matplotlib.pyplot as pd)
  4. Seaborn (seaborn as sns)
  5. Textblob (from textblob import Textblob)
  6. Emoji (import emoji)
  7. RE (import re) _a ragular expression module for text data_

# Overview
- 1 billion hours of Youtube are watched per day. It is the 2nd most visited site in the world.
- YouTube attracts 44% of all internet users whereas 37% of all mobile internet traffic belongs to YouTube.

# Analysis Carried out
- Sentiment analysis:
    1. Negative comments ![Negative comments](https://user-images.githubusercontent.com/66944986/161414816-291f891f-17ba-49c0-8cc6-6149813daeee.png)

    2. Positive comments ![positive sentiments](https://user-images.githubusercontent.com/66944986/161414825-49f5938c-3fc3-4730-bf26-08ceef8b8751.png)


- Hashtag Analysis ![Hashtag Analysis](https://user-images.githubusercontent.com/66944986/161414760-6070be9f-eaab-4556-9057-eada1e67126c.png)

- Analysis on Likes, Views, Dislikes and How they corrrelate to each other (compared using regression plot and correlation matrix) ![image](https://user-images.githubusercontent.com/66944986/161414845-b1b6dd13-6352-4d0b-a727-26744f1c041c.png)

![image](https://user-images.githubusercontent.com/66944986/161414851-736ab07c-6491-4bd3-8e58-dec894c9c7bf.png)

- Emoji Analysis on comments and creating a dataframe with the corresponding number of various emojis. ![emojis](https://user-images.githubusercontent.com/66944986/161414900-818a65c2-f60d-49ca-a805-2810a713c3cc.PNG)

![compiled](https://user-images.githubusercontent.com/66944986/161414922-82dd7c78-a8dc-4fb7-bfa1-6d638bfee50c.PNG)

![keys](https://user-images.githubusercontent.com/66944986/161415003-06bb2934-9822-4d65-9c42-87df80b91a1c.PNG)

![corresponding values](https://user-images.githubusercontent.com/66944986/161415016-c9bfd5c6-0ea6-48db-b096-ba81eb6cbcc2.PNG)

![new dataframe](https://user-images.githubusercontent.com/66944986/161415023-6cf4e390-9511-4371-b898-8a388257ea74.PNG)
