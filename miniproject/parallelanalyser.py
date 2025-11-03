import random
import matplotlib.pyplot as plt


print("======================================")
print("     PARALLEL SALES DATA ANALYZER     ")
print("======================================")

num_regions = int(input("Enter number of regions: "))
stores_per_region = int(input("Enter number of stores per region: "))
products_per_store = int(input("Enter number of products per store: "))

regions = []
for i in range(num_regions):
    reg = input(f"Enter name of region {i+1}: ")
    regions.append(reg)

print("\nGenerating random sales data..\n")

sales_data = {}
for region in regions:
    region_sales = []
    for store in range(stores_per_region):
        store_sales = [random.randint(50, 500) for _ in range(products_per_store)]
        region_sales.append(store_sales)
    sales_data[region] = region_sales

print("Random sales data generated successfully\n")

def analyze_region(region_data):
    total_sales = 0
    total_items = 0
    max_sale = 0
    product_sum = [0]*products_per_store

    for store in region_data:
        total_sales += sum(store)
        total_items += len(store)
        max_sale = max(max_sale, max(store))
        for i, val in enumerate(store):
            product_sum[i] += val

    avg_sales = total_sales / total_items
    top_product = product_sum.index(max(product_sum))

    return {
        "total": total_sales,
        "average": avg_sales,
        "peak": max_sale,
        "top_product_index": top_product,
        "product_totals": product_sum
    }

results = []
for region in regions:
    results.append(analyze_region(sales_data[region]))

region_totals = [r['total'] for r in results]
total_products = [0]*products_per_store
for res in results:
    for i in range(products_per_store):
        total_products[i] += res['product_totals'][i]

national_total = sum(region_totals)
national_avg = national_total / (num_regions * stores_per_region * products_per_store)
top3_products = sorted(range(products_per_store),
                       key=lambda x: total_products[x],
                       reverse=True)[:3]

high_region_index = region_totals.index(max(region_totals))
low_region_index = region_totals.index(min(region_totals))

fig, ax = plt.subplots(2, 2, figsize=(15, 9))
fig.suptitle("Parallel Sales Data Dashboard", fontsize=16)

# Graph 1: regional total
colors = ['skyblue']*len(regions)
colors[high_region_index] = 'green'
colors[low_region_index] = 'red'
ax[0,0].bar(regions, region_totals, color=colors)
ax[0,0].set_title("Total Sales per Region")
ax[0,0].set_ylabel("Sales Amount")

# Graph 2: top product per region
ax[0,1].bar(regions,
            [results[i]['product_totals'][results[i]['top_product_index']] for i in range(len(regions))],
            color='orange')
ax[0,1].set_title("Top Product per Region")
ax[0,1].set_ylabel("Units Sold")

# Graph 3: Product-wise National Totals
prod_colors = ['lightblue']*products_per_store
for idx in top3_products:
    prod_colors[idx] = 'gold'
ax[1,0].bar([f"P{i}" for i in range(products_per_store)], total_products, color=prod_colors)
ax[1,0].set_title("Total Sales per Product (National)")
ax[1,0].set_xlabel("Products")
ax[1,0].set_ylabel("Units Sold")

# Graph 4: Summary Box
summary = f"""
National Total Sales: {national_total}
National Average Sale: {national_avg:.2f}
Top 3 Products: {', '.join(['P'+str(i) for i in top3_products])}
Best Region: {regions[high_region_index]}
Lowest Region: {regions[low_region_index]}
"""
ax[1,1].axis('off')
ax[1,1].text(0.05, 0.5, summary, fontsize=12, va='center')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

save_opt = input("\nDo you want to save the dashboard as an image (yes/no)? ").strip().lower()
if save_opt == 'yes':
    plt.savefig("sales_dashboard.png", dpi=300)
    print("Dashboard saved as 'sales_dashboard.png'")

print("\n--- Analysis Completed Successfully ---")
