# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DB_CASCADE)
    product = models.ForeignKey('Products', models.DB_CASCADE)
    quantity = models.IntegerField()
    variant_details = models.JSONField(blank=True, null=True)
    added_at = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cart'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DB_CASCADE, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    display_order = models.IntegerField()
    is_active = models.BooleanField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DB_CASCADE)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    variant_details = models.JSONField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DB_CASCADE)
    order_number = models.CharField(unique=True, max_length=50)
    invoice_number = models.CharField(unique=True, max_length=50, blank=True, null=True)
    guest_email = models.CharField(max_length=100, blank=True, null=True)
    guest_phone = models.CharField(max_length=20, blank=True, null=True)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=20)
    delivery_date = models.DateField(blank=True, null=True)
    customer_notes = models.TextField(blank=True, null=True)
    admin_notes = models.TextField(blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)
    return_reason = models.TextField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.OneToOneField(Orders, models.DB_CASCADE)
    user = models.ForeignKey('Users', models.DB_CASCADE)
    transaction_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_method = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    gateway_status_code = models.CharField(max_length=20, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller = models.ForeignKey('Users', models.DB_CASCADE)
    category = models.ForeignKey(Categories, models.DB_SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sku = models.CharField(unique=True, max_length=50)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    stock_quantity = models.IntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    images = models.JSONField()
    variants = models.JSONField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()
    is_approved = models.BooleanField()
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Products, models.DB_CASCADE)
    user = models.ForeignKey('Users', models.DB_CASCADE)
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField()
    title = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    images = models.JSONField()
    videos = models.JSONField()
    verified_purchase = models.BooleanField()
    is_approved = models.BooleanField()
    is_featured = models.BooleanField()
    admin_response = models.TextField(blank=True, null=True)
    admin_response_at = models.DateTimeField(blank=True, null=True)
    seller_response = models.TextField(blank=True, null=True)
    seller_response_at = models.DateTimeField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=254)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=20)
    profile_image = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50)
    email_verified = models.BooleanField()
    phone_verified = models.BooleanField()
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    password_reset_token = models.CharField(max_length=100, blank=True, null=True)
    password_reset_expires = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    is_approved = models.BooleanField()
    is_blocked = models.BooleanField()
    language = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    notification_preferences = models.JSONField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
