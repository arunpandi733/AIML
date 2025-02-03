import streamlit as st
from zomato_data_analaysis import Deliveries, Orders, Delivery_persons, Restaurants, Customer

custom_obj = Customer()
res_ = Restaurants()
deli_per = Delivery_persons()
ord = Orders()
deliver = Deliveries()
st.title("🍽️ Zomato Customer Management")

# Main Menu
menu = st.sidebar.selectbox("Main Menu", ["Customer", "Restaurants", "Orders", "Deliveries", "Delivery Persons"])

if menu == "Customer":
    submenu = st.sidebar.radio("Customer Actions", ["View Customers", "Add Customer", "Update Customer", "Change Status", "Delete Customer"])

    # View Customers
    if submenu == "View Customers":
        st.subheader("📋 All Customers")
        customers = custom_obj.get_customers()
        if customers:
            st.table(customers)
        else:
            st.write("No customers found.")

    elif submenu == "Add Customer":
        st.subheader("➕ Add New Customer")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        location = st.text_input("Location")
        is_premium = st.selectbox("Is Premium?", ["yes", "no"])
        preferred_cuisine = st.text_input("Preferred Cuisine")
        average_rating = st.slider("Average Rating", min_value=0.0, max_value=5.0, step=0.1)

        if st.button("Add Customer"):
            result = custom_obj.customer_insert(name, email, phone, location, is_premium, preferred_cuisine, average_rating)
            st.success(result)

    elif submenu == "Update Customer":
        st.subheader("✏️ Update Customer Information")
        # Get Customer ID
        customer_id = st.number_input("Customer ID", min_value=1, step=1)
        if customer_id:
            customers_data = custom_obj.get_customers_active_list(customer_id)

            if customers_data:

                name = st.text_input("New Name", value=customers_data[0]["name"])
                email = st.text_input("New Email", value=customers_data[0]["email"])
                phone = st.text_input("New Phone", value=customers_data[0]["phone"])
                location = st.text_input("New Location", value=customers_data[0]["location"])
                is_premium = st.selectbox("Is Premium?", ["yes", "no"], index=0 if customers_data[0]["is_premium"] == "yes" else 1)
                preferred_cuisine = st.text_input("New Preferred Cuisine", value=customers_data[0]["preferred_cuisine"])
                average_rating = st.slider("New Average Rating", min_value=0.0, max_value=5.0, step=0.1,
                                           value=customers_data[0]["average_rating"])

                if st.button("Update Customer"):
                    result = custom_obj.customer_update(customer_id, name, email, phone, location, is_premium,
                                                    preferred_cuisine, average_rating)
                    st.success(result)
            else:
                st.warning("Customer ID not found. Please enter a valid ID.")


    elif submenu == "Change Status":
        st.subheader("✏️ Update Customer Status")

        customer_id = st.number_input("Customer ID", min_value=1, step=1)
        status_value = st.selectbox("Status", ["active", "inactive"])
        if st.button("Change Status"):
            result = custom_obj.customer_status_change(customer_id, status_value)
            st.success(result)


    elif submenu == "Delete Customer":
        st.subheader("❌ Delete Customer")

        customer_id = st.number_input("Customer ID to Delete", min_value=1, step=1)
        if st.button("Delete Customer"):
            result = custom_obj.customer_delete(customer_id)
            st.warning(result)

