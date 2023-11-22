from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, \
    create_product_flutter
from main.views import register, login_user, logout_user, remove_product, increment_amount, decrement_amount, edit_product, delete_product
from main.views import get_product_json, add_item_ajax, delete_item_ajax, inc_item_ajax, dec_item_ajax
app_name = 'main'

urlpatterns = [
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('dec-item-ajax/<int:id>/', dec_item_ajax, name='dec_item_ajax'),
    path('inc-item-ajax/<int:id>/', inc_item_ajax, name='inc_item_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('increment_amount/<int:product_id>/', increment_amount, name='increment_amount'),
    path('decrement_amount/<int:product_id>/', decrement_amount, name='decrement_amount'),
    path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('create-product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
]