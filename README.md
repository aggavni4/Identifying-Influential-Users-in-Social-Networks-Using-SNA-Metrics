# Identifying-Influential-Users-in-Social-Networks-Using-SNA-Metrics
## Summary
This project explores the structural properties of social networks using data from the Facebook network. The primary goal is to detect influential users by analyzing the network’s topology through centrality measures. While existing metrics such as degree, betweenness, closeness, and eigenvector centrality provide useful insights, they often fall short in capturing influence in complex community-based networks. To address this gap, we propose a novel centrality measure that accounts for both a node’s connectivity and its position within community structures identified using the Louvain algorithm. The new metric emphasizes not just how connected a user is, but how strategically placed they are within or across communities, making it a better indicator of influence in real-world networks. Using NetworkX, we perform community detection, compute various centrality metrics, and visualize the network to compare results. Our findings show that the proposed measure successfully highlights users who may be overlooked by traditional metrics, offering a more nuanced understanding of influence within social graphs.
## Empirical Study
The empirical foundation of this project lies in the detailed examination of a publicly available Facebook social network dataset (https://snap.stanford.edu/data/egonets-Facebook.html), which contains anonymized data reflecting friendships among users. This dataset is structured as an undirected, unweighted graph where each node represents a user, and each edge denotes a mutual friendship.
Firstly, the **Louvain algorithm** is applied for community detection.  Louvain algorithm is one of the most prominent modularity-based approaches, efficiently partitioning networks into communities while optimizing modularity scores. It is a heuristic method based on modularity optimization.The algorithm works in 2 steps. On the first step it assigns every node to be in its own community and then for each node it tries to find the maximum positive modularity gain by moving each node to all of its neighbor communities. If no positive gain is achieved the node remains in its original community.The modularity gain obtained by moving an isolated node i into a community C can easily be calculated by the following formula:<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/ba06d387-aae5-47fb-8507-e7988cd678f9" > <br>
</div>
where m  is the size of the graph, k<sub>i,in</sub> is the sum of the weights of the links from i to nodes in C, k<sub>i</sub> is the sum of the weights of the links incident to node i, ∑tot is the sum of the weights of the links incient to nodes in C and γ is the resolution parameter.

This algorithm is selected due to its exceptional scalability, high computational efficiency, and proven ability to optimize modularity—a crucial measure of the quality of community structures. The modular organization of the Facebook graph is uncovered, revealing the natural clusters within the social fabric of the network.<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/16f76182-b0ef-4358-b151-02cd89ab9d46" width="550"> <br>
</div>
Once community structures are identified, a suite of classical centrality measures—namely, degree, closeness, betweenness, and eigenvector centrality—is computed using the NetworkX library in Python. The results are thoroughly analyzed to discern patterns in node centrality and to highlight the limitations of these traditional approaches in fully capturing the spectrum of influential nodes. These insights directly motivate the creation of a new, more nuanced centrality measure.
This table is sorted by the values of PageRank centrality, in ascending order:
<div align="center">
<img src="https://github.com/user-attachments/assets/46d95a9f-fc82-4be8-b874-75f1055e7cc5" width="400">
</div>
New centrality measure is then defined, instantiated, and systematically applied to the same network. Its performance is evaluated based on comparative analysis with traditional measures, emphasizing its ability to single out key influencers within individual communities as well as across community borders.

The below **heatmap** shows the correlation between different centralities, which in turn represents the similarity or overlaps among them. It also shows how some of these centralities are quite different from each other and hence, there is a need of a new centrality measure that is more comprehensive in determining the influential users in a community structure.
<div align="center">
<img src="https://github.com/user-attachments/assets/8d8ebd0a-b4e5-45ed-bf18-9832a86042f1" width="400">
</div> 

## Brief Description of Solution Approach
The solution approach adopted in this project is systematic and multi-aspect, considering the inherent complexity of large social networks with embedded community structures. The approach begins with thorough preprocessing and visualization of the data to clean, structure, and understand the data structure of the Facebook social network data. This ensures that the subsequent analyses are grounded on good and understandable data.
Next, the Louvain algorithm is applied for community detection. The algorithm is chosen because it is efficient and effective in identifying densely connected subgroups by optimizing modularity. Detection of these communities provides valuable information on the meso-level structure of the network—an aspect typically overlooked by traditional node-level centrality measures.
After community structures are discovered, the project explores some of the most traditional centrality measures degree, closeness, betweenness, and eigenvector centrality and how influential each node is by definition. But with a glance and a statistical comparison, these measures prove to have shortcomings, especially in their ability to find influence that transcends communities or occurs within tighter but more cohesive clusters.
With the endeavor of enhancing these flaws, this project introduces a novel measure of centrality that integrates intra-community standing and inter-community bridging. The underlying philosophy in introducing this new measure is that influence in social networks is not just about being highly connected but where your connections are structurally located.<br>
The proposed centrality measure incorporates:
- Local degree centrality to account for immediate influence within a community
- Modularity-based participation score to capture a node’s embeddedness in well-formed communities
- Inter-community edge analysis to assess how effectively a node connects different communities<br>

This measure is implemented using Python's NetworkX and community libraries and evaluated through a comparative framework against traditional centrality measures. The comparative analysis includes graphical visualizations, rank correlations, and statistical summaries. This holistic approach ensures a robust understanding of influence dynamics and highlights the added value of the newly developed centrality metric.

## Comparison of the existing approaches to the problem framed
Existing approaches to identifying influential nodes in networks primarily rely on well-established centrality measures:
* **Degree Centrality:** ranks nodes based on the number of direct connections. While easy to compute and interpret, it overlooks the broader role a node plays in the network. It is defined as follows:
<div align="center">
<img src="https://github.com/user-attachments/assets/baa7a8fb-f585-41a9-b4a4-2d4ea5418a63">
</div>
where a<sub>ij</sub> is obtained from A<sup>1</sup>, 1-step neighborhood (p=l).

* **Closeness Centrality:** measures how close a node is to all others in terms of path length. It assumes a globally connected network and may not reflect true influence in disconnected or modular structures. It is defined as follows:
<div align="center">
<image src="https://github.com/user-attachments/assets/98d6eba6-a0f5-403c-b45d-57ca21afc918">
</div>
where d(i, j) is the shortest-path distance between node i and j.

* **Betweenness Centrality:** evaluates how often a node appears on the shortest paths between other nodes. Although it highlights nodes acting as bridges, it is computationally expensive and sensitive to network topology changes. It is defined as follows:
<div align="center">
<image src="https://github.com/user-attachments/assets/737568c1-3c33-40f2-ab86-cb032bc54f4b">
</div>
where 𝜎(s, t) is the number of shortest paths between nodes s and t and  𝜎<sub>i</sub>(s, t) is the number of shortest paths between nodes s and t that pass through node i.

* **Eigenvector Centrality:** considers both the number and quality of connections, favoring nodes connected to other well-connected nodes. However, it may disproportionately emphasize nodes in large, dense communities. It is defined as follows:
<div align="center">
<image src="https://github.com/user-attachments/assets/be4cc205-e2c9-44b0-9fae-36fb3a46b154">
</div>
where x<sub>i</sub> is the eigenvector centrality of a node i is and λ ≠ 0 is a constant.

* **PageRank Centrality:** builds upon the idea of eigenvector centrality by considering the probability distribution of a random walk across the network. However, PageRank may still underperform in modular networks if a node’s community interactions are not adequately represented in the global structure. It is defined as follows:
<div align="center">
<image src="https://github.com/user-attachments/assets/6620dd79-fbaa-443a-8e99-8973d2377c3f">
</div>
where α<sub>p</sub>(i) and α<sub>p</sub>(j) are the PageRank centralities of node i and node j, respectively, N<sub>1</sub>(i) is the set of direct neighbors of node i, k<sub>j</sub> is the number of links from node j to node i, and d is the damping parameter where d ∈ [0,1], set to 0.85 in the experiments.  

<br/>
These techniques, although strong, all have one thing in common: they generally fail to consider structures of communities, which are widespread in social networks. Intra-community bonding and inter-community contacts are frequently crucial to understanding the influence process.
The proposed centrality measure overcomes these limitations by explicitly including community-aware features, providing a more comprehensive perspective on node influence. It recognizes that influence in the real world is not entirely a function of the ties between nodes but also of purposeful positionning within and across densely connected subgroups.

## Overall Description of the Project
This project is rooted in the more general realm of Social Network Analysis (SNA) and its identification of key individuals within a large-scale, community-scaled social network. The project draws upon the shortfalls in classical centrality measures in portraying influence in such modular networks and suggests a new solution- a sophisticated, community-informed centrality measure that more accurately captures both the local and global aspects of influence.
Fundamentally, the project is based on the analysis of a Facebook ego-network dataset. Every node in the network is a Facebook user, and every edge is a mutual friendship. In contrast to the conventional graph analysis where attention is given only to direct connections or shortest paths, this project takes a more layered approach that focuses on the detection of communities using the Louvain algorithm and then a thorough centrality evaluation within and between those communities.
This research is not only analytical but also developmental and comparative. It ends with proposing and applying a new centrality measure that integrates community engagement, local node connectiveness, and inter-community bridging. The aim is to surpass the restrictive scope of previous measures and to offer a more realistic, functional, and interpretable model to identify key influencers.
The project proceeds in three major phases:
1. **Data Acquisition and Preprocessing** – Downloading, cleaning, and visualizing the Facebook network dataset to ensure consistency and reliability for analysis.
2. **Community Detection and Classical Centrality Analysis** – Applying the Louvain algorithm and computing standard centrality metrics such as degree, closeness, betweenness, eigenvector, and PageRank.
3. **Design, Development, and Evaluation of a Novel Centrality Measure** – Formulating a new metric that integrates intra-community importance with inter-community influence, followed by a comparative evaluation using quantitative and visual techniques.
The scope of the project ranges over data handling, algorithmic code, metric development, and explanation by empirical evidence, all predicated on graph theory and network science theoretical frameworks. The end objective is to not only come up with a theoretically robust measure of centrality but also substantiate its utility and applicability through experimental tests.

## Design Diagram
Activity Diagram
<div align="center">
<image src="https://github.com/user-attachments/assets/dbb9b14c-60bf-4235-9c3a-db2af556c9fb">
</div>

## Implementation Details
The project is implemented in Python, utilizing the NetworkX library for graph construction and analysis due to its strength. Matplotlib is used to process and visualize the Facebook dataset, and community detection is done using the community library that supports the Louvain method.
Implementation starts with converting the raw data set to an undirected graph. The traditional centrality measures are then calculated with default functions provided in NetworkX. For the suggested centrality score, user-defined functions are defined to obtain intra-community influence and inter-community connectivity. The individual components are combined linearly or through an adaptive function that is tunable. The ultimate influence score is calculated for every node.
To improve the interpretability of the detected communities and network structure, a web-based frontend using Dash and Plotly was implemented. The frontend enables users to visualize the entire Facebook graph and filter and examine individual community subgraphs. The nodes are color-coded according to community membership, and a node's details, including node ID and community label, are displayed when a node is hovered over. A dropdown menu supports dynamic filtering of communities, which makes the exploration very intuitive and visually informative. Layout is computed based on the spring layout algorithm, while interactivity is obtained from responsive callbacks. This frontend not only facilitates further analysis but also enhances the usability of the proposed system by providing direct, visual comprehension of community structures.

**Frontend:**

Communities using Louvain Algorithm:
<div align="center">
<image src="https://github.com/user-attachments/assets/05fdef26-05fc-4112-a45b-b4a3d135387c">
</div>
 Separate graph of Community-2:
<div align="center">
<image src="https://github.com/user-attachments/assets/7e52cc7d-999c-416c-83e8-ab9230eb52cd">
</div>
Separate graph of Community-13:
<div align="center">
<image src="https://github.com/user-attachments/assets/3bf5e1a6-4cdf-4f07-a938-b37aee466a97">
</div>

## Test Environment
Software Items:  
* Python 3.10 <br>
* Jupyter Notebook / VS Code
* NetworkX, Matplotlib, Seaborn, Pandas
* Operating System: Windows 11 / Ubuntu 22.04
* No automated test tools used, tests written manually

Hardware Items:  
* CPU: Intel i5 or Ryzen 5 or better
* RAM: 8GB or more
* No dedicated GPU used

## Findings and Conclusion
In order to compare the performance of the suggested centrality measure, Influential_Score, we calculated and compared it to other centralities with respect to top nodes in the Facebook network dataset. This table displays a sample of nodes and their respective values for each centrality measure, which is an indication of the contribution of the new metric toward the identification of influential nodes.

<div align="center">
<image src="https://github.com/user-attachments/assets/48ae68cd-484f-4bd6-9f92-d5e9f489290b" width="500">
</div>
<div align="center">
Table containing traditional centrality measures and with PCA1, PCA2, Influential_Score of all nodes
</div>
  
To explore the connection between the novel Influential_Score and historical centrality indices, a heatmap of correlations was generated. The following heatmap display shows the degree to which the new measure complies with or contradicts the past measures when it comes to expressing node relevance.
<div align="center">
<image src="https://github.com/user-attachments/assets/9163fb60-7b85-443f-bff4-c17f13369e5e" width="400">
</div>
<div align="center">
Heatmap containing Influential_Score with Traditional Centrality measures
</div>

**Key Observations:**

<ins>Strong Correlations Among Centrality Measures</ins>:
Degree, Betweenness, and PageRank are strongly correlated (0.78–0.85), which implies highly connected nodes are also likely to have high betweenness and PageRank scores.
Eigenvector centrality is positively correlated with Degree (0.78) and PageRank (0.70), which means highly connected nodes (Degree) and high-quality connected nodes (Eigenvector) concur but are not one and the same.
Closeness has weaker correlations (0.44–0.67), suggesting it measures different facets of network position (e.g., average distance to all nodes).

<ins>Weak/Negligible Correlation with Influential Score</ins>:
Every measure of centrality demonstrates close-to-zero correlation (−0.09 to 0.06) with the Influential Score.
This indicates the established "Influential Score" possibly measures something orthogonal to conventional centrality (e.g., external factors such as user activity, content quality, or influence in a specific domain).

<ins>Potential Outliers</ins>:
The slight negative correlation between Eigenvector centrality and Influential Score (−0.09) hints that nodes with high Eigenvector scores (influential neighbors) might not align with the external influence metric.

<ins>Interpretation & Recommendations</ins>:<br>
Centrality Measures:
Degree, Betweenness, and PageRank are likely interchangeable for identifying structurally central nodes in this network. Closeness and Eigenvector add complementary insights.<br>
Influential Score:
Since it’s uncorrelated with centrality, investigate its definition:
Is it based on non-topological factors (e.g., semantic content, user engagement)
If prediction of influence is the goal, one could consider hybridizing centrality with outside characteristics (e.g., regression modeling).

To further investigate pairwise correlations between various centrality metrics, including the introduced Influential_Score, the following scatter plots were created. The following scatter plots illustrate pairwise comparisons between traditional centrality metrics and the introduced Influential_Score, providing information about their linearity, clustering, and distribution patterns.

Here are Scatter plots of Eigenvector, PageRank and influential_score with all Traditional Centralities and Influential_Score:
<br>
<div align="center">
<image src="https://github.com/user-attachments/assets/e9f6da33-4688-41df-bc44-1ad6ae8671b0">
</div>
<br>
Here are the insights of all Centrality Measures: 


<div align="center">
  
| Centrality Measure | Captures...                               | Correlates Well With                      | Distinct From |
|--------------------|-------------------------------------------|-------------------------------------------|---------------|
| **Degree**         | Local connectedness                      | Closeness, Eigenvector, PageRank          | Betweenness   |
| **Betweenness**    | Bridge roles (shortest paths)             | None strongly                             | Most others   |
| **Closeness**      | Distance efficiency in network           | Degree, Eigenvector, PageRank             | Betweenness   |
| **Eigenvector**    | Connection to influential nodes          | PageRank, Closeness, Degree               | Betweenness   |
| **PageRank**       | Probabilistic importance (global)         | Eigenvector, Degree, Closeness            | Betweenness   |
| **Influential_Score** | Likely a weighted combo of multiple scores | All except Betweenness                  | Betweenness   |
</div>

## Conclusion
This project delved into the field of social network analysis (SNA) and examined identifying influential users within online communities. Through examining the Facebook network dataset, the project applied different traditional centrality metrics—Degree, Closeness, Betweenness, Eigenvector, and PageRank—and assessed their capability in pinpointing pivotal nodes in the network. The fundamental contribution of the project was the creation and implementation of a new centrality measure that both considered intra-community and inter-community interactions based on the modular community structure determined using the Louvain algorithm. This suggested measure sought to fill the gap left by conventional measures that, in many cases, were not able to account for influence diffusion across community borders. So we defined the Influential Score, a new centrality-based indicator created to highlight the most central nodes in discovered communities by leveraging the best qualities of several popular centrality metrics. By intense empirical testing across Louvain-algorithm detected communities, we established that not a single classic metric—e.g., Eigenvector, PageRank, or Closeness—captures node influence exclusively by itself because all of these accentuate diverse characteristics of connection and positional prominence. Yet, looking at these measures in combination, distinct patterns were clear: groups like 5, 7, and 13 uniformly contained high-ranking nodes in all three measures, affirming their structural centrality and power within the network. The Influential Score, as proposed, was successful at integrating these dimensions, providing a rigorous, multi-dimensional perspective on node significance superior to individual measures. This integrated score not only pinpointed the most influential communities but also offered a scalable and context-sensitive method for influence detection in massive networks. Finally, this measure provides a sound foundation for downstream applications for social influence modeling, epidemic control, and targeted intervention across complex networks.