elif menu == "Restaurants":
    submenu = st.sidebar.radio("Restaurants Actions", ["View Restaurants", "Add Restaurants", "Update Restaurants", "Change Status", "Delete Restaurants"])

    if submenu == "View Restaurants":
        st.subheader("📋 All Restaurants")
        res_lists = res_.get_restaurants()
        if res_lists:
            st.table(res_lists)
        else:
            st.write("No Restaurants found.")

    elif submenu == "Add Restaurants":
        st.subheader("➕ Add New Restaurants")

        name = st.text_input("Name")
        cuisine_type = st.text_input("Cuisine Type")
        location = st.text_input("Location")
        owner_name = st.text_input("Owner Name")
        average_delivery_time = st.text_input("Average Delivery Time")
        contact_number = st.text_input("Contact Number")
        rating = st.slider("Rating",  min_value=0.0, max_value=5.0, step=0.1)
        total_orders = st.text_input("Total Orders")

        if st.button("Add Restaurants"):
            result_ = res_.restaurants_insert(name, cuisine_type, location, owner_name, average_delivery_time, contact_number, rating, total_orders)
            st.success(result_)

    elif submenu == "Update Restaurants":

        st.subheader("➕ Add New Customer")

        restaurants_id = st.number_input("Restaurant ID", min_value=1, step=1)
        if restaurants_id:
            restaurants_data = res_.get_restaurants_list_active(restaurants_id)

            if restaurants_data:

                name = st.text_input("Name", value=restaurants_data[0]["name"])
                cuisine_type = st.text_input("Cuisine Type", value=restaurants_data[0]["cuisine_type"])
                location = st.text_input("Location", value=restaurants_data[0]["location"])
                owner_name = st.text_input("Owner Name", value=restaurants_data[0]["owner_name"])
                average_delivery_time = st.text_input("Average Delivery Time", value=restaurants_data[0]["average_delivery_time"])
                contact_number = st.text_input("Contact Number", value=restaurants_data[0]["contact_number"])
                rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1, value=restaurants_data[0]["rating"])
                total_orders = st.text_input("Total Orders", value=restaurants_data[0]["total_orders"])

                if st.button("Add Restaurants"):
                    result_ = res_.restaurants_insert(name, cuisine_type, location, owner_name, average_delivery_time,
                                                      contact_number, rating, total_orders)
                    st.success(result_)


                else:
                    st.warning("Restaurants ID not found. Please enter a valid ID.")

    elif submenu == "Change Status":
        st.subheader("✏️ Update Restaurants Status")

        restaurant_id = st.number_input("Restaurant ID", min_value=1, step=1)
        status_value = st.selectbox("Status", ["active", "inactive"])
        if st.button("Change Status Update"):
            result = res_.restaurants_status_change(restaurant_id, status_value)
            st.success(result)


    elif submenu == "Delete Restaurants":
        st.subheader("✏️ Delete Restaurants Status")
        restaurant_id = st.number_input("Restaurant ID", min_value=1, step=1)
        if st.button("Change Status Update"):
            result = res_.restaurants_delete(restaurant_id)
            st.success(result)

elif menu == "Delivery Persons":
    submenu = st.sidebar.radio("Delivery Persons Actions", ["View Delivery Persons", "Add Delivery Persons", "Update Delivery Persons", "Change Status", "Delete Delivery Persons"])

    if submenu == "View Delivery Persons":
        st.subheader("📋 All Delivery Persons")
        deliver_peron = deli_per.get_person_details()
        if deliver_peron:
            st.table(deliver_peron)
        else:
            st.write("No Delivery Persons found.")

    elif submenu == "Add Delivery Persons":
        st.subheader(" Add Delivery Persons ")

        name = st.text_input("Name")
        contact_number = st.text_input("Contact Number")
        vehicle_type = st.text_input("Vehicle Type")
        total_deliveries = st.text_input("Total Deliveries")
        average_rating = st.slider("Average Rating", min_value=0.0, max_value=5.0, step=0.1)
        location = st.text_input("Location")

        if st.button("Add Persons"):
            result_ = deli_per.persons_insert(name, contact_number, vehicle_type, location, total_deliveries, average_rating)
            st.success(result_)

    elif submenu == "Update Delivery Persons":
        st.subheader(" Update Delivery Persons ")

        person_id = st.number_input("Restaurant ID", min_value=1, step=1)
        if person_id:
            restaurants_data = deli_per.person_active_list(person_id)

            if restaurants_data:
                name = st.text_input("Name", value=restaurants_data[0]["name"])
                contact_number = st.text_input("Contact Number", value=restaurants_data[0]["contact_number"])
                vehicle_type = st.text_input("Vehicle Type", value=restaurants_data[0]["vehicle_type"])
                total_deliveries = st.text_input("Total Deliveries", value=restaurants_data[0]["total_deliveries"])
                average_rating = st.slider("Average Rating", min_value=0.0, max_value=5.0, step=0.1, value=restaurants_data[0]["average_rating"])
                location = st.text_input("Location", value=restaurants_data[0]["location"])

                if st.button("Add Persons"):
                    result_ = deli_per.persons_update(person_id, name, contact_number, vehicle_type, location, total_deliveries,
                                                      average_rating)
                    st.success(result_)

            else:
                st.warning("Delivery Person Not Available This Delivery Person ID")

    elif submenu == "Change Status":
        st.subheader("✏️ Update Delivery Person Status")

        delivery_person_id = st.number_input("Delivery Person ID", min_value=1, step=1)
        status_value = st.selectbox("Status", ["active", "inactive"])
        if st.button("Change Status Update"):
            result = deli_per.person_update_status(delivery_person_id, status_value)
            st.success(result)

    elif submenu == "Delete Delivery Persons":
        st.subheader(" Delete Delivery Person")
        delivery_person_id = st.number_input("Delivery Person ID", min_value=1, step=1)
        if st.button("Delete Delivery Person"):
            result = deli_per.person_delete(delivery_person_id)
            st.warning(result)

