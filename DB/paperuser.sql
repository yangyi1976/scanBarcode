/*
Navicat MySQL Data Transfer

Source Server         : mysql5.7
Source Server Version : 50738
Source Host           : localhost:3306
Source Database       : paperbarcode

Target Server Type    : MYSQL
Target Server Version : 50738
File Encoding         : 65001

Date: 2022-10-12 20:51:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `paperuser`
-- ----------------------------
DROP TABLE IF EXISTS `paperuser`;
CREATE TABLE `paperuser` (
  `usercode` varchar(18) NOT NULL DEFAULT '' COMMENT '用户条码',
  `username` varchar(8) NOT NULL COMMENT '姓名',
  `group` varchar(10) DEFAULT NULL COMMENT '班组',
  PRIMARY KEY (`usercode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of paperuser
-- ----------------------------
INSERT INTO `paperuser` VALUES ('6918163020886', '选纸1', null);
