---
title: "Django: Create multiple admin instances"
description: "create multiple admin instances in Django"
date: 2024-06-12T15:00:00Z
image: "/images/posts/post1/1.jpeg"
categories: ["Django"]
authors: ["Mina Atef"]
tags: ["django","django admin", "python", "web development"]
draft: false
---

# Creating Multiple Django Admin Instances

Having multiple Django admin sites is crucial. The ability to split the admin into multiple instances, each with its permissions, models, and logic, can be incredibly valuable.

So, how can we do it?

```python
# Creating multiple Django admin instances
from django.contrib.admin import AdminSite
from myapp.models import orders  # Adjust 'myapp' to your app's name

class OrdersAdmin(AdminSite):
    site_header = "Orders Admin"
    site_title = "Orders Admin Site"
    index_title = "Orders Admin"  
    site_url = ""

orders_admin = OrdersAdmin(name='orders_admin')
orders_admin.register(orders)
```

```python
# in urls.py
from django.urls import path
from orders.admin import orders_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders-admin/', orders_admin.urls)
]
```