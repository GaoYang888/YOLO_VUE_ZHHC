-- phpMyAdmin SQL Dump
-- version 4.4.15.10
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2023-08-23 17:13:37
-- 服务器版本： 5.6.50-log
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zhhc`
--

-- --------------------------------------------------------

--
-- 表的结构 `imginfo`
--

CREATE TABLE IF NOT EXISTS `imginfo` (
  `id` int(11) NOT NULL,
  `target_type_and_id` varchar(255) NOT NULL,
  `target_width` int(11) NOT NULL,
  `target_height` int(11) NOT NULL,
  `confidence` float NOT NULL,
  `detection_timestamp` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `imginfo`
--

INSERT INTO `imginfo` (`id`, `target_type_and_id`, `target_width`, `target_height`, `confidence`, `detection_timestamp`) VALUES
(26, 'person-01', 532, 507, 0.829, '2023-08-23 17:12:12'),
(27, '-----', 0, 0, 0, '2023-08-23 17:12:12'),
(28, 'person-01', 521, 508, 0.839, '2023-08-23 17:12:22'),
(29, '-----', 0, 0, 0, '2023-08-23 17:12:22'),
(30, 'person-01', 516, 509, 0.828, '2023-08-23 17:12:32'),
(31, '-----', 0, 0, 0, '2023-08-23 17:12:32'),
(32, 'person-01', 517, 503, 0.829, '2023-08-23 17:12:42'),
(33, '-----', 0, 0, 0, '2023-08-23 17:12:42'),
(34, 'person-01', 509, 501, 0.842, '2023-08-23 17:12:52'),
(35, '-----', 0, 0, 0, '2023-08-23 17:12:52'),
(36, 'person-01', 514, 503, 0.845, '2023-08-23 17:13:02'),
(37, '-----', 0, 0, 0, '2023-08-23 17:13:02'),
(38, '-----', 0, 0, 0, '2023-08-23 17:13:12'),
(39, '-----', 0, 0, 0, '2023-08-23 17:13:22'),
(40, '-----', 0, 0, 0, '2023-08-23 17:13:32');

-- --------------------------------------------------------

--
-- 表的结构 `testoverview`
--

CREATE TABLE IF NOT EXISTS `testoverview` (
  `监测时间` datetime NOT NULL,
  `人流量` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `testoverview`
--

INSERT INTO `testoverview` (`监测时间`, `人流量`) VALUES
('2023-08-23 16:33:38', 5),
('2023-08-23 16:34:46', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `imginfo`
--
ALTER TABLE `imginfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `testoverview`
--
ALTER TABLE `testoverview`
  ADD PRIMARY KEY (`监测时间`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `imginfo`
--
ALTER TABLE `imginfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=41;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
