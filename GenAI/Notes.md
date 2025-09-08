# What is AI?

AI is an application that performs tasks without human intervention.  
**Example:** Playing Chess (Decision-making, pattern recognition, problem-solving process)

## Types of AI:

### Discriminative AI:
- **Focus:** Classifies and distinguishes data by learning the boundaries between different categories.
- **Example:** Image Classification, where the AI identifies and labels objects within an image (e.g., distinguishing between cats and dogs).

### Generative AI (GenAI):
- **Focus:** Learn how data is generated to create new content that mimics the original data.
- **Examples:**
  - Image Generation: Creating new images based on learned patterns from existing images.
  - Text Generation: Producing coherent and contextually relevant text, such as writing articles or generating dialogue.

### Modern AI:
- **Focus:** Utilizes Deep Learning techniques, which involve neural networks with many layers (deep neural networks) to model complex patterns in large datasets.
- **Applications:** Includes advanced tasks like natural language processing, speech recognition, and autonomous driving.

## Generative AI (GenAI) Overview

Generative AI (GenAI) is an advanced application that combines Natural Language Processing (NLP) and Vision Computing to create versatile AI solutions. It uses generative models to produce new content, such as text, images, and videos, by learning patterns from existing data.

**Examples:**
- ChatGPT: Handles text-based tasks, enabling natural and engaging conversations.
- DALL-E: Generates images from textual descriptions, showcasing AI's visual creativity.

Applications of GenAI span various industries, including software development, healthcare, finance, and entertainment.

## System Requirements:
- Processor: i7 - i9  
- RAM: 16 - 32 GB  
- GPU: 4060  
- Editor Needed: Google Colab  
- Scripting Languages Required:
  - Python
  - C
  - C++

## 4 Ways to Utilize GenAI:
1. Through Tools: Leverage various AI tools designed for specific tasks.
2. AI ChatBot: Implement AI chatbots for customer service, support, and engagement.
3. LLM Framework API: Use Large Language Model (LLM) framework APIs to execute prompts and generate content.
4. Cloud Services: Utilize cloud services like Amazon Bedrock and Google Cloudrock for scalable AI solutions.

---

# Machine Learning

## Topics Covered:
- Foundations of ML
- Data preparation and processing
- Types of Algorithms
- Deep Learning
- Model Evaluation and Tuning

## What is ML?

ML is a subset of AI. Here we are going to analyze the given data, visualize and do some prediction/forecast, and involve algorithms.  
**Example:** Netflix Recommendation (Based on your past data, the system recommends content based on its learning from your past data)

## Workflow of a Normal ML Model:
**Input → ML System → Output**  
The output can be a number, class, or probability.

ML works with the function:  
**y = f(x)**  
- Y: Model output  
- F: Model  
- X: Input

## Machine Learning Life Cycle:

### Planning:
- Define the business problem and objectives.
- Assess feasibility and success metrics.

### Data Preparation:
- Collect and preprocess data (cleaning, transforming).

### Model Engineering:
- Select and train the appropriate model.
- Fine-tune model parameters.

### Model Evaluation:
- Assess model performance using evaluation metrics (accuracy, precision, etc.).

### Model Deployment:
- Implement the model in a production environment.
- Integrate with existing systems.

### Monitoring and Maintenance:
- Continuously monitor performance.
- Update and retrain the model as needed.

## Types of ML Techniques:

### Supervised Learning:
- Learn from labelled data
- When we have a dependent feature we call it supervised learning.

#### Types of Problem Statements:

**Regression**  
- Focus: Predicts output, mostly working with continuous data.  
- Example: Predicting house prices based on features like size, location, and number of bedrooms.  

**Regression Algorithms:**
- Simple Linear Regression
- Multi Linear Regression
- Polynomial Regression
- Support Vector Regression
- Ridge & Lasso Regression
- Elastic Net

**Classification**  
- Focus: Classifies or categorizes the data into distinct classes.  
- Example: Classifying emails as spam or not spam based on their content.  

**Types of Classification:**
- Binary Classification (When we have only two categories, o/p Pass OR Fail)
- Multi-Class Classification (When we have more than two categories, o/p Pass OR Fail OR Maybe)

**Classification Algorithms:**
- Logistic Regression
- K - Nearest Neighbours (KNN)
- Support Vector Machine (SVM)
- Kernal SVM
- Naive Bayes

### Unsupervised Learning:
- Algorithm without label
- Find the hidden pattern
- We don’t have dependent feature
- Group the data  
**Example:** Customer Segmentation

