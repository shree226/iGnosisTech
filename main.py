import pandas as pd
import matplotlib.pyplot as plt

purchase_behaviour = pd.read_csv('purchase_behaviour.csv')
transaction_data = pd.read_csv('transaction_data.csv')

purchase_behaviour.columns = purchase_behaviour.columns.str.strip()
transaction_data.columns = transaction_data.columns.str.strip()


merged_data = pd.merge(transaction_data, purchase_behaviour, on='LYLTY_CARD_NBR', how='inner')


all_products = (
    merged_data.groupby('PROD_NAME')['TOT_SALES']
    .sum()
    .sort_values(ascending=False)
)


all_loyal_customers = (
    merged_data.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES']
    .sum()
    .sort_values(ascending=False)
)


plt.figure(figsize=(30, 20))
all_products.plot(kind='bar', color='skyblue')
plt.title('Profitability of All Products')
plt.ylabel('Total Sales')
plt.xlabel('Product Name')
plt.xticks(rotation=90)
plt.savefig('Probability of All Products.png')
plt.show()

plt.figure(figsize=(30, 20))
all_loyal_customers.plot(kind='bar', color='orange')
plt.title('Sales by All Customer Segments')
plt.ylabel('Total Sales')
plt.xlabel('Customer Segment')
plt.xticks(rotation=45)
plt.savefig('Sales by All Customer Segments.png')
plt.show()

top_products = (
    merged_data.groupby('PROD_NAME')['TOT_SALES']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

loyal_customers = (
    merged_data.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

plt.figure(figsize=(20, 20))
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 3 Most Profitable Products')
plt.ylabel('Total Sales')
plt.xlabel('Product Name')
plt.xticks(rotation=45)

plt.savefig('Top 3 Most Profitable Products.png')
plt.show()

plt.figure(figsize=(20, 20))
loyal_customers.plot(kind='bar', color='orange')
plt.title('Most Loyal Customer Segments by Sales')
plt.ylabel('Total Sales')
plt.xlabel('Customer Segment')
plt.xticks(rotation=45)

plt.savefig('Most Loyal Customer Segments by Sales.png')
plt.show()

loyalty_by_frequency = (
    merged_data.groupby('LYLTY_CARD_NBR')['TXN_ID']
    .nunique()
    .sort_values(ascending=False)
)


print("Most Profitable Products:")
print(all_products.head(3))

print("\nCharacteristics of Most Loyal Customers:")
print(all_loyal_customers.head(3))

print("\nTop 3 Most Frequent Buyers:")
print(loyalty_by_frequency.head(3))

