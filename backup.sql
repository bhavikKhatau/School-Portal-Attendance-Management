-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.54-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema project
--

CREATE DATABASE IF NOT EXISTS project;
USE project;

--
-- Definition of table `eleven_a`
--

DROP TABLE IF EXISTS `eleven_a`;
CREATE TABLE `eleven_a` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_a`
--

/*!40000 ALTER TABLE `eleven_a` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_a` ENABLE KEYS */;


--
-- Definition of table `eleven_a_attendance`
--

DROP TABLE IF EXISTS `eleven_a_attendance`;
CREATE TABLE `eleven_a_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_a_attendance`
--

/*!40000 ALTER TABLE `eleven_a_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_a_attendance` ENABLE KEYS */;


--
-- Definition of table `eleven_b`
--

DROP TABLE IF EXISTS `eleven_b`;
CREATE TABLE `eleven_b` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_b`
--

/*!40000 ALTER TABLE `eleven_b` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_b` ENABLE KEYS */;


--
-- Definition of table `eleven_b_attendance`
--

DROP TABLE IF EXISTS `eleven_b_attendance`;
CREATE TABLE `eleven_b_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_b_attendance`
--

/*!40000 ALTER TABLE `eleven_b_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_b_attendance` ENABLE KEYS */;


--
-- Definition of table `eleven_c`
--

DROP TABLE IF EXISTS `eleven_c`;
CREATE TABLE `eleven_c` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_c`
--

/*!40000 ALTER TABLE `eleven_c` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_c` ENABLE KEYS */;


--
-- Definition of table `eleven_c_attendance`
--

DROP TABLE IF EXISTS `eleven_c_attendance`;
CREATE TABLE `eleven_c_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eleven_c_attendance`
--

/*!40000 ALTER TABLE `eleven_c_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `eleven_c_attendance` ENABLE KEYS */;


--
-- Definition of table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
CREATE TABLE `teachers` (
  `name` text NOT NULL,
  `email` varchar(45) NOT NULL DEFAULT '',
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers`
--

/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;


--
-- Definition of table `twelve_a`
--

DROP TABLE IF EXISTS `twelve_a`;
CREATE TABLE `twelve_a` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_a`
--

/*!40000 ALTER TABLE `twelve_a` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_a` ENABLE KEYS */;


--
-- Definition of table `twelve_a_attendance`
--

DROP TABLE IF EXISTS `twelve_a_attendance`;
CREATE TABLE `twelve_a_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_a_attendance`
--

/*!40000 ALTER TABLE `twelve_a_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_a_attendance` ENABLE KEYS */;


--
-- Definition of table `twelve_b`
--

DROP TABLE IF EXISTS `twelve_b`;
CREATE TABLE `twelve_b` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_b`
--

/*!40000 ALTER TABLE `twelve_b` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_b` ENABLE KEYS */;


--
-- Definition of table `twelve_b_attendance`
--

DROP TABLE IF EXISTS `twelve_b_attendance`;
CREATE TABLE `twelve_b_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_b_attendance`
--

/*!40000 ALTER TABLE `twelve_b_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_b_attendance` ENABLE KEYS */;


--
-- Definition of table `twelve_c`
--

DROP TABLE IF EXISTS `twelve_c`;
CREATE TABLE `twelve_c` (
  `GR_No` varchar(45) NOT NULL,
  `Roll_No` varchar(11) NOT NULL,
  `Name` text NOT NULL,
  `Gender` text NOT NULL,
  PRIMARY KEY (`Roll_No`,`GR_No`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_c`
--

/*!40000 ALTER TABLE `twelve_c` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_c` ENABLE KEYS */;


--
-- Definition of table `twelve_c_attendance`
--

DROP TABLE IF EXISTS `twelve_c_attendance`;
CREATE TABLE `twelve_c_attendance` (
  `date` varchar(11) NOT NULL,
  `GR_No` varchar(45) NOT NULL,
  `roll_no` varchar(11) NOT NULL DEFAULT '0',
  `name` text NOT NULL,
  `Gender` text NOT NULL,
  `attendance` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `twelve_c_attendance`
--

/*!40000 ALTER TABLE `twelve_c_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `twelve_c_attendance` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
