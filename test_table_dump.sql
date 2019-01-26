-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 26, 2019 at 04:10 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `turbosms`
--

-- --------------------------------------------------------

--
-- Table structure for table `turbosms_smsrecord`
--

CREATE TABLE `turbosms_smsrecord` (
  `id` int(11) NOT NULL,
  `msg_id` varchar(36) NOT NULL,
  `number` varchar(21) NOT NULL,
  `sign` varchar(21) NOT NULL,
  `message` longtext NOT NULL,
  `wappush` varchar(128) NOT NULL,
  `is_flash` tinyint(1) NOT NULL,
  `cost` decimal(4,2) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `added` datetime(6) NOT NULL,
  `send_time` datetime(6) NOT NULL,
  `sended` datetime(6) NOT NULL,
  `received` datetime(6) NOT NULL,
  `error_code` varchar(3) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `turbosms_smsrecord`
--
ALTER TABLE `turbosms_smsrecord`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `turbosms_smsrecord`
--
ALTER TABLE `turbosms_smsrecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
