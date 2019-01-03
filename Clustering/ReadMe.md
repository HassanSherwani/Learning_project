#K-Means analysis

K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity. The results of the K-means clustering algorithm are:

The centroids of the K clusters, which can be used to label new data Labels for the training data (each data point is assigned to a single cluster) Rather than defining groups before looking at the data, clustering allows you to find and analyze the groups that have formed organically. The "Choosing K" section below describes how the number of groups can be determined.

Each centroid of a cluster is a collection of feature values which define the resulting groups. Examining the centroid feature weights can be used to qualitatively interpret what kind of group each cluster represents.

Dataset
Goal is that there is a big mall in a specific city that contains informations of its clients that subscribe to the membership card. When the clients subscribed to the card they provided their information like their gender, their age, and their annual income because they have this card they use it to buy all sorts of things in the mall. Therefore themall has to purchase history of each of its client member and that's how they obtained the last column which is a spending trend.

So as a reminder the spinning score is a score that the Mall computed for each of their client based on several criteria including their income, the number of times per week they show up in the mall, and the amount of dollars they spent in a year. 

Based on all this, they computed this metric that takes values between 1 and a 100 so that the closer the spinning score is to 1 ,the less decline spent and the closer the spinning scores to a hundred the more declines spent.

After collecting mall wishes to segment their clients into different groups based on these two metrics

the annual income and the spending score 

Since the Mall has no idea of what this client segments might be or even has no idea about how many segments that would be this is typically a clustering problem because we don't know the answers. So now let's start our mission and use the k-means algorithm to find out what those clusters of clients might be.
