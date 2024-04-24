import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    # Send a GET request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract product name
        product_name_element = soup.find('span', id='productTitle')
        product_name = product_name_element.get_text().strip() if product_name_element else None
        
        # Extract product price
        product_price_element = soup.find('span', {'class': 'a-price-whole'})
        product_price = product_price_element.get_text().strip() if product_price_element else None
        
        # Extract product ratings
        ratings_element = soup.find('span', {'class': 'a-icon-alt'})
        ratings = ratings_element.get_text().strip() if ratings_element else None
        
        # Extract product comments/reviews
        comments = []
        review_section = soup.find('div', {'id': 'reviewsMedley'})
        if review_section:
            review_list = review_section.find_all('div', {'data-hook': 'review'})
            for review in review_list:
                comment_element = review.find('span', {'data-hook': 'review-body'})
                comment = comment_element.get_text().strip() if comment_element else None
                if comment:
                    comments.append(comment)
        
        # Return the extracted data
        return {
            'product_name': product_name,
            'product_price': product_price,
            'ratings': ratings,
            'comments': comments
        }
    else:
        # If the request was not successful, print an error message
        print('Failed to retrieve data from the URL:', url)
        return None

# Example URL of a product on Amazon India
url = 'https://www.amazon.in/dp/B0BSRV1YGK/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0BSRV1YGK&pd_rd_w=D02xA&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=GN1E0Y8BWGES07TMJVQ8&pd_rd_wg=10jbx&pd_rd_r=392bece6-6fa8-4720-8015-b313d81525fb&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM'

# Call the function to get data from the provided URL
product_data = get_product_data(url)

# Print the extracted data
if product_data:
    print("Product Name:", product_data['product_name'])
    print("Price:", product_data['product_price'])
    print("Ratings:", product_data['ratings'])
    print("Comments:")
    for idx, comment in enumerate(product_data['comments'], 1):
        print(f"{idx}. {comment}")
