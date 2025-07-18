# GitLab Docker Environment

这个仓库提供了一个完整的 GitLab Docker 环境，包含自动化的 GitHub Actions 工作流程。

## 🚀 快速开始

### 本地开发

1. 克隆仓库：
   ```bash
   git clone https://github.com/Musicminion/gitlab-mwe.git
   cd gitlab-mwe
   ```

2. 启动 GitLab：
   ```bash
   docker-compose up -d
   ```

3. 访问 GitLab：
   - 打开浏览器访问 `http://localhost`
   - 默认用户名：`root`
   - 密码在 `config/initial_root_password` 文件中

### 使用 GitHub Codespaces

1. 点击仓库页面的 "Code" 按钮
2. 选择 "Codespaces" 标签
3. 点击 "Create codespace on main"
4. 等待环境自动构建完成

## 🔧 配置说明

### 许可证

```
eyJkYXRhIjogImRxWDR5QmVjUTdGNTM2bHo5MUFZZVQ2RnRnbEtWdzNDb3E4emJtOUhwTUhYM1RSOVRod3M2MnJQZFk0RytidWcyOHM2RmZzNnZudEpPdEZjVU1VekxIcE1IQUpMVlZzNWRpM1hHN2VReURqVHhMTHE5bHdNdml2c3FDQ3FCYTVSbXlnUHdGejFTbVhWZ3NCU2JiYVdMbGthT0phTElqbnhnMU5nOFJQaThmSVUxM2ppT1NvV0VUaFBZZ3dyOXlKOXYwMXpLMmdtWW1HVUFYQmwyRmhHdW5BaldkZi9XcmxiR0IyNEFlUzh3OFNkQ2M4RTlDSktzbk5aOGg1N3JOVUJ4RytjQ0k1WVNORG1IMytzT1BOdXpiZEszZmpCWE9RaU1iZWFNS0lObWpHQzMvVmhBRjNhU1JZZThoRDNlRjdvYUI4cklmMzZPaDFnbXZFSzd2Y1hZOXZLSm83VWp4VnNmZVA0dXM0QnM1ZUJ6Sy9ORGtYVzN5UHQ2ckxlTys2T092dnJ1a3VGMmpMLzdtdERCZCs0Q0dTWG4ySHZrbEltUEVJZW01MG1ubUtsNFlXK2hyYXZIOTdwTE1TZlpUU3NFcUFPREcrV1krd1dmYjJTbnlaZHp0S1NsVzNuWmM3RWo1YlBvSVRwVzhVemp4WnBEZmQ0V2MzUEh6U0E0bTBSaldMU3F2RjZuRjhreUdPaGRTYjV5VUp2ZmswYmFINndtNVdjQ1FCUEhlbVQrRXZOOU1obUJJeDhSclZmR3AzbXV3Qy9TVWtKZkZuQ2V1bkJvZm01RW5kQThwU0pxUU4rR3lJT3gwQ2pTWnJYd01Ob0Z4anMwS0VlUTFjZzFwVXJSNnhZVXlsNFNtcDdTQ1I3ZzNaQi9IQ3FpY1hiWWdCTU5UOHpCMjhPZjVsMzRURWx5T3NuNDRhSjc4NFcyWGEyelgyenU1d2JsYnJqc3NYdmVmZHNuQT09IiwgImtleSI6ICJmSnVUemxHSVdLbzlPaWlSQ1N1SFY2YWRiSmFEQ0xSL2pVeWpoZ1FXZSt3Y09BNENmS3cyajBWVTJ1Z1l1dGRHa3lnV0kzYmJKSGlLRVFtdlZUUmZ5QkdIQ0J3RzlRdVgvZWs0TTdHVkhqNlk2TktHMEUwd3BPK29aVmNXUk1sampJdVExaWlsdFZaRU54TlFVZTY0TDkvcE9MYUFFaHRwd0J4K0RJZGpPemsyUUQ3UWFRK3VIWEE5RHdTd3Y0TzkrZGd2NnhIR0hTVHBvTGYvNWtHdXNBVzZQaS9YcHBWY0F2NHIxT1FoVlFobjRscUt6ZTVMbjE1UVNPTlJ3a0xOTGNhVGpIK0dtUDk2Tit1djR2YzZLdEdKUDFKK0xwUnpiMU1Wbk9KRld2dys1RjdnSm12VktndnNzb29hVHpkSytKMnE4QVc5WGczSkR5bER5Q2UwRWc9PSIsICJpdiI6ICJhT2NCcEN1RmU4YVFVN0NtSVhsbmxRPT0ifQ==
```

### Docker Compose

- **GitLab CE/EE**: 最新版本
- **端口映射**:
  - `80`: HTTP 访问
  - `443`: HTTPS 访问
  - `22`: SSH 访问

### 数据持久化

- `./config`: GitLab 配置文件
- `./logs`: GitLab 日志
- `./data`: GitLab 数据（仓库、数据库等）

## 🤖 自动化工作流程

### GitHub Actions

1. **Prebuild (`.github/workflows/prebuild.yml`)**
   - 在每次推送到 main 分支时运行
   - 预拉取 Docker 镜像
   - 验证 Docker Compose 配置
   - 进行健康检查

2. **Update Images (`.github/workflows/update-images.yml`)**
   - 每周日自动运行
   - 检查并更新 Docker 镜像
   - 创建 PR 如果有更新

### GitHub Codespaces

- **开发容器配置** (`.devcontainer/devcontainer.json`)
- **自动端口转发**: 80, 443, 22
- **预装扩展**: Docker, GitLab Workflow
- **自动执行**: `docker-compose pull`

## 📋 使用指南

### 手动触发镜像更新

```bash
# 在 GitHub Actions 页面手动触发 "Update Docker Images" 工作流程
# 或者使用 GitHub CLI
gh workflow run update-images.yml
```

### 查看服务状态

```bash
# 查看所有服务状态
docker-compose ps

# 查看 GitLab 日志
docker-compose logs gitlab

# 重启服务
docker-compose restart gitlab
```

### 备份和恢复

```bash
# 备份数据
docker-compose exec gitlab gitlab-backup create

# 备份文件位置
ls -la data/backups/

# 恢复数据（替换 TIMESTAMP）
docker-compose exec gitlab gitlab-backup restore BACKUP=TIMESTAMP
```

## 🔒 安全注意事项

1. **更改默认密码**: 首次登录后立即更改 root 密码
2. **SSL 证书**: 生产环境建议配置 SSL 证书
3. **防火墙**: 确保只有必要的端口对外开放
4. **定期备份**: 设置定期数据备份

## 🛠️ 故障排除

### 常见问题

1. **GitLab 启动慢**
   - 正常情况，GitLab 初次启动需要 2-5 分钟
   - 查看日志: `docker-compose logs -f gitlab`

2. **端口冲突**
   - 修改 `docker-compose.yml` 中的端口映射
   - 确保本地没有其他服务占用相同端口

3. **磁盘空间不足**
   - 清理 Docker 镜像: `docker system prune -f`
   - 检查 `./data` 目录大小

### 日志位置

- **GitLab 日志**: `./logs/`
- **Docker 日志**: `docker-compose logs`
- **系统日志**: `./logs/reconfigure/`

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

[MIT License](LICENSE)
