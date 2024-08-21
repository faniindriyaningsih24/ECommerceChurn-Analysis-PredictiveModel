# E-Commerce Customer Churn Analysis and Classification Predictive Modeling Approach to Reduce Acquisition and Retention Costs

Presentation: [Link](https://www.canva.com/design/DAGL2FOtmnk/18WrhARHPHJXvJYo_M6yng/view?utm_content=DAGL2FOtmnk&utm_campaign=designshare&utm_medium=link&utm_source=editor)

Tableau: [Link](https://public.tableau.com/views/E-CommerceDashboardBetaGroup1/MainDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Created by our team:
### Alif Wahyu Syahnanda [Profile](https://www.linkedin.com/in/alifsyahnanda)
### Cyntia Angelica [Profile](https://www.linkedin.com/in/cyntia-angelica-6b5439217)
### Fani Indriyaningsih [Profile](https://www.linkedin.com/in/fani-indriyaningsih)

## **Background Context**
In a dynamic and competitive business world, the way companies operate and interact with the market is constantly changing. E-commerce is one clear example of this business evolution, opening up new opportunities for companies and individuals to buy and sell goods online. When the COVID-19 pandemic hit, global lockdowns fuelled a huge surge in e-commerce. In 2020, e-commerce sales penetration in the United States more than doubled to 35% from the previous year, which is equivalent to a decade of growth. Globally, nearly 20% of total sales in 2021 were made online, and it is expected to reach nearly a quarter of all global sales by 2025.([Mckinsey](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-e-commerce)).

The rise of online purchases makes customer focus even more important for e-commerce. According to McKinsey & Company([McKinsey & Company](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-three-building-blocks-of-successful-customer-experience-transformations)), improved customer experience can lower customer churn by almost 15%, as well as increase win ratio by almost 40%. Customer churn is a phenomenon where customers decide to stop buying or using products or services from a company. Understanding and improving customer experience is critical to maintaining their loyalty (retention) and reducing churn.

This customer experience is highly correlated with their behaviour towards e-commerce or a particular company. Providing satisfactory, responsive and personalised service is key to maintaining long-term relationships with customers. With the right strategy, companies can reduce churn, increase customer retention, and ultimately increase profitability. Research shows that satisfied and loyal customers tend to spend more and more frequently, making investment in customer experience an important strategic move for the long-term success of e-commerce companies.

Therefore, for e-commerce companies, it is important to understand and predict churn rates to identify at-risk customers and take proactive steps to retain them. With proper analysis, companies can design loyalty programmes, offer relevant incentives and improve overall service quality to minimise churn and maximise profits.

***What is Churn?***

Churn rate in *e-commerce* is the percentage of customers who stop making purchases or interacting with a company within a certain period of time. According to [shopify.com](https://www.shopify.com/blog/churn-rate-in-ecommerce), the churn rate is calculated in the following way:

(Number of customers at the beginning of the period - number of customers at the end of the period + number of new customers)/Number of customers at the beginning of the period

Determining whether a customer churns can be seen from the customer's historical purchase data to see the frequency of their purchases. If a customer usually buys every month but hasn't made a purchase for three months, this could be an indicator of churn.

## **Problem Statement**

According to [invespcro.com](https://www.invespcro.com/blog/customer-acquisition-retention/), 44% of companies focus more on customer acquisition than retention. This is despite the fact that the chances of selling goods to repeat customers (60%-70%) are greater than selling products to new customers (5%). In addition, 70% of companies agree that customer retention costs much less than new customer acquisition ($29/customer) ([semrush.com](https://www.semrush.com/blog/customer-retention-stats/) & [invespcro.com](https://www.invespcro.com/blog/customer-acquisition-retention/)). Even 44% of companies do not calculate their customer retention rate. This results in increased marketing costs and inefficient acquisition, while the profit potential of existing customers is not fully utilised.

Then, other findings reveal that existing customers tend to spend 67% more and more often than new customers ([semrush.com](https://www.semrush.com/blog/customer-retention-stats/)). This is supported by research conducted by [invespcro.com](https://www.invespcro.com/blog/customer-acquisition-retention/), which states that by increasing the retention rate by 5%, companies have the opportunity to increase their profitability by 25%-95%. However, many e-commerce platforms have not been able to provide an adequate experience to retain these customers. Dissatisfaction with the service, both in terms of product quality and delivery speed, is often the main reason why customers switch to other platforms (churn). Thus, improving customer experience is crucial to drive their loyalty.

A well-structured loyalty programme can be very effective in increasing customer retention and sales. Unfortunately, many e-commerce sites have not implemented loyalty programmes optimally. Existing programmes often do not provide attractive enough incentives for customers to remain loyal. Moreover, the variation in customer retention rates across different industries suggests that a one-size-fits-all approach is not effective.

To address these issues, it is important for e-commerce to predict churn rates to understand customer behaviour and the factors that influence it. With accurate predictions, companies can take proactive steps to improve customer experience and implement more effective retention strategies. Understanding shopping patterns and customer preferences can help in designing more attractive loyalty programmes. Thus, e-commerce can increase customer retention, reduce acquisition costs, and ultimately increase profitability.

## **Objective and Goals**

1. Identifying churn customers to know and understand what factors affect customers so that these customers churn.
2. Predict customers who have the potential to churn so that e-commerce/companies are proactive in retaining these customers with a model that produces the smallest possible loss and reduces the company's budget related to new customer acquisition.
3. Understanding the patterns and reasons behind churn that can help companies to improve certain aspects of the _user experience_.
4. Develop better retention strategies such as loyalty programmes, special discounts, and enhanced customer service to increase customer loyalty and reduce churn.

## **Analytics Approach**

* Based on the problem statement and goals, we will analyse data on customer churn by finding patterns or factors that affect customer churn.
* Next, build a classification model that is able to predict customers who churn or no churn.

## **Metrics Evaluation**

**Type 1 error** 	  : False Negative
<br>Consequence  : Since the predicted No Churn but Actual customers experience Churn, the company will lose the potential additional profit from customers who stop using or transacting in e-commerce. These customers are not targeted with retention efforts, leading to a higher likelihood of leaving our service (App), which directly impacts revenue. To acquire new customers, a fee is required which also incurs costs.

**Type 2 error** 	  : False Positive
<br>Consequence  : Due to predicted Churn but Actual customers experiencing No Churn the company will experience wasteful costs due to providing extra treatment (Churn treatment) to No Churn customers. The company may allocate retention resources (discounts, coupons) to these customers that are not actually needed. This may lead to increased costs without actual benefits.

Matriks Evaluasi Model: [Referensi](https://www.kdnuggets.com/2020/04/performance-evaluation-metrics-classification.html)
* Precision is a metric used to measure how many predictions of a class match reality. A very appropriate keyword to describe precision is exactness.
* Recall is a metrics in classification methods that states how much percentage of events in the positive class are successfully detected. The keyword that best describes recall is completeness.
* F1 score is the harmonic mean of precision and recall. When we use F1-score in machine learning model selection, F1-score can keep the selected model has balanced recall and precision values.
Accuracy is one of the commonly used evaluation metrics in machine learning to measure the extent to which a classification model is able to correctly predict the class or label of the test data. Simply put, accuracy measures the percentage of correct predictions out of the total number of predictions.

<br>Based on the confusion matrix above and looking at the consequences, the model built will focus on type error 1 (False Negative) or recall value. Because type error 1 (False Negative) will have a greater impact on company revenue than type error 2 (False Positive).

<br>Although the model built will focus on the recall value, but for the case of customer churn, the model will still pay attention to the precision value, because these 2 values have an impact on the company. So the model will be built with a balanced performance between false negatives (recall) and false positives (precision).

#### **Cost analysis of False Positive (FP) & False Negative (FN)**
Based on the selection of evaluation metrics that are the focus of ML development and the alignment of ML development with the problem and objectives to be achieved, the following is the calculation of the cost of loss based on False Positive (FP) and False Negative (FN) that will be evaluated. We need to determine the `Customer Spending per Month` (CSPM), `Customer Acquisition Cost` (CAC), and `Customer Retention Cost` (CRC).

- According to [yaguara.co](https://www.yaguara.co/online-shopping-statistics/), online shoppers in the United States spend an average of `$5381/year or `$448.4167/month' by 2023. This value will be the CSPM.
- According to [semrush.com](https://www.semrush.com/blog/customer-retention-stats/), to attract 1 new customer, a company needs to spend `$29/customer`. This value will act as `CAC`.
- Then, suppose we give a `5% discount` to customers who are predicted to churn. This means \$448,667*0.05 = `$22,433/customer`.

**Define Variables**
- CSPM = $448.4167

- CAC = $29 per Customer

- CRC = $22.433 per Customer

- FN = 10

- FP = 10

Loss Cost FN    = 10 * CSPM
                = 10 * $448.4167
                = $4.484.167
Direct revenue loss equivalent to CSPM
Loss Cost FP    = 10 * CRC
                = 10 * $22.433
                = $224.33
Just adding retention cost is much lower than loss cost FN

<br>The loss of False Negative (FN) is much greater than that of False Positive (FP). Therefore, prediction models that focus on minimising Type Error 1 (False Negative) or that have a high recall value are more beneficial to the company's revenue. This is because losing customers that can be avoided with retention incentives will have a significant impact on the company's revenue compared to providing unnecessary incentives.
