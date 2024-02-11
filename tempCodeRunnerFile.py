
# @bot.message_handler(func=lambda message: message.text == 'Button 2')
# def handle_button2(message):
#     # Replace with your actual URL
#     img_urls = scrape_website('your website url')  
#     for img_url in img_urls:
#         if not img_url.startswith('http'):
#             img_url = 'actual base URL' + img_url  # Replace with your actual base URL
#         try:
#             response = requests.get(img_url)
#             response.raise_for_status()
#         except (requests.HTTPError, requests.ConnectionError):
#             print(f"Unable to access image at {img_url}")
#             continue
#         bot.send_photo(CHANNEL_ID, img_url)  # Send the image to the channel

# @bot.message_handler(func=lambda message: message.text == 'Button 3')
# def handle_button3(message):
#     # Replace with your actual URL
#     img_urls = scrape_website('your website url')  
#     for img_url in img_urls:
#         if not img_url.startswith('http'):
#             img_url = 'actual base URL' + img_url  # Replace with your actual base URL
#         try:
#             response = requests.get(img_url)
#             response.raise_for_status()
#         except (requests.HTTPError, requests.ConnectionError):
#             print(f"Unable to access image at {img_url}")
#             continue
#         bot.send_photo(CHANNEL_ID, img_url)  # Send the image to the channel

# @bot.message_handler(func=lambda message: message.text == 'Button 4')
# def handle_button4(message):
#     # Replace with your actual URL
#     img_urls = scrape_website('your website url')  
#     for img_url in img_urls:
#         if not img_url.startswith('http'):
#             img_url = 'actual base URL' + img_url  # Replace with your actual base URL
#         try:
#             response = requests.get(img_url)
#             response.raise_for_status()
#         except (requests.HTTPError, requests.ConnectionError):
#             print(f"Unable to access image at {img_url}")
#             continue
#         bot.send_photo(CHANNEL_ID, img_url)  # Send the image to the channel

