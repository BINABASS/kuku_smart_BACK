-- Drop existing tables if they exist
DROP TABLE IF EXISTS activity_schedule_tb;
DROP TABLE IF EXISTS activity_type_tb;
DROP TABLE IF EXISTS batch_activity_tb;
DROP TABLE IF EXISTS batch_feeding_tb;
DROP TABLE IF EXISTS batches_tb;
DROP TABLE IF EXISTS breed_activities_tb;
DROP TABLE IF EXISTS breed_conditions;
DROP TABLE IF EXISTS breed_feeding_tb;
DROP TABLE IF EXISTS breed_growth_tb;
DROP TABLE IF EXISTS breed_tb;
DROP TABLE IF EXISTS breed_type_tb;
DROP TABLE IF EXISTS condition_type_tb;
DROP TABLE IF EXISTS devices_tb;
DROP TABLE IF EXISTS farm_tb;
DROP TABLE IF EXISTS farmer_subscription_payment_tb;
DROP TABLE IF EXISTS farmer_subscription_resources;
DROP TABLE IF EXISTS farmers_subscription_tb;
DROP TABLE IF EXISTS farmers_tb;
DROP TABLE IF EXISTS feeding_type_tb;
DROP TABLE IF EXISTS food_type_tb;
DROP TABLE IF EXISTS sensor_type_tb;
DROP TABLE IF EXISTS sensors_tb;
DROP TABLE IF EXISTS subscription_resources;
DROP TABLE IF EXISTS subsription_tb;
DROP TABLE IF EXISTS users_tb;

-- Create tables
CREATE TABLE breed_type_tb (
    breed_typeID SERIAL PRIMARY KEY,
    breedType VARCHAR(50) NOT NULL
);

