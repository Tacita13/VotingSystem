-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 18, 2018 at 09:36 PM
-- Server version: 5.6.34-log
-- PHP Version: 7.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upr-2fast4u-voting`
--

drop table if exists Voting;
drop table if exists User_Confirmation;
drop table if exists Results;
drop table if exists Question;
drop table if exists Group_Permission;
drop table if exists Create_Group;
drop table if exists User;

-- --------------------------------------------------------

--
-- Table structure for table `create_group`
--

CREATE TABLE `create_group` (
  `group_id` varchar(10) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `group_creator` varchar(20) NOT NULL,
  `group_name` varchar(50) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `create_group`
--

INSERT INTO `create_group` (`group_id`, `user_id`, `group_creator`, `group_name`, `date_created`) VALUES
('1', '1', 'admin', 'prueba01', CURRENT_DATE());

-- --------------------------------------------------------

--
-- Table structure for table `group_permission`
--

CREATE TABLE `group_permission` (
  `permission_id` varchar(10) NOT NULL,
  `group_id` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `permission_creator` varchar(50) NOT NULL,
  `group_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `group_permission`
--


-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `question_id` varchar(15) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `group_name` varchar(50) NOT NULL,
  `question_creator` varchar(20) NOT NULL,
  `question_type` varchar(20) NOT NULL,
  `question_title` varchar(50) NOT NULL,
  `question_description` varchar(500) NOT NULL,
  `voting_status` varchar(20) DEFAULT NULL,
  `question_author` varchar(20) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--



-- --------------------------------------------------------

--
-- Table structure for table `results`
--

CREATE TABLE `results` (
  `result_id` varchar(10) NOT NULL,
  `question_id` varchar(10) NOT NULL,
  `question_title` varchar(50) NOT NULL,
  `question_type` varchar(20) NOT NULL,
  `group_name` varchar(50) NOT NULL,
  `count_yes` int(3) DEFAULT NULL,
  `count_no` int(3) DEFAULT NULL,
  `count_abstain` int(3) DEFAULT NULL,
  `total_voters` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `student_number` varchar(15) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `username`, `name`, `last_name`, `user_type`, `password`, `email`, `student_number`, `date_created`) VALUES
('1', 'admin', 'admin', 'B', 'Staff', '4dff4ea340f0a823f15d3f4f01ab62', 'admin@admin.com', '801-15-9203', CURRENT_DATE());

-- --------------------------------------------------------

--
-- Table structure for table `user_confirmation`
--

CREATE TABLE `user_confirmation` (
  `user_confirmationID` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `Email_key` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `voting`
--

CREATE TABLE `voting` (
  `voting_id` varchar(20) NOT NULL,
  `question_id` varchar(10) NOT NULL,
  `group_name` varchar(50) NOT NULL,
  `question_title` varchar(50) NOT NULL,
  `question_type` varchar(20) NOT NULL,
  `voting_choice` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create_group`
--
ALTER TABLE `create_group`
  ADD PRIMARY KEY (`group_id`),
  ADD UNIQUE KEY `UC_Group` (`group_id`,`group_name`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `group_permission`
--
ALTER TABLE `group_permission`
  ADD PRIMARY KEY (`permission_id`),
  ADD UNIQUE KEY `permission_id` (`permission_id`),
  ADD KEY `group_id` (`group_id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`question_id`),
  ADD UNIQUE KEY `question_id` (`question_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`result_id`,`question_title`),
  ADD UNIQUE KEY `result_id` (`result_id`,`question_title`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `UC_User` (`user_id`,`username`,`email`,`student_number`);

--
-- Indexes for table `user_confirmation`
--
ALTER TABLE `user_confirmation`
  ADD PRIMARY KEY (`user_confirmationID`),
  ADD UNIQUE KEY `UC_User` (`Email_key`);

--
-- Indexes for table `voting`
--
ALTER TABLE `voting`
  ADD PRIMARY KEY (`voting_id`,`question_title`),
  ADD UNIQUE KEY `voting_id` (`voting_id`,`question_title`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `create_group`
--
ALTER TABLE `create_group`
  ADD CONSTRAINT `create_group_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
