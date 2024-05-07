from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_881b77a9-f36f-431e-8436-22ec8733aac7'

API_TOKEN = 'ISSecretKey_test_8f5ecb0e-1218-478e-9306-af0ffd2f0485'

service = APIService(token=API_TOKEN , publishable_key= API_PUBLISHABLE_KEY , test=True)
create_order = service.collect.mpesa_stk_push(phone_number= +254714130512 , email='test@gmail.com' , amount=100 , narrative='purchase of laptops')
print(create_order)