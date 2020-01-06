# Mexican Peso Performance in the Last 10 Years

In Mexico it is often a topic of discussion whether the Mexican Peso is devaluating or depreciating. The exchange rate is often used to determine how well is doing the Mexican econonmy.

I took the task on reviewing 10 popular currencies against the Mexican Peso. The objective is to observe how the value of the Mexican Peso has changed in the last 10 years.

To accomplish this I gathered historical data from the last 120 months. Each month was resampled into a single value representing its mean.

The following charts and insights are presented from the Mexican Peso perspective, positive percentage values mean that the Mexican Peso got stronger and negative percent values mean that it got weaker.

The higher the number is on the Initial Value, Latest Value, Min, Max and Mean, means the more Mexican Pesos are needed to buy other currencies.

The data covers all exchange rates between January 2010 to January 2020.

The insights and charts from this document were generated using the `pandas` and `matplotllb` libraries from the `Python` programming language.

It is important to note that the exchange rate doesn't absolutely represent how a country's economy is performing.

## The Top 5

In the following figure we will observe how the Mexican Peso has performed against the top 5 currencies.

![Top 5](./figs/top5.png)

| Code | Name | Initial Value | Latest Value | Percentage Change | Min | Max | Mean |
| ---- |:---------------------|------:|------:|---------:|------:|------:|------:|
| CHF | Swiss Franc | 12.38 | 19.44 | -57.08% | 11.28 | 21.19 | 16.24 |
| EUR | Euro | 18.25 | 21.10 | -15.63% | 15.35 | 23.67 | 18.95 |
| GBP | Great Britain Pound | 20.70 | 24.75 | -19.59% | 18.68 | 26.94 | 22.63 |
| JPY | Japanese Yen | 0.14 | 0.17 | -23.99% | 0.12 | 0.19 | 0.15 |
| USD | United States Dollar | 12.82 | 18.90 | -47.42% | 11.65 | 21.35 | 15.64 |


The Mexican Peso lost against all the top 5 currencies. It lost the most against the Swiss Franc.

## Popular Currencies

In the next figure we can observe how the Mexican Peso performed against other 5 currencies that are popular.

![Top 5](./figs/popular.png)

| Code | Name | Initial Value | Latest Value | Percentage Change | Min | Max | Mean |
| ---- |:---------------------|------:|------:|--------:|-----:|------:|------:|
| ARS | Argentine Peso | 3.37 | 0.32 | 90.62% | 0.32 | 3.37 | 1.83 |
| AUD | Australian Dollar | 11.69 | 13.15 | -12.56% | 10.86 | 15.94 | 13.04 |
| BRL | Brazilian Real | 7.16 | 4.66 | 34.91% | 4.28 | 7.67 | 5.91 |
| CAD | Canadian Dollar | 12.27 | 14.54 | -18.53% | 11.49 | 16.17 | 13.29 |
| CNY | Chinese Yuan | 1.88 | 2.71 | -44.50% | 1.79 | 3.13 | 2.40 |

The Mexican Peso got stronger against the Argentine Peso, it almost doubled in value.

Similarly, the Brazilian Real lost one third of its value against the Mexican Peso.

There is something in common in both charts, at the beginning of 2017 the Mexican Peso got significanly weaker against most other currencies.

The following headlines summarize the events of January 2017 that could have affected the value perceived of Mexico.

* Ford announces that it has cancelled plans to build a $1.6 billion plant in Mexico, long criticized by U.S. President-elect Donald Trump, and will invest $700 million in its Michigan plant in Flat Rock, potentially creating 700 new jobs from the investment and expansion of the plant.

* Following a start-of-year hike to the price of gas, widespread riots and looting mostly targeting gas stations, supermarkets and department stores take place in several cities in Mexico. Over 250 people are said to have been arrested so far while blockades to PEMEX installations potentially lead to critical situations in some states. 

* U.S. President Donald Trump issues executive orders to withdraw the United States from the Trans-Pacific Partnership, and reinstates the Mexico City Policy, a policy banning U.S. aid to foreign organizations that use funds from other sources to perform or discuss abortions, which Barack Obama scrapped in 2009.

* Mexican President Enrique Peña Nieto rejects the idea, announced by U.S. President Donald Trump, that Mexico would pay for any border wall between the United States and his country.

* Mexican senior officials say President Peña Nieto may cancel his plans to visit the White House next Tuesday, January 31, because of President Trump's actions.

[Source](https://en.wikipedia.org/wiki/Portal:Current_events/January_2017)

## Conclusion

The Mexican Peso has depreciated significantly in the last 10 years but it is also important to note that it has gotten stronger against other currencies which means it only depreciated against the top currencies belonging to countries that are perceived as safer to invest in.

[![Become a Patron!](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/bePatron?u=20521425)