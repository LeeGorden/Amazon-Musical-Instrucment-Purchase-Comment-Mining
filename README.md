<br>

## <div align="center">Amazon Musical Instrument Comment Analysis</div>

<details open>
<summary>Introduction</summary>

There are 10000+ comments on Amazon Musical Instrument selling website and corresponding score ranging from 1-5. The task is to apply topic modelling and train a model predicting score based on comment.

</details>

<details open>
<summary>Step</summary>
The whole project include the following steps

<details open>
<summary>Data Preprocess</summary>

- Data Preparation:

  Dealing with data imbalance. In this project, Up-Sampling and Down-Sampling is used to balance data with different score. More detailly, in Up-Sampling, Back Translation is applied via google API to generate comments under minority score.

</details>  

<details open>
<summary>Descriptive Analysis</summary>

- Comment Score Distribution:
  
  ![image](https://user-images.githubusercontent.com/72702872/168739738-1337975e-cb46-4ba1-b15e-a548988f57e3.png)

</details>   

<details open>
<summary>Model Training</summary>

- In topic modeling, bag-of-words vectorization is applied. The best topic number is defined based on Perplexity.
- In model predicting score, different tokenizing methods including Word Bag, TF-IDF + UniGram, TF-IDF + UniGram, TF-IDF + Uni&BiGram, TF-IDF BiGram.

</details>

<details open>
<summary>Result</summary>
  
<details open>
<summary>Data Balancing</summary>

- After applying Down-Sampling(random sampling) and Up-Sampling(Back Translation), score distribution is as follow:

  ![image](https://user-images.githubusercontent.com/72702872/168740529-9b2e9c94-c610-4ca3-bedf-70ea5e5ddca5.png)

</details>


<details open>
<summary>Model Performance</summary>

- Final topic modeling result:
  
  ![image](https://user-images.githubusercontent.com/72702872/168740661-a9303b69-f84d-45c6-bfbe-8efdd47993ae.png)

- Final prediction model result:
  
  ![image](https://user-images.githubusercontent.com/72702872/168740715-c47bb1c4-211d-47b2-bd7e-75dbbc6fc78b.png)

  ANN can do better on high dimension token Uni+Bi Gram TF-IDF , but will overfit on simple word bag or Uni Gram TF-IDF.

</details>

</details>

<details open>
<summary>Reference</summary>

[1] World Meteorological Organization (WMO). 2009. Weather and Climate Change 
Implications for Surface Transportation in the USA. Available at https://public.wmo.int/ 
as of 2009.

[2] United States Department of Transportation. 2020. Transportation Statistics Annual 
Report 2020 Available at https://fdd.bts.gov/freight-data-dictionary/ as of 2020

[3] U.S. Energy information Administration. 2020. Available at https://www.eia.gov/ as of 
2020

[4] Quora Answer Board. 2020 Available at https://www.quora.com/How-many-milescan-the-average-semi-truck-pull-a-full-load-without-refueling as of 201

</details>

</details>

## <div align="center">Contact</div>

email: likehao1006@gmail.com

LinkedIn: https://www.linkedin.com/in/kehao-li-06a9a2235/

ResearchGate: https://www.researchgate.net/profile/Gorden-Li

<br>

