#!/bin/bash


# 进入到 crack 目录
cd /root/patch


# 移动生成的公钥文件
cp ./.license_encryption_key.pub /opt/gitlab/embedded/service/gitlab-rails/.license_encryption_key.pub

# 修改 license.rb
sed -i 's/restricted_attr(:plan).presence || STARTER_PLAN/restricted_attr(:plan).presence || ULTIMATE_PLAN/g' /opt/gitlab/embedded/service/gitlab-rails/ee/app/models/license.rb
