/*
Navicat MySQL Data Transfer

Source Server         : mysql5.7
Source Server Version : 50738
Source Host           : localhost:3306
Source Database       : paperbarcode

Target Server Type    : MYSQL
Target Server Version : 50738
File Encoding         : 65001

Date: 2022-10-12 20:51:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `papercode`
-- ----------------------------
DROP TABLE IF EXISTS `papercode`;
CREATE TABLE `papercode` (
  `barcode` varchar(20) NOT NULL COMMENT ' 产品条码',
  `type` varchar(4) DEFAULT NULL,
  `scantime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `operator` varchar(10) DEFAULT NULL,
  `sheetNum` int(11) DEFAULT NULL,
  `lingNum` int(15) DEFAULT NULL,
  `lingID` varchar(20) DEFAULT NULL,
  `mainLingID` varchar(20) DEFAULT NULL,
  `state` varchar(4) DEFAULT NULL,
  'info'  varchar(500) DEFAULT NULL,	
  PRIMARY KEY (`barcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


