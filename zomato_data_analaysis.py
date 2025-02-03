
from database_conection import database_connection

class Customer:
    def __init__(self):
        self.db = database_connection()

    def customer_check(self, curer, customer_id, name, email, phone):
        where = ''
        if customer_id != '':
            where = f" and customer_id <> '{customer_id}'"
        query = f"SELECT * FROM customers WHERE is_active <> 'delete' and name = '{name}' AND (email = '{email}' OR phone = '{phone}') {where}"
        curer.execute(query)
        return curer.fetchall()

    def customer_insert(self, name, email, phone, location, is_premium, preferred_cuisine, average_rating):
        with self.db.cursor() as curer:
            if self.customer_check(curer, '', name, email, phone):
                return "This Data Already Available"
            query = f"""INSERT INTO customers set 
                name = '{name}', 
                email = '{email}', 
                phone = '{phone}', 
                location = '{location}', 
                signup_date = now(), 
                is_premium = '{is_premium}', 
                preferred_cuisine = '{preferred_cuisine}', 
                average_rating = '{average_rating}'
            """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Data Saved Successfully"

    def customer_update(self, customer_id, name, email, phone, location, is_premium, preferred_cuisine, average_rating):
        """Update an existing customer's details."""
        with self.db.cursor() as curer:
            if self.customer_check(curer, customer_id, name, email, phone):
                return "This Data Already Available"
            query = f"""UPDATE customers SET 
                name = '{name}', 
                email = '{email}', 
                phone = '{phone}', 
                location = '{location}', 
                signup_date = now(), 
                is_premium = '{is_premium}', 
                preferred_cuisine = '{preferred_cuisine}', 
                average_rating = '{average_rating}'
            WHERE customer_id = '{customer_id}'
            """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Data Updated Successfully"

    def customer_status_change(self, customer_id, status):
        with self.db.cursor() as curer:
            query = f"""Update customers set is_active = '{status}' where customer_id = '{customer_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()

    def customer_delete(self, customer_id):
        with self.db.cursor() as curer:
            query = f"Update customers set is_active = 'delete' WHERE customer_id = '{customer_id}'"
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Customer Deleted Successfully"

    def get_customers_active_list(self, customer_id):
        where = ''
        if customer_id != '':
            where = f" and customer_id = '{customer_id}' Limit 1"
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM customers where is_active = 'active' {where}")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

    def get_customers(self):
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM customers WHERE is_active <> 'delete'")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

class Restaurants:
    def __init__(self):
        self.db = database_connection()

    def restaurants_check(self, curer, restaurant_id, name, cuisine_type):
        where = ''
        if restaurant_id != '':
            where = f" and restaurant_id <> '{restaurant_id}'"
        query = f"SELECT * FROM restaurants WHERE is_active <> 'delete' and name = '{name}' and cuisine_type = '{cuisine_type}' {where}"
        curer.execute(query)
        return curer.fetchall()

    def restaurants_insert(self, name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders):
        with self.db.cursor() as curer:
            if self.restaurants_check(curer, '', name, cuisine_type):
                return "This Data Already Available"
            query = f"""Insert Into restaurants set 
                        name = '{name}',
                        cuisine_type = '{cuisine_type}',
                        location = '{location}',
                        owner_name = '{owner_name}',
                        average_delivery_time = '{average_delivery_time}',
                        contact_number = '{contact_number}',
                        rating = '{rating}',
                        total_orders = '{total_orders}'
                        """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Data Saved Successfully"

    def restaurants_update(self, restaurant_id, name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders):
        with self.db.cursor() as curer:
            if self.restaurants_check(curer, restaurant_id, name, cuisine_type):
                return "This Data Already Available"
            query = f"""Update restaurants set 
                        name = '{name}',
                        cuisine_type = '{cuisine_type}',
                        location = '{location}',
                        owner_name = '{owner_name}',
                        average_delivery_time = '{average_delivery_time}',
                        contact_number = '{contact_number}',
                        rating = '{rating}',
                        total_orders = '{total_orders}'
                        where restaurant_id = '{restaurant_id}'
                        """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Data Update Successfully"

    def restaurants_status_change(self, restaurant_id, status):
        with self.db.cursor() as curer:
            query = f"""Update restaurants set is_active = '{status}' where restaurant_id = '{restaurant_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()

    def restaurants_delete(self, restaurant_id):
        with self.db.cursor() as curer:
            query = f"Update restaurants set is_active = 'delete' WHERE restaurant_id = '{restaurant_id}'"
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Restaurant Deleted Successfully"

    def get_restaurants_list_active(self, restaurant_id):
        where = ''
        if restaurant_id != '':
            where = f" and restaurant_id = '{restaurant_id}' Limit 1"
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM restaurants where is_active = 'active' {where}")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

    def get_restaurants(self):
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM restaurants WHERE is_active <> 'delete'")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

