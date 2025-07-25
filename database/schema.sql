-- Users Table
CREATE TABLE users_tb (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    user_role INTEGER NOT NULL DEFAULT 0,
    user_status INTEGER NOT NULL DEFAULT 0,
    last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    profile VARCHAR(50) NOT NULL DEFAULT 'default.png'
);

-- Farmers Table
CREATE TABLE farmers_tb (
    farmer_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_date DATE DEFAULT CURRENT_DATE
);

-- Farms Table
CREATE TABLE farm_tb (
    farm_id SERIAL PRIMARY KEY,
    farm_name VARCHAR(200) NOT NULL,
    location VARCHAR(200) NOT NULL,
    farm_size VARCHAR(50) NOT NULL,
    farmer_id INTEGER NOT NULL,
    FOREIGN KEY (farmer_id) REFERENCES farmers_tb(farmer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Batches Table
CREATE TABLE batches_tb (
    batch_id SERIAL PRIMARY KEY,
    farm_id INTEGER NOT NULL,
    breed_id INTEGER NOT NULL,
    arrive_date DATE NOT NULL,
    init_age INTEGER NOT NULL,
    harvest_age INTEGER NOT NULL DEFAULT 0,
    quantity INTEGER NOT NULL,
    init_weight INTEGER NOT NULL,
    batch_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (farm_id) REFERENCES farm_tb(farm_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (breed_id) REFERENCES breed_tb(breed_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Breeds Table
CREATE TABLE breed_tb (
    breed_id SERIAL PRIMARY KEY,
    breed_name VARCHAR(50) NOT NULL,
    breed_type_id INTEGER NOT NULL,
    preedphoto VARCHAR(50) NOT NULL DEFAULT 'preedphoto.png',
    FOREIGN KEY (breed_type_id) REFERENCES breed_type_tb(breed_type_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Breed Types Table
CREATE TABLE breed_type_tb (
    breed_type_id SERIAL PRIMARY KEY,
    breed_type VARCHAR(50) NOT NULL
);

-- Activity Types Table
CREATE TABLE activity_type_tb (
    activity_type_id SERIAL PRIMARY KEY,
    activity_type VARCHAR(50) NOT NULL
);

-- Breed Activities Table
CREATE TABLE breed_activities_tb (
    breed_activity_id SERIAL PRIMARY KEY,
    breed_id INTEGER NOT NULL,
    activity_type_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    breed_activity_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (breed_id) REFERENCES breed_tb(breed_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (activity_type_id) REFERENCES activity_type_tb(activity_type_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Batch Activity Table
CREATE TABLE batch_activity_tb (
    batch_activity_id SERIAL PRIMARY KEY,
    batch_id INTEGER NOT NULL,
    breed_activity_id INTEGER NOT NULL,
    batch_activity_name VARCHAR(100) NOT NULL,
    batch_activity_date DATE NOT NULL,
    batch_activity_details VARCHAR(50) NOT NULL,
    batch_activity_cost INTEGER NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batches_tb(batch_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (breed_activity_id) REFERENCES breed_activities_tb(breed_activity_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Activity Schedule Table
CREATE TABLE activity_schedule_tb (
    activity_id SERIAL PRIMARY KEY,
    batch_id INTEGER NOT NULL,
    activity_name VARCHAR(100) NOT NULL,
    activity_description VARCHAR(300) NOT NULL,
    activity_day VARCHAR(10) NOT NULL DEFAULT 'Day',
    activity_status INTEGER NOT NULL,
    activity_frequency INTEGER NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batches_tb(batch_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Batch Feeding Table
CREATE TABLE batch_feeding_tb (
    batch_feeding_id SERIAL PRIMARY KEY,
    batch_id INTEGER NOT NULL,
    feeding_date DATE NOT NULL DEFAULT CURRENT_DATE,
    feeding_amount INTEGER NOT NULL,
    status INTEGER NOT NULL,
    FOREIGN KEY (batch_id) REFERENCES batches_tb(batch_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Breed Feeding Table
CREATE TABLE breed_feeding_tb (
    breed_feeding_id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL DEFAULT 0,
    breed_feed_status INTEGER NOT NULL DEFAULT 1,
    breed_id INTEGER NOT NULL,
    food_type_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    frequency INTEGER NOT NULL,
    FOREIGN KEY (breed_id) REFERENCES breed_tb(breed_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (food_type_id) REFERENCES food_type_tb(food_type_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Food Type Table
CREATE TABLE food_type_tb (
    food_type_id SERIAL PRIMARY KEY,
    food_name VARCHAR(50) NOT NULL
);

-- Breed Growth Table
CREATE TABLE breed_growth_tb (
    breed_growth_id SERIAL PRIMARY KEY,
    breed_id INTEGER NOT NULL,
    age INTEGER NOT NULL,
    min_weight INTEGER NOT NULL,
    FOREIGN KEY (breed_id) REFERENCES breed_tb(breed_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Condition Type Table
CREATE TABLE condition_type_tb (
    condition_type_id SERIAL PRIMARY KEY,
    condition_name VARCHAR(50) NOT NULL,
    condition_unit VARCHAR(50) NOT NULL
);

-- Breed Conditions Table
CREATE TABLE breed_conditions (
    breed_condition_id SERIAL PRIMARY KEY,
    breed_id INTEGER NOT NULL,
    condition_min INTEGER NOT NULL,
    condition_max INTEGER NOT NULL,
    condition_status INTEGER NOT NULL DEFAULT 1,
    condition_type_id INTEGER NOT NULL,
    FOREIGN KEY (breed_id) REFERENCES breed_tb(breed_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (condition_type_id) REFERENCES condition_type_tb(condition_type_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Devices Table
CREATE TABLE devices_tb (
    device_no SERIAL PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL UNIQUE,
    device_name VARCHAR(50) NOT NULL,
    farm_id INTEGER NOT NULL,
    cell_no VARCHAR(20) NOT NULL DEFAULT 'none',
    device_picture VARCHAR(50) NOT NULL DEFAULT 'device_default.png',
    device_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (farm_id) REFERENCES farm_tb(farm_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Sensor Type Table
CREATE TABLE sensor_type_tb (
    sensor_type_id SERIAL PRIMARY KEY,
    sensor_type_name VARCHAR(50) NOT NULL,
    measurement_unit VARCHAR(20) NOT NULL
);

-- Sensors Table
CREATE TABLE sensors_tb (
    sensor_no SERIAL PRIMARY KEY,
    sensor_id INTEGER NOT NULL,
    sensor_type_id INTEGER NOT NULL,
    sensor_value DOUBLE PRECISION NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    device_no INTEGER NOT NULL,
    FOREIGN KEY (device_no) REFERENCES devices_tb(device_no) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sensor_type_id) REFERENCES sensor_type_tb(sensor_type_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Subscription Table
CREATE TABLE subsription_tb (
    sub_id SERIAL PRIMARY KEY,
    sub_name VARCHAR(50) NOT NULL,
    farm_size VARCHAR(20) NOT NULL,
    sub_cost INTEGER NOT NULL,
    sub_description VARCHAR(200) NOT NULL
);

-- Subscription Resources Table
CREATE TABLE subscription_resources (
    resource_id SERIAL PRIMARY KEY,
    resource_name VARCHAR(50) NOT NULL,
    resource_type INTEGER NOT NULL DEFAULT 0,
    unit_cost INTEGER NOT NULL,
    resource_status INTEGER NOT NULL DEFAULT 1
);

-- Farmer Subscription Table
CREATE TABLE farmers_subscription_tb (
    farmers_sub_id SERIAL PRIMARY KEY,
    sub_id INTEGER NOT NULL,
    farmer_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    farmer_sub_status INTEGER NOT NULL,
    discount INTEGER DEFAULT 0,
    FOREIGN KEY (farmer_id) REFERENCES farmers_tb(farmer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sub_id) REFERENCES subsription_tb(sub_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Farmer Subscription Payment Table
CREATE TABLE farmer_subscription_payment_tb (
    sub_payment_id SERIAL PRIMARY KEY,
    farmers_sub_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    pay_date DATE NOT NULL,
    receipt VARCHAR(50) NOT NULL DEFAULT 'no_receipt.jpg',
    pay_status INTEGER NOT NULL,
    FOREIGN KEY (farmers_sub_id) REFERENCES farmers_subscription_tb(farmers_sub_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Farmer Subscription Resources Table
CREATE TABLE farmer_subscription_resources (
    farmer_resource_id SERIAL PRIMARY KEY,
    resource_id INTEGER NOT NULL,
    resource_quantity INTEGER NOT NULL DEFAULT 1,
    farmer_resource_status INTEGER NOT NULL DEFAULT 1,
    farmers_sub_id INTEGER NOT NULL,
    FOREIGN KEY (farmers_sub_id) REFERENCES farmers_subscription_tb(farmers_sub_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES subscription_resources(resource_id) ON DELETE CASCADE ON UPDATE CASCADE
);