### Reinforcement Learning:
- Application will learn from things by itself by getting some rewards and feedback

## Different Types of Learning Models:

### Instance Based Learning:
- Model is completely dependent on data
- Trained based on data what we give
- Output is based on data used  
**Example:** Pass/Fail, Features: No of study hours, No of play hours

### Model Based Learning:
- Understand the pattern
- Creates a generalization method
- Curve called “Decision Bounding”

## Steps to Build an ML Model:

1. Problem Definition: Clearly define the problem you want to solve and the objectives.
2. Data Collection: Gather relevant data from various sources.
3. Data Preprocessing: Clean the data (handle missing values, remove duplicates). Transform the data (normalize, scale).
4. Model Selection: Choose the appropriate algorithm based on the problem and data.
5. Model Training: Train the model using the training dataset.
6. Model Evaluation: Assess the model's performance using evaluation metrics (accuracy, precision, recall, etc.).
7. Model Tuning: Fine-tune the model parameters to improve performance.
8. Model Development & Deployment: Implement the model in a production environment. Integrate with existing systems.
9. Model Monitoring: Continuously monitor the model's performance.
10. Model Improvement: Update and retrain the model as needed based on new data and feedback.

## Algorithms:

### Algorithms in Supervised Learnings

**Regression Algorithms:**
- Simple Linear Regression
- Multi Linear Regression
- Polynomial Regression
- Support Vector Regression
- Ridge & Lasso Regression
- Elastic Net

**Classification Algorithms:**
- Logistic Regression
- K - Nearest Neighbours (KNN)
- Support Vector Machine (SVM)
- Kernal SVM
- Naive Bayes

**Both Classification & Regression Algorithms:**
- Decision Tree
- Random Forest
- AdaBoost
- XGBoost

### Algorithms in Unsupervised Learnings:
- K-Means
- Hierarchical Means
- DBScan Clustering

## How to Choose Algorithm:

Choosing the right algorithm for your machine learning task involves several considerations:

1. **Type of Problem:**
   - Supervised Learning: Classification or Regression
   - Unsupervised Learning: Clustering or Dimensionality Reduction
   - Reinforcement Learning: Learning from environment feedback

2. **Data Size and Structure:**
   - Small Datasets: Simpler algorithms
   - Large Datasets: Complex algorithms

3. **Accuracy vs Resources:**
   - High accuracy may require more computational resources

4. **Interpretability:**
   - High: Decision Trees, Linear Regression
   - Low: Neural Networks, Ensemble Methods

5. **Type of Features:**
   - Numerical: Linear Regression, SVM
   - Categorical: Decision Trees, Naive Bayes

6. **Computational Resources:**
   - Simpler algorithms for limited resources
   - Deep Learning for powerful hardware

7. **Specific Use Case:**
   - CNN for image recognition
   - RNN for time series data

## What is Deep Learning?

Deep Learning is a subset of ML. It mimics the human brain using multi-layer neural networks.  
**Example:** Self-driving cars

## Few Mathematical Equations:

- **Equation of Line**
- **3D and Hyperplane**

**Cost Function:** To reduce error i.e. y - y^ (predicted value - actual value)  
**Global Minima**  
**Gradient Descent**  
**Convergence Algorithm:** Optimize the change of theta 1 value  
- Low Bias & High Variance [Overfitting]  
- Low Bias & Low Variance [Underfitting]

## Topics Covered:
- Simple Linear Regression
- Multi Linear Regression [Economic Index example]
- Simple Polynomial Regression

## Euclidean Formula:

The Euclidean formula is used to calculate the distance between two points in a plane.  
Formula:  
`d = sqrt((x2 - x1)^2 + (y2 - y1)^2)`

**Example:**  
Points A(1, 2) and B(4, 6)  
`d = sqrt((4 - 1)^2 + (6 - 2)^2) = sqrt(9 + 16) = sqrt(25) = 5`

## Manhattan Formula:

Measures distance by moving along grid lines (horizontal and vertical).  
Formula:  
`d = |x2 - x1| + |y2 - y1|`

**Example:**  
Points A(1, 2) and B(4, 6)  
`d = |4 - 1| + |6 - 2| = 3 + 4 = 7`

**Applications:**
- Urban Planning
- Machine Learning (KNN)
- Robotics

## Other Concepts:
- K-D Tree
- Ball Tree
- KNN
- Naive Bayes Algorithm requires understanding of probability & Bayes theorem
