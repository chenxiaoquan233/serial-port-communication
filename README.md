# Serial-Port-Communication

![](https://img.shields.io/badge/build-passing-brightgreen)
![](https://img.shields.io/badge/shell-bash-brightgreen)

厦门大学信息学院计算机网络课程实验

作者： [chenxiaoquan233](https://github.com/chenxiaoquan233)

<!-- TOC -->
## 目录

- [Serial-Port_Communication](#Serial-Port-Communication)
- [简介](#简介)
  * [注意](#注意)
- [运行环境](#运行环境)
- [使用教程](#使用教程)
  * [主机](#主机)
  * [从机](#从机)
- [Todo](#todo)
- [Change log](#change-log)
- [交流反馈](#交流反馈)
<!-- /TOC -->

## 简介
在两台虚拟机上通过命名管道模拟串口操作

### 注意
本操作通过对/dev/ttyS*设备读写完成，请在root权限下运行

## 运行环境
任一GNU/Linux发行版

## 使用教程

### 主机
进入bin文件夹，在终端运行：
```
sudo chmod +x master.sh
sudo ./master.sh
```
    
### 从机
进入bin文件夹，在终端运行：
```
sudo chmod +x slave.sh
sudo ./slave.sh
```

## Todo

## Change log

## 交流反馈
邮箱: chenxiaoquan233@gmail.com  
QQ: 770355275
