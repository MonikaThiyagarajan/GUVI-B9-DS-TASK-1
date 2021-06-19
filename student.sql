-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2021 at 03:30 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `marks`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `ID` int(11) NOT NULL,
  `Name` varchar(10) NOT NULL,
  `School` varchar(10) NOT NULL,
  `Class` int(11) DEFAULT NULL,
  `Tamil` int(11) DEFAULT NULL,
  `English` int(11) DEFAULT NULL,
  `Math` int(11) DEFAULT NULL,
  `Science` int(11) DEFAULT NULL,
  `Social` int(11) DEFAULT NULL,
  `Total` varchar(255) DEFAULT NULL,
  `average` varchar(255) DEFAULT NULL,
  `Grade` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`ID`, `Name`, `School`, `Class`, `Tamil`, `English`, `Math`, `Science`, `Social`, `Total`, `average`, `Grade`) VALUES
(1, 'Monika', 'GRTMV', 10, 78, 84, 85, 86, 81, NULL, NULL, NULL),
(2, 'Vicky', 'St.Paul', 10, 83, 75, 54, 85, 62, NULL, NULL, NULL),
(3, 'Hari', 'DAV', 10, 65, 78, 92, 84, 67, NULL, NULL, NULL),
(4, 'Deepika', 'VGHSS', 10, 89, 62, 50, 68, 93, NULL, NULL, NULL),
(10, 'Monika', 'GRTMV', 8, 56, 65, 75, 85, 58, NULL, NULL, NULL),
(11, 'Karthika', 'GRTMV', 10, 85, 92, 56, 65, 75, NULL, NULL, NULL),
(12, 'Jessi', 'SCAI', 56, 54, 58, 57, 95, 92, '436', '87.2', ''),
(13, 'Surya', 'GRTMV', 10, 74, 85, 96, 71, 82, '408', '81.6', 'A'),
(14, 'Latha', 'GRTMV', 10, 65, 80, 100, 95, 98, '438', '87.6', 'A'),
(15, 'Trisha', 'GRTMV', 12, 65, 68, 69, 95, 94, '320', '64.0', 'B'),
(17, 'Thiyagu', 'GRTMV', 12, 95, 85, 100, 90, 85, '455', '91.0', 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