elif menu == "Orders":
    submenu = st.sidebar.radio("Orders Actions", ["View Orders", "Add Orders", "Update Process Status", "Update Orders FeedBack", "Change Status", "Delete Orders"])

    if submenu == "View Orders":
        st.subheader("📋 All Orders")
        order_list = ord.get_orders()
        if order_list:
            st.table(order_list)
        else:
            st.write("No Order found.")


    elif submenu == "Add Orders":
        st.subheader(" Add New Orders")
        customer_id = st.number_input("Customer ID", min_value=1, step=1)
        restaurant_id = st.number_input("Restaurant ID", min_value=1, step=1)
        delivery_time = st.text_input("Delivery Time")
        total_amount = st.text_input("Total Amount")
        payment_mode = st.selectbox("payment Mode", ['credit_cart','cash','debit_card','UPI'])
        discount_applied = st.selectbox("Discount Applied", ["Yes", "No"])

        if st.button("Add Orders Data"):
            result_ = ord.orders_insert(customer_id, restaurant_id, total_amount, payment_mode, discount_applied)
            st.success(result_)

    elif submenu == "Update Orders FeedBack":
        st.subheader(" Update Orders FeedBack")

        order_id = st.number_input("Order ID", min_value=1, step=1)
        feedback_rating = st.slider("Feedback Rating", min_value=0.0, max_value=5.0, step=0.1)

        if st.button("Order FeedBack"):
            result = ord.order_rating_update(order_id, feedback_rating)
            st.success(result)

    elif submenu == "Change Status":
        st.subheader("Update Status Order")
        order_id = st.number_input("Order ID", min_value=1, step=1)
        status_value = st.selectbox("Status", ["active", "inactive"])

        if st.button("Change Order Status"):
            result = ord.order_status_changes(order_id, status_value)
            st.success(result)

    elif submenu == "Update Process Status":
        st.subheader("Update Process Status Order")
        order_id = st.number_input("Order ID", min_value=1, step=1)
        status_value = st.selectbox("Status", ["pending","delivered","cancelled"])

        if st.button("Change Order Status"):
            result = ord.order_status_update(order_id, status_value)
            st.success(result)

    elif submenu == "Delete Orders":
        st.subheader("Delete Orders")
        order_id = st.number_input("Order ID", min_value=1, step=1)

        if st.button("Delete Order Details"):
            result = ord.order_list_delete(order_id)
            st.success(result)

elif menu == "Deliveries":
    submenu = st.sidebar.radio("Deliveries Actions", ["View Deliveries", "Add Deliveries", "Update Deliveries Time", "Update Deliveries status"])

    if submenu == "View Deliveries":
        st.subheader("All Deliveries")

        table_data = deliver.all_delivery_list()
        if table_data:
            st.table(table_data)
        else:
            st.write("No Deliveries found.")


    elif submenu == "Add Deliveries":
        st.subheader("Add New Deliveries")

        order_id = st.number_input("Order ID", min_value=1, step=1)
        delivery_person_id = st.number_input('Delivery Person ID', min_value=1, step=1)
        distance = st.text_input('Distance')
        estimated_time = st.text_input('Estimated Time')
        delivery_fee = st.text_input('Delivery Fee')
        vehicle_type = st.selectbox('Vehicle Type', ["Bike", "Car"])

        if st.button("Add New Deliveries"):
            result = deliver.delivery_insert(order_id, delivery_person_id, distance, estimated_time, delivery_fee, vehicle_type)
            st.success(result)

    elif submenu == "Update Deliveries Time":
        st.subheader("Update deliver Time")

        delivery_id = st.number_input("Delivery ID", min_value=1, step=1)
        delivery_time = st.text_input("Delivery Time")

        if st.button("Update Time"):
            result = deliver.update_delivery_time(delivery_id, delivery_time)
            st.success(result)

    elif submenu == "Update Deliveries status":
        st.subheader("Update Delivery Status")

        delivery_id = st.number_input("Delivery ID", min_value=1, step=1)
        delivery_status = st.selectbox("Delivery Status", ["on_the_way", "delivered"])

        if st.button("Update status"):
            result = deliver.update_delivery_status(delivery_id, delivery_status)
            st.success(result)


