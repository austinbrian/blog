---
layout: page
title: "What's the Problem?"
subtitle: "Topic modeling consumer complaints to the CFPB"

---
*Find the full code and data for this project at [GitHub here](https://github.com/austinbrian/portfolio/).*

## Overview
- This project examines the text of complaints to the Consumer Financial Protection Bureau.
- Topics are generated using Latent Dirichlet Allocation, an unsupervised clustering algorithm that groups words commonly used in the same context.
- Topics are used to predict which financial product a consumer is referring to, given a set of unstructured text. A support vector machine classifier determined which product a given complaint referred to with 77% accuracy.
- This model could be useful to a company that used a customer service chatbot to efficiently direct consumers to on-site resources.


## Introduction   
The [Consumer Financial Protection Bureau](https://www.consumerfinance.gov/) (CFPB) has been around since 2011. The organization is charged with policing financial services companies to ensure that they are fairly treating consumers. One of the ways they gather information on consumers' experiences is by tallying complaints of wrongdoing against companies.

This graph shows the number of complaints for every day since the organization began keeping track. Complaints have been increasing over its four-year history, and for reasons that escape me, Wednesdays and Thursdays are consistently less frequent days for complaints to be made than the rest of the week.

![](/images/cfpb/all_complaints_scatter.png "That highest orange point is Donald Trump's Inauguration")

Complaints include information regarding the company, the product, sub-products, as well as information on whether or not the company in question responded to the consumer.
