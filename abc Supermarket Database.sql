-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 07:49 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abc supermarket database`
--
CREATE DATABASE IF NOT EXISTS `abc supermarket database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `abc supermarket database`;

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `Job_Type` varchar(50) NOT NULL,
  `Job_Name` varchar(50) NOT NULL,
  `Job_ID` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`Job_Type`, `Job_Name`, `Job_ID`) VALUES
('Delivery', 'Driver', 101),
('Delivery', 'Deliveryman', 102),
('Delivery', 'Checker', 103),
('Sale', 'Sale Assistant (part time)', 201),
('Sale', 'Sale Assistant (full time)', 202),
('Sale', 'Senior Sale Assistant', 203),
('Operative', 'Loader', 301),
('Operative', 'Warehouseman', 302),
('Operative', 'Production Operative', 303);

-- --------------------------------------------------------

--
-- Table structure for table `job_apply`
--

CREATE TABLE `job_apply` (
  `Applicant_Name` varchar(50) NOT NULL,
  `Telephone` int(9) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Job_Name` varchar(50) NOT NULL,
  `Job_ID` int(4) NOT NULL,
  `Apply_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `User_Name(email)` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Date_of_Birth` date NOT NULL,
  `Register_Date` date NOT NULL,
  `Discount` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `Order_ID` int(10) NOT NULL,
  `Order_Product` varchar(2200) NOT NULL,
  `Title` varchar(5) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Phone_No` int(9) NOT NULL,
  `Address_Name` varchar(50) NOT NULL,
  `Floor` int(4) DEFAULT NULL,
  `Flat` varchar(4) DEFAULT NULL,
  `Block/Building` varchar(50) NOT NULL,
  `Estate/Street` varchar(50) NOT NULL,
  `District` varchar(25) NOT NULL,
  `Region` varchar(20) NOT NULL,
  `Payment_Method` varchar(15) NOT NULL,
  `Credit_C_Type` varchar(20) DEFAULT NULL,
  `Product_Price` int(10) NOT NULL,
  `Shipping_Price` int(3) NOT NULL,
  `Discount` varchar(4) NOT NULL,
  `Total_Price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `password_find`
--

CREATE TABLE `password_find` (
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_Name` varchar(50) NOT NULL,
  `Product_ID` int(5) NOT NULL,
  `Product_Category` varchar(50) NOT NULL,
  `Product_Price` int(5) NOT NULL,
  `Product_Brand` varchar(50) NOT NULL,
  `Product_Stock` int(5) NOT NULL,
  `Product_Total_Sale` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_Name`, `Product_ID`, `Product_Category`, `Product_Price`, `Product_Brand`, `Product_Stock`, `Product_Total_Sale`) VALUES
('Apple', 1001, 'Fruits', 3, 'Fruit Daily', 100, 0),
('Bananas (1 comb)', 1002, 'Fruits', 12, 'Fruit Daily', 100, 0),
('Orange', 1003, 'Fruits', 3, 'Fruit Daily', 100, 0),
('Green Grapes (1 bunch)', 1004, 'Fruits', 40, 'Fruit Daily', 100, 0),
('Purple Grapes (1 bunch)', 1005, 'Fruits', 40, 'Fruit Daily', 100, 0),
('Cherries (1 bunch)', 1006, 'Fruits', 26, 'Fruit Daily', 100, 0),
('Kiwi', 1007, 'Fruits', 2, 'Fruit Daily', 100, 0),
('Lemon', 1008, 'Fruits', 2, 'Fruit Daily', 100, 0),
('Mango', 1009, 'Fruits', 6, 'Fruit Daily', 100, 0),
('Pineapple', 1010, 'Fruits', 22, 'Fruit Daily', 100, 0),
('Chocolate Bar (100g)', 2001, 'Snacks', 6, 'FAVARGER', 100, 0),
('Milk Chocolate Bar (100g)', 2002, 'Snacks', 6, 'Lindt', 96, 4),
('Chocolate Biscuit Sticks (70g)', 2003, 'Snacks', 12, 'Pocky', 100, 0),
('Cookies & Cream Biscuit Sticks (70g)', 2004, 'Snacks', 12, 'Pocky', 100, 0),
('Strawberry Biscuit Sticks (70g)', 2005, 'Snacks', 12, 'Pocky', 96, 4),
('Chocolate Mini Swiss Roll (60g)', 2006, 'Snacks', 8, 'Garden', 99, 1),
('Peanut Mini Swiss Roll (60g)', 2007, 'Snacks', 8, 'Garden', 100, 0),
('Mango Mini Swiss Roll (60g)', 2008, 'Snacks', 8, 'Garden', 100, 0),
('Lemon Mini Swiss Roll (60g)', 2009, 'Snacks', 8, 'Garden', 100, 0),
('Biscuit Roll (200g)', 2010, 'Snacks', 12, 'Monteagle', 100, 0),
('Jam Biscuit (300g)', 2011, 'Snacks', 35, 'KOLSON', 100, 0),
('Cookies (300g)', 2012, 'Snacks', 30, 'Chips Ahoy', 100, 0),
('Potato Chips (226.8g)', 2013, 'Snacks', 20, 'Lay\'s', 100, 0),
('Soft Candies (116g)', 2014, 'Snacks', 10, 'nimm2', 100, 0),
('Marshmallows (150g)', 2015, 'Snacks', 18, 'Rocky Mountain', 100, 0),
('Popcorns (559.8g)', 2016, 'Snacks', 66, 'Orville Redenbacher\'s', 100, 0),
('Lemon Tea (250mL)', 3001, 'Drinks and Beverages', 4, 'VITA', 100, 0),
('Lemon Tea (6 packs - 250ml)', 3002, 'Drinks and Beverages', 20, 'VITA', 100, 0),
('Milk Tea (250ml)', 3003, 'Drinks and Beverages', 5, 'POKKA', 100, 0),
('Milk Tea (6 packs - 250ml)', 3004, 'Drinks and Beverages', 25, 'POKKA', 100, 0),
('Coca (330ml)', 3005, 'Drinks and Beverages', 4, 'Coca-Cola', 100, 0),
('Coca (8 cans - 330ml)', 3006, 'Drinks and Beverages', 28, 'Coca-Cola', 100, 0),
('Cream Soda (330ml)', 3007, 'Drinks and Beverages', 4, 'Schweppes', 100, 0),
('Cream Soda (8 cans - 330ml)', 3008, 'Drinks and Beverages', 28, 'Schweppes', 100, 0),
('Coffee (240ml)', 3009, 'Drinks and Beverages', 7, 'NESCAFE', 100, 0),
('Coffee (6 cans - 240ml)', 3010, 'Drinks and Beverages', 35, 'NESCAFE', 100, 0),
('Distilled Water (500ml)', 3011, 'Drinks and Beverages', 6, 'Bonaqua', 100, 0),
('Mineral Water (500ml)', 3012, 'Drinks and Beverages', 6, 'evian', 100, 0),
('Orange Juice (1gal)', 3013, 'Drinks and Beverages', 32, 'Great Value', 100, 0),
('Apple Juice (1gal)', 3014, 'Drinks and Beverages', 32, 'MOTTS', 100, 0),
('Milk (1gal)', 3015, 'Drinks and Beverages', 40, 'Great Value', 100, 0),
('Beer (650ml)', 4001, 'Wines', 30, 'Heineken', 100, 0),
('Vodka (1L)', 4002, 'Wines', 150, 'ABSOLUT VODKA', 100, 0),
('Champagne (750ml)', 4003, 'Wines', 300, 'MOET', 100, 0),
('Grape Wine (750ml)', 4004, 'Wines', 185, 'Gallo Family', 100, 0),
('White Wine (750ml)', 4005, 'Wines', 100, 'Pyramid Valley', 100, 0),
('Red Wine (750ml)', 4006, 'Wines', 250, 'MAURO', 100, 0),
('Whisky (375ml)', 4007, 'Wines', 325, 'Grown Royal', 100, 0),
('Tissues (7 sheets)', 5001, 'Cleaning Supllies, Health and Beauty', 3, 'Tempo', 100, 0),
('Tissues (18 packs - 7 sheets)', 5002, 'Cleaning Supllies, Health and Beauty', 30, 'Tempo', 100, 0),
('Box Tissues (90 sheets)', 5003, 'Cleaning Supllies, Health and Beauty', 32, 'Tempo', 100, 0),
('Toilet Paper (10 rolls)', 5004, 'Cleaning Supllies, Health and Beauty', 45, 'Tempo', 100, 0),
('Hand Towel', 5005, 'Cleaning Supllies, Health and Beauty', 25, 'HAND', 100, 0),
('Cotton Tips (300pcs)', 5006, 'Cleaning Supllies, Health and Beauty', 20, 'Cotton Tips', 100, 0),
('Body Lotion (400ml)', 5007, 'Cleaning Supllies, Health and Beauty', 40, 'NIVEA', 100, 0),
('Shampoo (400ml)', 5008, 'Cleaning Supllies, Health and Beauty', 22, 'head & shoulders', 100, 0),
('Body Wash (1L)', 5009, 'Cleaning Supllies, Health and Beauty', 34, 'Dove', 100, 0),
('Toothbrush (3 packs)', 5010, 'Cleaning Supllies, Health and Beauty', 10, 'Colgate', 100, 0),
('Toothpaste (170g)', 5011, 'Cleaning Supllies, Health and Beauty', 15, 'Colgate', 100, 0),
('Hand Sanitizer (520ml)', 5012, 'Cleaning Supllies, Health and Beauty', 40, 'Walch', 100, 0),
('Hand Wash (520ml)', 5013, 'Cleaning Supllies, Health and Beauty', 36, 'Dettol', 100, 0),
('Laundry Powder (1.6kg)', 5014, 'Cleaning Supllies, Health and Beauty', 80, 'Attack', 100, 0),
('Dish Soap (828ml)', 5015, 'Cleaning Supllies, Health and Beauty', 42, 'DAWN', 100, 0),
('Floor Cleaner (2L)', 5016, 'Cleaning Supllies, Health and Beauty', 70, 'LONG LIFE', 100, 0),
('Cat Food - Dry (3kg)', 6001, 'Pets', 50, 'TESCO', 100, 0),
('Dog Food - Dry (3kg)', 6002, 'Pets', 50, 'Pedigree', 100, 0),
('Cat Treats - Chicken (4 packs - 56g)', 6003, 'Pets', 14, 'Squeeze up', 100, 0),
('Cat Threat - Salmon Soft (482g)', 6004, 'Pets', 26, 'Irresistibles', 100, 0),
('Dog Treat - Marrowbone (500g)', 6005, 'Pets', 22, 'Pedigree', 100, 0),
('Dog Treat - Biscuits (500g)', 6006, 'Pets', 25, 'Pedigree', 100, 0),
('Cat Accessory - Catsan (5L)', 6007, 'Pets', 62, 'CATSAN', 100, 0),
('Dog Accessory - Leash & Collar', 6008, 'Pets', 150, 'flexi', 100, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`Job_ID`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`User_Name(email)`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`Order_ID`);

--
-- Indexes for table `password_find`
--
ALTER TABLE `password_find`
  ADD PRIMARY KEY (`Email`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`Product_ID`);
--
-- Database: `phpmyadmin`
--
CREATE DATABASE IF NOT EXISTS `phpmyadmin` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `phpmyadmin`;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