class Orders:

    def __init__(self):
        self.db = database_connection()

    def orders_insert(self, customer_id, restaurant_id, total_amount, payment_mode, discount_applied):
        with self.db.cursor() as curer:
            query = f"""Insert Into orders set 
                        customer_id = '{customer_id}',
                        restaurant_id = '{restaurant_id}',
                        order_date = now(),
                        delivery_time = now(),
                        total_amount = '{total_amount}',
                        payment_mode = '{payment_mode}',
                        discount_applied = '{discount_applied}'
                        """
            curer.execute(query)
            self.db.commit()
            query = f"""update customers set total_orders = total_orders + 1 where customer_id = '{customer_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Save Data Successfully"

    def order_rating_update(self, order_id, feedback_rating):

        with self.db.cursor() as curer:
            query = f"""Update orders set
                        feedback_rating = '{feedback_rating}'
                        where order_id = '{order_id}'
                    """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Order Rating Successfully"

    def order_status_update(self, order_id, order_status):

        with self.db.cursor() as curer:
            query = f"""Update orders set
                        status = '{order_status}'
                        where order_id = '{order_id}'
                    """
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Order Status Successfully"

    def order_status_changes(self, order_id, is_active):
        with self.db.cursor() as curer:
            query = f"""Update orders set is_active = '{is_active}' where order_id = '{order_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Status Successfully"

    def order_list_delete(self, order_id):
        with self.db.cursor() as curer:
            query = f"""Update orders set is_active = 'delete' where order_id = '{order_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return  "Order Delete Successfully"

    def get_order_list(self, order_id):
        where = ''
        if order_id != '':
            where = f" and order_id = '{order_id}' Limit 1"
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM order where is_active = 'active' {where}")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

    def get_orders(self):
        with self.db.cursor() as curer:
            curer.execute(f"SELECT * FROM orders WHERE is_active <> 'delete'")
            get_data = curer.fetchall()
            curer.close()
            self.db.close()
            return get_data

class Delivery_persons:

    def __init__(self):
        self.db = database_connection()

    def persons_check(self,  curer, person_id, name, contact_number, vehicle_type):
        where = ''
        if person_id != '':
            where += f" and delivery_person_id = '{person_id}'"
        query = f"Select * from delivery_persons where is_active <> 'delete' and name = '{name}' and contact_number = '{contact_number}' and vehicle_type = '{vehicle_type}' {where}"
        curer.execute(query)
        get_data = curer.fetchall()
        return get_data

    def persons_insert(self, name, contact_number, vehicle_type, location, total_deliveries, average_rating):
        with self.db.cursor() as curer:
            if self.persons_check(curer, '', name, contact_number, vehicle_type):
                return  "Already Exsit"
            query = f"""Insert into delivery_persons set
                        name = '{name}',
                        contact_number = '{contact_number}',
                        vehicle_type = '{vehicle_type}',
                        total_deliveries = '{total_deliveries}',
                        average_rating = '{average_rating}',
                        location = '{location}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return  "Save Data Successfully"

    def persons_update(self, person_id, name, contact_number, vehicle_type, location, total_deliveries, average_rating):
        with self.db.cursor() as curer:
            if self.persons_check(curer, person_id, name, contact_number, vehicle_type, location):
                return "Already Exsit"
            query = f"""Update delivery_persons set
                            name = '{name}',
                            contact_number = '{contact_number}',
                            vehicle_type = '{vehicle_type}',
                            total_deliveries = '{total_deliveries}',
                            average_rating = '{average_rating}',
                            location = '{location}'
                        where delivery_person_id = '{person_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Data Successfully"

    def person_update_status(self, person_id, status):
        with self.db.cursor() as curer:
            query = f"update delivery_persons set is_active = '{status}' where delivery_person_id = '{person_id}'"
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Data Successfully"

    def person_delete(self, person_id):
        with self.db.cursor() as curer:
            query = f"update delivery_persons set is_active = 'delete' where delivery_person_id = '{person_id}'"
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Delete Data Successfully"

    def person_active_list(self, person_id):
        where = ""
        if person_id != '':
            where += f" and delivery_person_id = '{person_id}' limit 1"
        with self.db.cursor() as curer:
            query = f"Select * from delivery_persons where is_active = 'active' {where}"
            curer.execute(query)
            get_data = curer.fetchall()
            return  get_data

    def get_person_details(self):
        with self.db.cursor() as curer:
            query = f"Select * from delivery_persons where is_active = 'active'"
            curer.execute(query)
            get_data = curer.fetchall()
            return  get_data

class Deliveries:
    def __init__(self):
        self.db = database_connection()

    def delivery_insert(self, order_id, delivery_person_id, distance, estimated_time, delivery_fee, vehicle_type):
        with self.db.cursor() as curer:
            query = f"""Insert Into deliveries set
                        order_id = '{order_id}',
                        delivery_person_id = '{delivery_person_id}',
                        distance = '{distance}',
                        estimated_time = '{estimated_time}',
                        delivery_fee = '{delivery_fee}',
                        vehicle_type = '{vehicle_type}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Save Data Successfully"

    def update_delivery_time(self, delivery_id, delivery_time):
        with self.db.cursor() as curer:
            query = f"""Update deliveries set
                        delivery_time = '{delivery_time}'
                    where delivery_id = '{delivery_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Data Successfully"

    def update_delivery_status(self, delivery_id, delivery_status):
        with self.db.cursor() as curer:
            query = f"""Update deliveries set
                        delivery_status = '{delivery_status}'
                    where delivery_id = '{delivery_id}'"""
            curer.execute(query)
            self.db.commit()
            curer.close()
            self.db.close()
            return "Update Data Successfully"

    def all_delivery_list(self):
        with self.db.cursor() as curer:
            query = f"""Select
                            ds.*
                        From 
                            deliveries ds
                            INNER JOIN orders od on od.order_id=ds.order_id
                            INNER JOIN delivery_persons dp on dp.delivery_person_id=ds.delivery_person_id"""
            curer.execute(query)
            get_data = curer.fetchall()
            return get_data