CREATE TABLE breed_tb (
    breedID SERIAL PRIMARY KEY,
    breedName VARCHAR(50) NOT NULL,
    breed_typeID INTEGER NOT NULL,
    preedphoto VARCHAR(50) NOT NULL DEFAULT 'preedphoto.png',
    FOREIGN KEY (breed_typeID) REFERENCES breed_type_tb(breed_typeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE breed_growth_tb (
    breedGrowthID SERIAL PRIMARY KEY,
    breedID INTEGER NOT NULL,
    age INTEGER NOT NULL,
    minWeight INTEGER NOT NULL,
    FOREIGN KEY (breedID) REFERENCES breed_tb(breedID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE food_type_tb (
    foodTypeID SERIAL PRIMARY KEY,
    foodName VARCHAR(50) NOT NULL
);

CREATE TABLE breed_feeding_tb (
    breedFeedingID SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL DEFAULT 0,
    breed_feed_status INTEGER NOT NULL DEFAULT 1,
    breedID INTEGER NOT NULL,
    foodTypeID INTEGER NOT NULL,
    age INTEGER NOT NULL,
    frequency INTEGER NOT NULL,
    FOREIGN KEY (breedID) REFERENCES breed_tb(breedID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (foodTypeID) REFERENCES food_type_tb(foodTypeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE condition_type_tb (
    condition_typeID SERIAL PRIMARY KEY,
    conditionName VARCHAR(50) NOT NULL,
    condition_unit VARCHAR(50) NOT NULL
);

CREATE TABLE breed_conditions (
    breed_conditionID SERIAL PRIMARY KEY,
    breedID INTEGER NOT NULL,
    condictionMin INTEGER NOT NULL,
    conditionMax INTEGER NOT NULL,
    condition_status INTEGER NOT NULL DEFAULT 1,
    condition_typeID INTEGER NOT NULL,
    FOREIGN KEY (breedID) REFERENCES breed_tb(breedID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (condition_typeID) REFERENCES condition_type_tb(condition_typeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE activity_type_tb (
    activityTypeID SERIAL PRIMARY KEY,
    activityType VARCHAR(50) NOT NULL
);

CREATE TABLE breed_activities_tb (
    breedActivityID SERIAL PRIMARY KEY,
    breedID INTEGER NOT NULL,
    activityTypeID INTEGER NOT NULL,
    age INTEGER NOT NULL,
    breed_activity_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (breedID) REFERENCES breed_tb(breedID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (activityTypeID) REFERENCES activity_type_tb(activityTypeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE farmers_tb (
    farmerID SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    fullName VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    createdDate DATE DEFAULT CURRENT_DATE
);

CREATE TABLE farm_tb (
    farmID SERIAL PRIMARY KEY,
    farmName VARCHAR(200) NOT NULL,
    location VARCHAR(200) NOT NULL,
    farmSize VARCHAR(50) NOT NULL,
    farmerID INTEGER NOT NULL,
    FOREIGN KEY (farmerID) REFERENCES farmers_tb(farmerID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE batches_tb (
    batchID SERIAL PRIMARY KEY,
    farmID INTEGER NOT NULL,
    breedID INTEGER NOT NULL,
    arriveDate DATE NOT NULL,
    initAge INTEGER NOT NULL,
    harvestAge INTEGER NOT NULL DEFAULT 0,
    quantity INTEGER NOT NULL,
    initWeight INTEGER NOT NULL,
    batch_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (farmID) REFERENCES farm_tb(farmID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (breedID) REFERENCES breed_tb(breedID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE batch_activity_tb (
    batchActivityID SERIAL PRIMARY KEY,
    batchID INTEGER NOT NULL,
    breedActivityID INTEGER NOT NULL,
    batchActivityName VARCHAR(100) NOT NULL,
    batchActivityDate DATE NOT NULL,
    batchActivityDetails VARCHAR(50) NOT NULL,
    batchAcitivtyCost INTEGER NOT NULL,
    FOREIGN KEY (batchID) REFERENCES batches_tb(batchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (breedActivityID) REFERENCES breed_activities_tb(breedActivityID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE batch_feeding_tb (
    batchFeedingID SERIAL PRIMARY KEY,
    batchID INTEGER NOT NULL,
    feedingDate DATE NOT NULL DEFAULT CURRENT_DATE,
    feedingAmount INTEGER NOT NULL,
    status INTEGER NOT NULL,
    FOREIGN KEY (batchID) REFERENCES batches_tb(batchID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE activity_schedule_tb (
    activityID SERIAL PRIMARY KEY,
    batchID INTEGER NOT NULL,
    activityName VARCHAR(100) NOT NULL,
    activityDescription VARCHAR(300) NOT NULL,
    activityDay VARCHAR(10) NOT NULL DEFAULT 'Day',
    activity_status INTEGER NOT NULL,
    activity_frequency INTEGER NOT NULL,
    FOREIGN KEY (batchID) REFERENCES batches_tb(batchID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE sensor_type_tb (
    sensorTypeID SERIAL PRIMARY KEY,
    sensorTypeName VARCHAR(50) NOT NULL,
    measurementUnit VARCHAR(20) NOT NULL
);

CREATE TABLE devices_tb (
    deviceNo SERIAL PRIMARY KEY,
    deviceID VARCHAR(50) NOT NULL UNIQUE,
    deviceName VARCHAR(50) NOT NULL,
    farmID INTEGER NOT NULL,
    cellNo VARCHAR(20) NOT NULL DEFAULT 'none',
    device_picture VARCHAR(50) NOT NULL DEFAULT 'device_default.png',
    device_status INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (farmID) REFERENCES farm_tb(farmID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE sensors_tb (
    sensorNo SERIAL PRIMARY KEY,
    sensorID INTEGER NOT NULL,
    sensorTypeID INTEGER NOT NULL,
    sensorValue DOUBLE PRECISION NOT NULL,
    timeStamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deviceNo INTEGER NOT NULL,
    FOREIGN KEY (deviceNo) REFERENCES devices_tb(deviceNo) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sensorTypeID) REFERENCES sensor_type_tb(sensorTypeID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE subsription_tb (
    subID SERIAL PRIMARY KEY,
    subName VARCHAR(50) NOT NULL,
    farmSize VARCHAR(20) NOT NULL,
    subCost INTEGER NOT NULL,
    subDescription VARCHAR(200) NOT NULL
);

CREATE TABLE subscription_resources (
    resourceID SERIAL PRIMARY KEY,
    resource_name VARCHAR(50) NOT NULL,
    resource_type INTEGER NOT NULL DEFAULT 0,
    unit_cost INTEGER NOT NULL,
    resource_status INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE farmers_subscription_tb (
    farmersSubID SERIAL PRIMARY KEY,
    subID INTEGER NOT NULL,
    farmerID INTEGER NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    farmer_sub_status INTEGER NOT NULL,
    discount INTEGER DEFAULT 0,
    FOREIGN KEY (farmerID) REFERENCES farmers_tb(farmerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (subID) REFERENCES subsription_tb(subID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE farmer_subscription_resources (
    farmer_resourceID SERIAL PRIMARY KEY,
    resourceID INTEGER NOT NULL,
    resource_quantity INTEGER NOT NULL DEFAULT 1,
    farmer_resource_status INTEGER NOT NULL DEFAULT 1,
    farmersSubID INTEGER NOT NULL,
    FOREIGN KEY (farmersSubID) REFERENCES farmers_subscription_tb(farmersSubID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (resourceID) REFERENCES subscription_resources(resourceID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE farmer_subscription_payment_tb (
    subPaymentID SERIAL PRIMARY KEY,
    farmersSubID INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    payDate DATE NOT NULL,
    receipt VARCHAR(50) NOT NULL DEFAULT 'no_receipt.jpg',
    payStatus INTEGER NOT NULL,
    FOREIGN KEY (farmersSubID) REFERENCES farmers_subscription_tb(farmersSubID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users_tb (
    userID SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    userRole INTEGER NOT NULL DEFAULT 0,
    userStatus INTEGER NOT NULL DEFAULT 0,
    lastLogin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    profile VARCHAR(50) NOT NULL DEFAULT 'default.png'
);
